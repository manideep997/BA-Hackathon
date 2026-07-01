import sys

def test_python_version():
    assert sys.version_info >= (3, 10), "Python version must be 3.10 or higher"

def test_imports():
    try:
        import torch
        import xarray
        import netCDF4
        import h5py
        import fastapi
        import uvicorn
        import boto3
        import s3fs
        import yaml
    except ImportError as e:
        assert False, f"Failed to import required package: {e}"

def test_yaml_config():
    import yaml
    import os
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    assert os.path.exists(config_path), "default.yaml configuration file is missing"
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    assert config["project"]["name"] == "Fill in the Frames Seamlessly"
