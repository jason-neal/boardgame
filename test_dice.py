from dice import Dice
import pytest

@pytest.fixture
def dice():
   """Return a dice object"""
   return Dice()

def test_Dice_type():
    d = Dice()
    assert isinstance(d, Dice)
   

@pytest.mark.parametrize("s", [2,3,4,5,6,7,8,9,20, 50])
def test_dice_sides(s):
    d = Dice(sides=s)
    assert d.sides == s


def test_dice_roll(dice):
    result = dice.roll()
    assert result <= dice.sides
    assert result >= 1

@pytest.mark.parametrize("n", [1,2,3,4,5,6,500])
def test_dice_rolln(dice, n):
    """Test rolling many dice.""" 
    rolls = dice.rolln(n)
    assert len(rolls) == n
    assert isinstance(rolls, list)
    assert isinstance(rolls[0], int)
    # Sum between n and s*n
    assert sum(rolls) <= n * dice.sides 
    assert sum(rolls) >= n * 1

