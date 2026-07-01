import os
import sys
import numpy as np
import pytest
import xarray as xr
import tempfile
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from preprocessing.generate_triplets import extract_timestamp, generate_triplets

def create_mock_nc_with_time(filepath, timestamp_str):
    ds = xr.Dataset(
        {"Rad": (("y", "x"), np.random.rand(10, 10))},
        coords={
            "x": np.arange(10),
            "y": np.arange(10),
            "t": np.array([timestamp_str], dtype="datetime64[ns]")
        }
    )
    ds.to_netcdf(filepath, engine="netcdf4")

def test_extract_timestamp():
    with tempfile.TemporaryDirectory() as tmpdir:
        fp = os.path.join(tmpdir, "test.nc")
        create_mock_nc_with_time(fp, "2024-01-01T12:00:00")
        ts = extract_timestamp(fp)
        assert ts == pd.to_datetime("2024-01-01T12:00:00")

def test_generate_triplets():
    with tempfile.TemporaryDirectory() as tmpdir:
        in_dir = os.path.join(tmpdir, "input")
        out_dir = os.path.join(tmpdir, "output")
        os.makedirs(in_dir)
        
        # Create 3 files with exactly 10 min gaps
        create_mock_nc_with_time(os.path.join(in_dir, "f1.nc"), "2024-01-01T12:00:00")
        create_mock_nc_with_time(os.path.join(in_dir, "f2.nc"), "2024-01-01T12:10:00")
        create_mock_nc_with_time(os.path.join(in_dir, "f3.nc"), "2024-01-01T12:20:00")
        
        # Create 1 file with bad gap (should be ignored)
        create_mock_nc_with_time(os.path.join(in_dir, "f4.nc"), "2024-01-01T13:00:00")
        
        result = generate_triplets(in_dir, out_dir, 10)
        assert result == True
        assert os.path.exists(os.path.join(out_dir, "triplets_manifest.txt"))
