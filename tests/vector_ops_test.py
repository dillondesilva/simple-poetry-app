from app import __version__
from app import Vector3
from app import VectorOperations

# Testing that two vectors are added correctly
def test_vector_addition():
    # Testing with two vectors that have positive int component values
    a = Vector3(3, 4, 5)
    b = Vector3(6, 8, 10)

    resultantVector = VectorOperations.addVectors(a, b)

    # Testing vector components are correct values
    assert resultantVector.x == 9;
    assert resultantVector.y == 12;
    assert resultantVector.z == 15;

# Testing that two vectors are subtracted correctly
def test_vector_subtraction():
    # Testing with two vectors that have positive int component values
    a = Vector3(3, 4, 5)
    b = Vector3(6, 8, 10)

    resultantVector = VectorOperations.subtractVectors(a, b)

    # Testing vector components are correct values
    assert resultantVector.x == -3;
    assert resultantVector.y == -4;
    assert resultantVector.z == -5;