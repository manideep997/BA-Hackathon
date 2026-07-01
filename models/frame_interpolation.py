import torch
import torch.nn as nn
import logging

logger = logging.getLogger(__name__)

class UNetFlowEstimator(nn.Module):
    """
    A simplified U-Net based flow estimator representing architectures like RAFT or RIFE's IFNet.
    """
    def __init__(self, in_channels=2, out_channels=4):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, 16, 3, 2, 1), nn.ReLU(inplace=True),
            nn.Conv2d(16, 32, 3, 2, 1), nn.ReLU(inplace=True),
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, 4, 2, 1), nn.ReLU(inplace=True),
            nn.ConvTranspose2d(16, out_channels, 4, 2, 1)
        )
        
    def forward(self, x):
        features = self.encoder(x)
        return self.decoder(features)

class RIFE(nn.Module):
    """
    Real-Time Intermediate Flow Estimation (RIFE).
    Generates Bi-directional flows and a blending mask.
    """
    def __init__(self, channels=1):
        super().__init__()
        # Input: T0 and T2 concatenated
        self.ifnet = UNetFlowEstimator(in_channels=channels*2, out_channels=5) # 4 for flow (F0->1, F2->1), 1 for mask
        
    def forward(self, img0, img2):
        x = torch.cat((img0, img2), dim=1)
        flow_and_mask = self.ifnet(x)
        
        flow01 = flow_and_mask[:, 0:2, :, :]
        flow21 = flow_and_mask[:, 2:4, :, :]
        mask = torch.sigmoid(flow_and_mask[:, 4:5, :, :])
        
        # Warp logic (simulated with grid_sample in a real pipeline)
        # Here we just generate an interpolated output for benchmarking purposes
        warped0 = img0 + flow01.mean() * 0 # Mock warp
        warped2 = img2 + flow21.mean() * 0 # Mock warp
        
        output = warped0 * mask + warped2 * (1 - mask)
        return output

class IFRNet(nn.Module):
    def __init__(self, channels=1):
        super().__init__()
        self.encoder = UNetFlowEstimator(in_channels=channels*2, out_channels=channels)
    def forward(self, img0, img2):
        return self.encoder(torch.cat((img0, img2), dim=1))

class SuperSloMo(nn.Module):
    def __init__(self, channels=1):
        super().__init__()
        self.flow_comp = UNetFlowEstimator(in_channels=channels*2, out_channels=channels)
    def forward(self, img0, img2):
        return self.flow_comp(torch.cat((img0, img2), dim=1))

class EMA_VFI(nn.Module):
    def __init__(self, channels=1):
        super().__init__()
        self.extract = UNetFlowEstimator(in_channels=channels*2, out_channels=channels)
    def forward(self, img0, img2):
        return self.extract(torch.cat((img0, img2), dim=1))

def select_model(model_name="RIFE", channels=1):
    logger.info(f"Initializing model architecture: {model_name}")
    models = {
        "RIFE": RIFE(channels),
        "IFRNet": IFRNet(channels),
        "SuperSloMo": SuperSloMo(channels),
        "EMA-VFI": EMA_VFI(channels)
    }
    if model_name not in models:
        raise ValueError(f"Model {model_name} not supported.")
    return models[model_name]
