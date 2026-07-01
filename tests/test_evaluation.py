import os
import sys
import torch
import tempfile
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from evaluation.metrics import calculate_psnr, calculate_mse, calculate_ssim, evaluate_predictions

def test_metrics_identical():
    img1 = torch.ones(1, 1, 64, 64)
    img2 = torch.ones(1, 1, 64, 64)
    
    mse = calculate_mse(img1, img2)
    assert mse == 0.0
    
    ssim = calculate_ssim(img1, img2)
    assert ssim == 1.0

def test_evaluate_predictions():
    p = torch.rand(2, 1, 64, 64)
    t = torch.rand(2, 1, 64, 64)
    with tempfile.TemporaryDirectory() as tmpdir:
        metrics = evaluate_predictions(p, t, output_dir=tmpdir)
        assert "PSNR" in metrics
        assert "SSIM" in metrics
        assert os.path.exists(os.path.join(tmpdir, "evaluation_metrics.csv"))
        assert os.path.exists(os.path.join(tmpdir, "comparison_0.png"))
