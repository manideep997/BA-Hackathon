import os
import sys
import torch

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.frame_interpolation import BaselineInterpolator
from models.optical_flow import BaselineOpticalFlow

def test_frame_interpolation_forward():
    model = BaselineInterpolator(channels=1)
    img0 = torch.rand(1, 1, 64, 64)
    img1 = torch.rand(1, 1, 64, 64)
    out = model(img0, img1)
    assert out.shape == (1, 1, 64, 64)

def test_optical_flow_forward():
    model = BaselineOpticalFlow()
    img0 = torch.rand(1, 1, 64, 64)
    img1 = torch.rand(1, 1, 64, 64)
    flow = model(img0, img1)
    assert flow.shape == (1, 2, 64, 64)
