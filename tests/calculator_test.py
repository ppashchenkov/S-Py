import pytest
from product.calculator import Calculator


calc = Calculator()

@pytest.mark.parametrize(
    "a_, b_, expected_",
    [
        (5, 7, 12),
        (0, -7, -7),
        (-10, 7, -3),
        (99, -9, 90)
    ])
def test_sum(a_, b_, expected_):
    assert calc.sum(a_, b_) == expected_

@pytest.mark.parametrize(
    "a_, b_, expected_",
    [
        (5, 7, -2),
        (0, -7, 7),
        (-10, 7, -17),
        (99, -9, 108)
    ])
def test_sub(a_, b_, expected_):
    assert calc.sub(a_, b_) == expected_

@pytest.mark.parametrize(
    "a_, b_, expected_",
    [
        (5, 7, 35),
        (0, -7, 0),
        (-10, 7, -70),
        (99, -9, -891)
    ])
def test_mult(a_, b_, expected_):
    assert calc.mult(a_, b_) == expected_

@pytest.mark.parametrize(
    "a_, b_, expected_",
    [
        (5, 2, 25),
        (5, 3, 125),
        (-10, 0, 1),
        (2, -1, 0.5),
        (4, -2, 0.0625)
    ])
def test_power(a_, b_, expected_):
    assert calc.power(a_, b_) == expected_

@pytest.mark.parametrize(
    "a_, b_, expected_",
    [
        (14, 7, 2),
        (0, -7, 0),
        (-7, 7, -1),
        (99, -9, -11)
    ])
def test_div(a_, b_, expected_):
    assert calc.div(a_, b_) == expected_

@pytest.mark.xfail(raises=ArithmeticError)
def test_div_on_zero():
    assert calc.div(5, 0) == 5

@pytest.mark.parametrize(
    "nums_, expected_",
    [
        ([], 0),
        ([2,2,3,5], 3),
        ([0, 8], 4),
        ([5], 5)
    ])
def test_avr(nums_, expected_):
    assert calc.avr(nums_) == expected_

@pytest.mark.xfail(raises=Exception)
def test_avr_nums_strings():
    assert calc.avr(['w']) == 1
