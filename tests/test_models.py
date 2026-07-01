import os
import sys
import torch

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.frame_interpolation import select_model
from models.optical_flow import BaselineOpticalFlow

def test_frame_interpolation_architectures():
    models = ["RIFE", "IFRNet", "SuperSloMo", "EMA-VFI"]
    img0 = torch.rand(2, 1, 64, 64)
    img2 = torch.rand(2, 1, 64, 64)
    
    for m in models:
        model = select_model(m, channels=1)
        out = model(img0, img2)
        assert out.shape == (2, 1, 64, 64), f"Model {m} output shape mismatch"

def test_optical_flow_forward():
    model = BaselineOpticalFlow()
    img0 = torch.rand(1, 1, 64, 64)
    img1 = torch.rand(1, 1, 64, 64)
    flow = model(img0, img1)
    assert flow.shape == (1, 2, 64, 64)
