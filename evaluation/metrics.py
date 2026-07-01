import os
import logging
import torch
import torch.nn.functional as F
import numpy as np
import pandas as pd
from skimage.metrics import structural_similarity as ssim_metric
from skimage.metrics import peak_signal_noise_ratio as psnr_metric
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def calculate_mse(img1, img2):
    return F.mse_loss(img1, img2).item()

def calculate_psnr(img1, img2):
    i1 = img1.squeeze().detach().cpu().numpy()
    i2 = img2.squeeze().detach().cpu().numpy()
    # Assuming normalized to [0, 1] or similar - we need data_range. We'll use actual min/max of img2.
    data_range = i2.max() - i2.min()
    if data_range == 0:
        data_range = 1.0
    return psnr_metric(i1, i2, data_range=data_range)

def calculate_ssim(img1, img2):
    i1 = img1.squeeze().detach().cpu().numpy()
    i2 = img2.squeeze().detach().cpu().numpy()
    data_range = i2.max() - i2.min()
    if data_range == 0:
        data_range = 1.0
    return ssim_metric(i1, i2, data_range=data_range)

def generate_comparison_plot(img1, img2, filepath):
    i1 = img1.squeeze().detach().cpu().numpy()
    i2 = img2.squeeze().detach().cpu().numpy()
    diff = np.abs(i1 - i2)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(i1, cmap='gray')
    axes[0].set_title('Prediction')
    axes[1].imshow(i2, cmap='gray')
    axes[1].set_title('Ground Truth')
    im3 = axes[2].imshow(diff, cmap='hot')
    axes[2].set_title('Absolute Difference')
    plt.colorbar(im3, ax=axes[2])
    
    plt.savefig(filepath)
    plt.close()

def evaluate_predictions(preds, targets, output_dir="reports"):
    logger.info("Evaluating predictions against ground truth...")
    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    # Assumes preds and targets are shape (B, C, H, W)
    batch_size = preds.shape[0]
    for b in range(batch_size):
        p = preds[b]
        t = targets[b]
        
        psnr_val = calculate_psnr(p, t)
        mse_val = calculate_mse(p, t)
        ssim_val = calculate_ssim(p, t)
        
        results.append({"Batch_Idx": b, "PSNR": psnr_val, "MSE": mse_val, "SSIM": ssim_val})
        generate_comparison_plot(p, t, os.path.join(output_dir, f"comparison_{b}.png"))
        
    df = pd.DataFrame(results)
    csv_path = os.path.join(output_dir, "evaluation_metrics.csv")
    df.to_csv(csv_path, index=False)
    
    logger.info(f"Evaluation completed. Report saved to {csv_path}")
    logger.info(f"Mean PSNR: {df['PSNR'].mean():.2f}, Mean SSIM: {df['SSIM'].mean():.4f}")
    return df.mean().to_dict()

if __name__ == "__main__":
    # Smoke test
    p = torch.rand(2, 1, 256, 256)
    t = torch.rand(2, 1, 256, 256)
    evaluate_predictions(p, t)
