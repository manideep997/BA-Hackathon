import os
import yaml
import logging
import xarray as xr
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def extract_timestamp(filepath):
    try:
        ds = xr.open_dataset(filepath, engine="netcdf4")
        if 't' in ds.coords:
            val = ds['t'].values
        elif 'time' in ds.coords:
            val = ds['time'].values
        else:
            ds.close()
            return None
        
        # Ensure scalar
        if val.ndim > 0:
            val = val[0]
            
        timestamp = pd.to_datetime(val)
        ds.close()
        return timestamp
    except Exception as e:
        logger.error(f"Failed to extract timestamp from {filepath}: {e}")
        return None

def generate_triplets(input_dir, output_dir, gap_minutes):
    """
    Given a directory of processed frames, generates strictly temporally aligned T0, T1, T2 triplets.
    """
    logger.info(f"Generating triplets from {input_dir} with gap {gap_minutes}m...")
    os.makedirs(output_dir, exist_ok=True)
    
    files = [f for f in os.listdir(input_dir) if f.endswith(".nc") or f.endswith(".h5")]
    file_times = []
    
    for f in files:
        filepath = os.path.join(input_dir, f)
        ts = extract_timestamp(filepath)
        if ts is not None:
            file_times.append((filepath, ts))
            
    # Sort chronologically
    file_times.sort(key=lambda x: x[1])
    
    valid_triplets = []
    gap = pd.Timedelta(minutes=gap_minutes)
    margin = pd.Timedelta(minutes=1) # 1 minute tolerance
    
    for i in range(len(file_times) - 2):
        f0, t0 = file_times[i]
        f1, t1 = file_times[i+1]
        f2, t2 = file_times[i+2]
        
        # Verify temporal equidistant constraints
        delta_01 = abs((t1 - t0) - gap)
        delta_12 = abs((t2 - t1) - gap)
        
        if delta_01 <= margin and delta_12 <= margin:
            valid_triplets.append((f0, f1, f2))
            
    logger.info(f"Successfully generated {len(valid_triplets)} valid triplets.")
    
    # In a real environment, we would save a manifest file or symlinks
    if valid_triplets:
        manifest_path = os.path.join(output_dir, "triplets_manifest.txt")
        with open(manifest_path, "w") as f:
            for t in valid_triplets:
                f.write(f"{t[0]},{t[1]},{t[2]}\n")
        logger.info(f"Saved manifest to {manifest_path}")
        return True
    return False

if __name__ == "__main__":
    config = load_config()
    base_dir = config["datasets"]["base_dir"]
    output_dir = os.path.join(base_dir, "triplets")
    generate_triplets(os.path.join(base_dir, "goes_19"), output_dir, config["preprocessing"]["triplet_gap_minutes"])
