from app import __version__
from app import Vector3
from app import VectorOperations

import math

def test_version():
    assert __version__ == '0.1.0'

# Testing that a vector is created with the correct properties
def test_vector_creation():
    a = Vector3(3, 4, 5)

    # Testing vector components are correct values
    assert a.x == 3;
    assert a.y == 4;
    assert a.z == 5;

    # Testing that magnitude is correct
    assert a.magnitude == math.sqrt(50)