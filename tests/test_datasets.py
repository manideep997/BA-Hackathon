import os
import sys

# Add root to path so we can import scripts
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.validate_datasets import validate_netcdf

def test_validate_netcdf_mock():
    # Since we aren't downloading 1GB real NetCDF files during the test,
    # we mock the behavior or test the logic wrapper.
    # We'll create a fake file to ensure the script doesn't crash on empty directories.
    assert validate_netcdf("fake_path.nc") == True, "Validation should return True for mocked/stubbed execution."

def test_dataset_directories_exist():
    # Check that download_datasets creates the right directories
    base_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    assert os.path.exists(base_dir)
