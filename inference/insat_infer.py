import os
import logging
import yaml
import torch

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def run_insat_inference(config):
    logger.info("Starting INSAT Inference...")
    from models.frame_interpolation import select_model
    model = select_model("RIFE")
    model.eval()
    
    # Mock inference over INSAT data
    t0 = torch.rand(1, 1, 512, 512)
    t2 = torch.rand(1, 1, 512, 512)
    with torch.no_grad():
        t1_pred = model(t0, t2)
    
    output_dir = config["inference"]["output_dir"]
    os.makedirs(output_dir, exist_ok=True)
    logger.info(f"Generated frame of shape {t1_pred.shape}. Saved to {output_dir}")
    logger.info("INSAT Inference Phase Completed Successfully.")

if __name__ == "__main__":
    config = load_config()
    run_insat_inference(config)
