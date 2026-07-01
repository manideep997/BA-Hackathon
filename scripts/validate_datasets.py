import os
import logging
import xarray as xr

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_netcdf(file_path):
    """
    Validates that a NetCDF/HDF5 file contains required geospatial and temporal metadata.
    """
    try:
        ds = xr.open_dataset(file_path, engine="netcdf4")
        
        # Check coordinates (latitude/longitude or projection coordinates x/y)
        coords = ds.coords
        has_geo = ('x' in coords and 'y' in coords) or ('lat' in coords and 'lon' in coords) or ('latitude' in coords and 'longitude' in coords)
        
        if not has_geo:
            logger.error(f"Validation failed for {file_path}: Missing geospatial coordinates (x/y or lat/lon).")
            return False
            
        # Check time variable
        if 't' not in coords and 'time' not in coords:
            logger.warning(f"Validation warning for {file_path}: Missing explicit time coordinate. It might be stored as an attribute.")
            
        ds.close()
        return True
    except Exception as e:
        logger.error(f"Validation failed for {file_path}: {e}")
        return False

def validate_all_datasets(base_dir):
    logger.info(f"Validating datasets in {base_dir}...")
    found_files = False
    valid = True
    
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".nc") or f.endswith(".h5"):
                found_files = True
                file_path = os.path.join(root, f)
                if not validate_netcdf(file_path):
                    logger.error(f"Corrupted or invalid metadata in {file_path}")
                    valid = False
                    
    if not found_files:
        logger.warning(f"No NetCDF (.nc) or HDF5 (.h5) files found in {base_dir} to validate.")
        
    if valid:
        logger.info("All dataset metadata validated successfully.")
    return valid

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    if validate_all_datasets(base_dir):
        logger.info("Dataset Validation Phase Completed Successfully.")
    else:
        exit(1)
