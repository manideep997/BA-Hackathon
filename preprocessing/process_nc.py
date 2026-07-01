import os
import yaml
import logging
import xarray as xr
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def normalize_radiances(data, norm_range):
    """
    Normalizes array to a specified range (e.g. [-1, 1]).
    """
    min_val, max_val = data.min(), data.max()
    if max_val - min_val == 0:
        return data
    normalized = (data - min_val) / (max_val - min_val)
    return normalized * (norm_range[1] - norm_range[0]) + norm_range[0]

def process_file(file_path, config):
    logger.info(f"Processing {file_path}...")
    norm_range = config["preprocessing"]["normalization_range"]
    output_res = config["preprocessing"].get("output_resolution", [512, 512])
    
    try:
        ds = xr.open_dataset(file_path, engine="netcdf4")
        
        # Determine the primary data variable. For GOES it might be 'Rad' or 'CMI'
        data_var = None
        for var in ['Rad', 'CMI', 'data', 'Rad_TIR1']:
            if var in ds.data_vars:
                data_var = var
                break
                
        if not data_var:
            logger.error(f"Could not find a valid radiance/data variable in {file_path}")
            return None
            
        data = ds[data_var].values
        
        # Spatial Resampling if configured
        # Note: robust interpolation (e.g., scipy.interpolate or OpenCV) is used for changing spatial dimensions.
        if data.shape != tuple(output_res):
            logger.warning(f"Data shape {data.shape} does not match config {output_res}. Resampling...")
            import cv2
            # Replace NaNs or fill values before resizing
            data = np.nan_to_num(data)
            data = cv2.resize(data, (output_res[1], output_res[0]), interpolation=cv2.INTER_LINEAR)
            
        normalized = normalize_radiances(data, norm_range)
        
        logger.info(f"Successfully processed {file_path} to shape {normalized.shape}.")
        ds.close()
        return normalized
    except Exception as e:
        logger.error(f"Failed to process {file_path}: {e}")
        return None

def process_all_datasets(base_dir, config):
    logger.info(f"Starting bulk processing of datasets in {base_dir}...")
    processed_count = 0
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".nc") or f.endswith(".h5"):
                file_path = os.path.join(root, f)
                result = process_file(file_path, config)
                if result is not None:
                    processed_count += 1
    logger.info(f"Processed {processed_count} files.")
    return processed_count > 0

if __name__ == "__main__":
    config = load_config()
    base_dir = config["datasets"]["base_dir"]
    logger.info("Data Preprocessing Module Initialized.")
    if process_all_datasets(base_dir, config):
        logger.info("Data Preprocessing Completed Successfully.")
    else:
        logger.warning("No files were successfully processed. Check datasets directory.")
