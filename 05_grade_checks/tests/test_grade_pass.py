import pytest
from grade_pass import has_passed

def test_p01():
    """Zero score returns False."""
    assert has_passed(0) == False

def test_p02():
    """Score below boundary returns False."""
    assert has_passed(49) == False

def test_p03():
    """Boundary score 50 returns True."""
    assert has_passed(50) == True

def test_p04():
    """Score above boundary returns True."""
    assert has_passed(51) == True

def test_p05():
    """Maximum score returns True."""
    assert has_passed(100) == True

def test_p06():
    """Negative score raises ValueError."""
    with pytest.raises(ValueError):
        has_passed(-1)

def test_p07():
    """Score above 100 raises ValueError."""
    with pytest.raises(ValueError):
        has_passed(101)

def test_p08():
    """String score raises TypeError."""
    with pytest.raises(TypeError):
        has_passed('50')

def test_p09():
    """Float score raises TypeError."""
    with pytest.raises(TypeError):
        has_passed(50.0)

def test_p10():
    """Boolean score raises TypeError."""
    with pytest.raises(TypeError):
        has_passed(True)

def test_p11():
    """Missing score raises TypeError."""
    with pytest.raises(TypeError):
        has_passed(None)
