import pytest
from libello.dice import *

def test_coin():
    assert 1 <= coin() <= 2

def test_d4():
    assert 1 <= d4() <= 4

def test_d6():
    assert 1 <= d6() <= 6

def test_d8():
    assert 1 <= d8() <= 8

def test_d10():
    assert 1 <= d10() <= 10

def test_d12():
    assert 1 <= d12() <= 12

def test_d20():
    assert 1 <= d20() <= 20

def test_adv():
    assert 1 <= adv() <= 20

def test_disadv():
    assert 1 <= disadv() <= 20

def test_d100():
    assert 1 <= d100() <= 100

def test_twod6():
    assert 2 <= twod6() <= 12

def test_threed6():
    assert 3 <= threed6() <= 18

@pytest.mark.parametrize('test_input,lower_bound,upper_bound', [(4, 4, 24), (5, 5, 30), (6, 6, 36)])
def test_xd6(test_input, lower_bound, upper_bound):
    assert lower_bound <= xd6(test_input) <= upper_bound