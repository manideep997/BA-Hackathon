import os
import sys
import tempfile
import numpy as np
import xarray as xr
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from scripts.validate_datasets import validate_netcdf

def create_mock_netcdf(filepath, valid=True):
    """Creates a small dummy NetCDF file for testing."""
    if valid:
        # Create valid geospatial metadata
        ds = xr.Dataset(
            {
                "Rad": (("y", "x"), np.random.rand(10, 10))
            },
            coords={
                "x": np.arange(10),
                "y": np.arange(10),
                "t": np.array(["2024-01-01T00:00:00"], dtype="datetime64[ns]")
            }
        )
    else:
        # Create invalid (missing geospatial coords)
        ds = xr.Dataset(
            {
                "Rad": (("a", "b"), np.random.rand(10, 10))
            },
            coords={
                "a": np.arange(10),
                "b": np.arange(10)
            }
        )
    ds.to_netcdf(filepath, engine="netcdf4")
    return filepath

def test_validate_netcdf_valid():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "valid.nc")
        create_mock_netcdf(filepath, valid=True)
        assert validate_netcdf(filepath) == True, "Validation failed on valid NetCDF"

def test_validate_netcdf_invalid():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "invalid.nc")
        create_mock_netcdf(filepath, valid=False)
        assert validate_netcdf(filepath) == False, "Validation passed on invalid NetCDF"
