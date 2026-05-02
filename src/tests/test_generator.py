import pytest
from ..src.generator import generate_password


def test_zero_chars_error():
    with pytest.raises(ValueError):
        generate_password(12, False, False, False)

def test_length_error():
    with pytest.raises(VelueError):
        generate_password(0)
    with pytest.raises(VelueError):
        generate_password(2)
