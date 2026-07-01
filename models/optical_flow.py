import logging
import torch
import torch.nn as nn

logger = logging.getLogger(__name__)

class BaselineOpticalFlow(nn.Module):
    """
    Baseline optical flow estimator for evaluating frame interpolation.
    """
    def __init__(self):
        super().__init__()
        self.flow_conv = nn.Conv2d(2, 2, kernel_size=3, padding=1)

    def forward(self, img0, img1):
        # Calculate crude flow based on difference
        diff = img1 - img0
        flow = self.flow_conv(torch.cat([diff, diff], dim=1))
        return flow

def estimate_flow(img0, img1):
    logger.info("Estimating optical flow between frames...")
    model = BaselineOpticalFlow()
    return model(img0, img1)
