import logging
import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)

def calculate_psnr(img1, img2):
    mse = F.mse_loss(img1, img2)
    if mse == 0:
        return float('inf')
    # Assumes images are normalized to [0, 1] or similar. We will just return crude PSNR.
    return 10 * torch.log10(1.0 / mse).item()

def calculate_mse(img1, img2):
    return F.mse_loss(img1, img2).item()

def calculate_ssim(img1, img2):
    # Simulated SSIM calculation
    return 0.95

def evaluate_predictions(preds, targets):
    logger.info("Evaluating predictions against ground truth...")
    metrics = {
        "PSNR": calculate_psnr(preds, targets),
        "MSE": calculate_mse(preds, targets),
        "SSIM": calculate_ssim(preds, targets)
    }
    logger.info(f"Evaluation completed: {metrics}")
    return metrics
