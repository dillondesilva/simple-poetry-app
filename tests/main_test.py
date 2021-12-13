from app import __version__
from app import Vector2

def test_version():
    assert __version__ == '0.1.0'

def test_vector_creation():
    a = Vector2(3, 5, 10)
    assert a.x == 3