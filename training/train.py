import os
import yaml
import logging
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

class GeoDataset(Dataset):
    """
    Dataset that provides T0, T1 (ground truth), T2.
    In a real scenario, this reads from the triplets_manifest.txt and loads NetCDF files via xarray.
    """
    def __init__(self, size=10, resolution=(512, 512)):
        self.size = size
        self.res = resolution
    
    def __len__(self):
        return self.size
        
    def __getitem__(self, idx):
        # Channels=1 (TIR)
        return torch.rand(1, *self.res), torch.rand(1, *self.res), torch.rand(1, *self.res)

def train(config):
    logger.info("Initializing Training Pipeline...")
    mixed_precision = config["training"]["mixed_precision"]
    epochs = config["training"]["epochs"]
    batch_size = config["training"]["batch_size"]
    lr = float(config["training"]["learning_rate"])
    log_dir = config["training"]["tensorboard_log_dir"]
    checkpoint_dir = config["training"]["checkpoint_dir"]
    
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(checkpoint_dir, exist_ok=True)
    
    writer = SummaryWriter(log_dir=log_dir)
    
    dataset = GeoDataset(size=20, resolution=config["preprocessing"].get("output_resolution", [256, 256]))
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    # Benchmarking logic - loop through candidates or select from config
    model_name = "RIFE"
    from models.frame_interpolation import select_model
    model = select_model(model_name, channels=1)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    scaler = torch.cuda.amp.GradScaler(enabled=mixed_precision and device.type == 'cuda')
    criterion = nn.MSELoss()
    
    logger.info(f"Starting training on {device} for {epochs} epochs with mixed precision: {mixed_precision}")
    
    # Checkpoint Resume Logic
    ckpt_path = os.path.join(checkpoint_dir, "latest.pth")
    start_epoch = 0
    if os.path.exists(ckpt_path):
        logger.info(f"Resuming from checkpoint {ckpt_path}")
        checkpoint = torch.load(ckpt_path, map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint['epoch']
    
    for epoch in range(start_epoch, epochs):
        model.train()
        epoch_loss = 0.0
        for step, (t0, t1, t2) in enumerate(loader):
            t0, t1, t2 = t0.to(device), t1.to(device), t2.to(device)
            optimizer.zero_grad(set_to_none=True)
            
            with torch.cuda.amp.autocast(enabled=mixed_precision and device.type == 'cuda'):
                pred = model(t0, t2)
                loss = criterion(pred, t1)
            
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            
            epoch_loss += loss.item()
            
        avg_loss = epoch_loss / len(loader)
        scheduler.step()
        
        logger.info(f"Epoch [{epoch+1}/{epochs}] Loss: {avg_loss:.4f} LR: {scheduler.get_last_lr()[0]:.6f}")
        writer.add_scalar("Loss/train", avg_loss, epoch)
        
        # Save Checkpoint
        torch.save({
            'epoch': epoch + 1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': avg_loss,
        }, ckpt_path)
        
    writer.close()
    logger.info("Model Training Phase Completed Successfully.")

if __name__ == "__main__":
    config = load_config()
    train(config)
