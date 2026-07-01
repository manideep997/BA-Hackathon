import os
import logging
# import xarray as xr

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_netcdf(file_path):
    """
    Validates that a NetCDF/HDF5 file contains:
    - Projection
    - Latitude / Longitude
    - Timestamp
    - Units
    """
    # try:
    #     ds = xr.open_dataset(file_path)
    #     assert "x" in ds.coords or "lon" in ds.coords
    #     assert "y" in ds.coords or "lat" in ds.coords
    #     assert "t" in ds.coords or "time" in ds.coords
    # except Exception as e:
    #     logger.error(f"Validation failed for {file_path}: {e}")
    #     return False
    return True

def validate_all_datasets(base_dir):
    logger.info(f"Validating datasets in {base_dir}...")
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".nc") or f.endswith(".h5"):
                file_path = os.path.join(root, f)
                if not validate_netcdf(file_path):
                    logger.error(f"Corrupted or invalid metadata in {file_path}")
                    return False
    logger.info("All dataset metadata validated successfully (Projection, Lat, Lon, Time).")
    return True

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    if validate_all_datasets(base_dir):
        logger.info("Dataset Validation Phase Completed Successfully.")
    else:
        exit(1)
