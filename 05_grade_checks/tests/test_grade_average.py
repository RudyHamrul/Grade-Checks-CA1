import pytest
from grade_average import calculate_average

def test_a01():
    """Both zero marks return 0."""
    assert calculate_average(0, 0) == 0

def test_a02():
    """Both maximum marks return 100."""
    assert calculate_average(100, 100) == 100

def test_a03():
    """Even sum returns whole-number average."""
    assert calculate_average(40, 60) == 50

def test_a04():
    """Odd sum retains fractional average."""
    assert calculate_average(50, 51) == 50.5

def test_a05():
    """Odd sum near minimum retains fractional average."""
    assert calculate_average(0, 1) == 0.5

def test_a06():
    """Reversed marks produce same average."""
    assert calculate_average(80, 20) == 50

def test_a07():
    """Negative first mark raises ValueError."""
    with pytest.raises(ValueError):
        calculate_average(-1, 50)

def test_a08():
    """First mark above 100 raises ValueError."""
    with pytest.raises(ValueError):
        calculate_average(101, 50)

def test_a09():
    """Negative second mark raises ValueError."""
    with pytest.raises(ValueError):
        calculate_average(50, -1)

def test_a10():
    """Second mark above 100 raises ValueError."""
    with pytest.raises(ValueError):
        calculate_average(50, 101)

def test_a11():
    """String first mark raises TypeError."""
    with pytest.raises(TypeError):
        calculate_average('50', 50)

def test_a12():
    """Float second mark raises TypeError."""
    with pytest.raises(TypeError):
        calculate_average(50, 50.0)

def test_a13():
    """Boolean first mark raises TypeError."""
    with pytest.raises(TypeError):
        calculate_average(True, 50)

def test_a14():
    """None second mark raises TypeError."""
    with pytest.raises(TypeError):
        calculate_average(50, None)
