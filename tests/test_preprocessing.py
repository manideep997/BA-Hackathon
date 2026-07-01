import os
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from preprocessing.process_nc import normalize_radiances

def test_normalization():
    data = np.array([0, 50, 100])
    norm_range = [-1.0, 1.0]
    result = normalize_radiances(data, norm_range)
    assert np.isclose(result.min(), -1.0)
    assert np.isclose(result.max(), 1.0)
    assert np.isclose(result[1], 0.0)
