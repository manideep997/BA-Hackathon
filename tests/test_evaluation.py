import os
import sys
import torch

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from evaluation.metrics import calculate_psnr, calculate_mse, calculate_ssim

def test_metrics():
    img1 = torch.ones(1, 1, 64, 64)
    img2 = torch.ones(1, 1, 64, 64)
    
    mse = calculate_mse(img1, img2)
    assert mse == 0.0
    
    psnr = calculate_psnr(img1, img2)
    assert psnr == float('inf')
    
    ssim = calculate_ssim(img1, img2)
    assert ssim > 0.0
