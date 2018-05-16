from dice import Dice
import pytest

@pytest.fixture(params=[2, 4, 6, 24])
def dice(request):
   """Return a dice object"""
   return Dice(sides=request.param)

def test_Dice_type():
    d = Dice()
    assert isinstance(d, Dice)
   

@pytest.mark.parametrize("s", [2,3,4,5,6,7,8,9,20, 50])
def test_dice_sides(s):
    d = Dice(sides=s)
    assert d.sides == s


@pytest.mark.parametrize("s", [0.5, 2.0, "6", "7.0", None])
def test_dice_with_noninteger_sides(s):
    """Should raise TypeError when side is non-integer."""
    with pytest.raises(TypeError):
        Dice(sides=s)


@pytest.mark.parametrize("s", [True, False, -1, -5, 1, 0])
def test_dice_with_small_sides(s):
    """Should raise ValueError when side is less than 2."""
    with pytest.raises(ValueError):
        Dice(sides=s)


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

