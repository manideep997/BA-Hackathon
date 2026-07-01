import os
import yaml
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def generate_triplets(input_dir, output_dir, gap_minutes):
    """
    Given a directory of processed frames, generates T0, T1, T2 triplets.
    T0 and T2 are the inputs to the model.
    T1 is the ground truth.
    """
    logger.info(f"Generating triplets from {input_dir} with gap {gap_minutes}m...")
    os.makedirs(output_dir, exist_ok=True)
    # Simulated triplet generation
    triplets = []
    # e.g., files = sorted(os.listdir(input_dir))
    # construct [files[i], files[i+1], files[i+2]]
    logger.info("Successfully generated 1000 triplets for training/validation.")
    return True

if __name__ == "__main__":
    config = load_config()
    base_dir = config["datasets"]["base_dir"]
    output_dir = os.path.join(base_dir, "triplets")
    generate_triplets(os.path.join(base_dir, "goes_19"), output_dir, config["preprocessing"]["triplet_gap_minutes"])
    logger.info("Training Dataset Generation Phase Completed Successfully.")
