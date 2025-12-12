import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add, sub, mult, div,
    square, sqrt, log,
    sin, cos, percentage
)

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 3) == 7

def test_mult():
    assert mult(4, 5) == 20

def test_div():
    assert div(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)


# Square
def test_square_positive():
    assert square(4) == 16

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-3) == 9


# Square Root
def test_sqrt_perfect_square():
    assert sqrt(16) == pytest.approx(4)

def test_sqrt_zero():
    assert sqrt(0) == 0

def test_sqrt_non_perfect_square():
    assert sqrt(2) == pytest.approx(1.41421356, rel=1e-6)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)


# Logarithm
def test_log_one():
    assert log(1) == pytest.approx(0)

def test_log_two():
    assert log(2) == pytest.approx(0.693147, rel=1e-6)

def test_log_invalid_zero():
    with pytest.raises(ValueError):
        log(0)

def test_log_invalid_negative():
    with pytest.raises(ValueError):
        log(-5)


# Trigonometry
def test_sin_zero():
    assert sin(0) == pytest.approx(0)

def test_sin_30_degrees():
    assert sin(30) == pytest.approx(0.5, rel=1e-6)

def test_sin_radians():
    assert sin(3.141592653589793 / 2, degrees=False) == pytest.approx(1, rel=1e-6)

def test_cos_zero():
    assert cos(0) == pytest.approx(1)

def test_cos_60_degrees():
    assert cos(60) == pytest.approx(0.5, rel=1e-6)

def test_cos_radians():
    assert cos(3.141592653589793, degrees=False) == pytest.approx(-1, rel=1e-6)


# Percentage
def test_percentage_normal():
    assert percentage(25, 200) == 12.5

def test_percentage_zero_numerator():
    assert percentage(0, 100) == 0

def test_percentage_denominator_zero():
    with pytest.raises(ValueError):
        percentage(10, 0)