import pytest
from player import Player, Card
from player import PaymentError


def test_player_instance():
    p = Player()
    assert isinstance(p, Player)
    assert p.score == 0
    assert not Player() is Player()  # Players are different!
    assert p.cubes == 0
    assert len(p.hand) == 0
    assert isinstance(p.hand, list) 


@pytest.mark.parametrize("name", ["Jessica", "Jason","Timothy", None])
def test_player_name(name):
    p = Player(name)
    assert p.name == name


@pytest.mark.parametrize("badname", [dict(), list(), tuple(), 7, 1.0, True])  
def test_player_name_is_str(badname):
    with pytest.raises(TypeError):
        Player(name=badname)


from deck import Card
@pytest.fixture()
def player():
    p = Player("Fixed player")
    p.score = 10
    p.cubes = 4
    p.hand = [Card(), Card(), Card()]
    return p

@pytest.mark.parametrize("points", [1, 2, 3, 100])    
def test_add_score(player, points):
    """Addition of score."""
    org_score = player.score
    player.add_score(points)
    assert org_score + points == player.score


@pytest.mark.parametrize("num", [-1, -5])
def test_points_and_cubes_positive(num):
    """Points and cubes must be positive."""
    with pytest.raises(ValueError):
        Player().add_score(num)

    with pytest.raises(ValueError):
        Player().pickup_cubes(num)

    with pytest.raises(ValueError):
        Player().pay_cubes(num)


@pytest.mark.parametrize("num", ["0", "2", 0.1, -1.0, dict(), list()])
def test_points_and_cubes_correct_type(num):
    """Points and cubes must be positive."""
    with pytest.raises(TypeError):
        Player().add_score(num)

    with pytest.raises(TypeError):
        Player().pickup_cubes(num)

    with pytest.raises(TypeError):
        Player().pay_cubes(num)


@pytest.mark.parametrize("cubes", [1, 2, 3])
def test_pickup_cubes_addition(player, cubes):
    """Addition of cubes."""
    org_cubes = player.cubes
    player.pickup_cubes(cubes)
    assert org_cubes + cubes == player.cubes


@pytest.mark.parametrize("cubes", [1, 2, 3, 4])
def test_pay_cubes(player, cubes):
    """Decrease number of cubes."""
    org_cubes = player.cubes
    player.pay_cubes(cubes)
    assert org_cubes - cubes == player.cubes


@pytest.mark.parametrize("cubes", [1, 2, 10])
def test_pay_cubes_more_than_have(player, cubes):
    """Decrease number of cubes."""
    print(player.cubes)
    player.pay_cubes(player.cubes) # Pay all cubes 
    assert player.cubes == 0
    with pytest.raises(PaymentError):
        player.pay_cubes(cubes)

