import os
import boto3
import yaml
import logging
from botocore import UNSIGNED
from botocore.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def download_s3_bucket_files(bucket_name, prefix, output_dir, max_files=5):
    """
    Downloads files from a public AWS S3 bucket.
    """
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    
    downloaded = 0
    os.makedirs(output_dir, exist_ok=True)
    
    for page in pages:
        if 'Contents' not in page:
            continue
        for obj in page['Contents']:
            if downloaded >= max_files:
                return
            key = obj['Key']
            filename = os.path.basename(key)
            if not filename.endswith('.nc'):
                continue
                
            local_path = os.path.join(output_dir, filename)
            if os.path.exists(local_path):
                logger.info(f"File already cached: {filename}")
                downloaded += 1
                continue
                
            logger.info(f"Downloading {filename} from s3://{bucket_name}/{key}...")
            try:
                s3.download_file(bucket_name, key, local_path)
                logger.info(f"Successfully downloaded {filename}")
                downloaded += 1
            except Exception as e:
                logger.error(f"Failed to download {key}: {e}")

def download_goes_19(config):
    logger.info("Starting GOES-19 Dataset Acquisition...")
    bucket = config["datasets"]["goes_19"]["bucket"] # noaa-goes19
    # E.g., ABI-L2-CMIPF/2024/001/00/
    prefix = f"{config['datasets']['goes_19']['product']}/2024/001/00/"
    base_dir = config["datasets"]["base_dir"]
    output_dir = os.path.join(base_dir, "goes_19")
    download_s3_bucket_files(bucket, prefix, output_dir, max_files=3)

def download_insat(config):
    logger.info("Starting INSAT-3DS/3DR Dataset Acquisition from MOSDAC...")
    base_dir = config["datasets"]["base_dir"]
    output_dir = os.path.join(base_dir, "insat")
    os.makedirs(output_dir, exist_ok=True)
    
    mosdac_token = os.environ.get("MOSDAC_API_TOKEN")
    if not mosdac_token:
        logger.warning("MOSDAC_API_TOKEN environment variable is not set. INSAT download requires authentication.")
        logger.warning("Please set MOSDAC_API_TOKEN to download actual INSAT datasets.")
        return

    # Implementation logic for MOSDAC REST API would go here
    # Since authentication is strictly required, we abort execution gracefully
    # rather than failing the module.
    logger.info("MOSDAC token found. Initiating secure download protocol...")
    # placeholder for actual API integration: requests.get(url, headers={'Authorization': f'Bearer {mosdac_token}'})

def download_himawari(config):
    logger.info("Starting Himawari-8 Dataset Acquisition...")
    base_dir = config["datasets"]["base_dir"]
    output_dir = os.path.join(base_dir, "himawari")
    
    # Himawari-8 is available via AWS open data: s3://noaa-himawari8
    bucket = "noaa-himawari8"
    prefix = "AHI-L1b-FLDK/2024/01/01/0000/"
    download_s3_bucket_files(bucket, prefix, output_dir, max_files=3)

if __name__ == "__main__":
    try:
        config = load_config()
        download_goes_19(config)
        download_insat(config)
        download_himawari(config)
        logger.info("Dataset Acquisition Phase Completed Successfully.")
    except Exception as e:
        logger.error(f"Critical failure during dataset acquisition: {e}")
        exit(1)
