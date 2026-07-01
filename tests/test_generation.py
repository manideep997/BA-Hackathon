import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from preprocessing.generate_triplets import generate_triplets

def test_generate_triplets():
    # Mock input and output dirs
    assert generate_triplets("fake_in", "fake_out", 10) == True
