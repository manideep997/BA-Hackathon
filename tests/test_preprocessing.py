import os
import sys
import numpy as np
import pytest
import xarray as xr
import tempfile

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from preprocessing.process_nc import normalize_radiances, process_file

def test_normalization():
    data = np.array([0, 50, 100])
    norm_range = [-1.0, 1.0]
    result = normalize_radiances(data, norm_range)
    assert np.isclose(result.min(), -1.0)
    assert np.isclose(result.max(), 1.0)
    assert np.isclose(result[1], 0.0)

def test_process_file_valid():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "valid.nc")
        
        # Create a valid dataset with 'Rad' variable
        ds = xr.Dataset(
            {
                "Rad": (("y", "x"), np.random.rand(64, 64) * 100)
            },
            coords={
                "x": np.arange(64),
                "y": np.arange(64)
            }
        )
        ds.to_netcdf(filepath, engine="netcdf4")
        
        config = {
            "preprocessing": {
                "normalization_range": [-1.0, 1.0],
                "output_resolution": [32, 32]
            }
        }
        
        result = process_file(filepath, config)
        assert result is not None
        assert result.shape == (32, 32)
        assert result.min() >= -1.0
        assert result.max() <= 1.0
