import pytest


@pytest.fixture()
def a_tuple():
    """ Return somth more interesting. """
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    """ Demo the a_tuple fixture. """
    assert a_tuple[3]['bar'] == 32

# error directly in the fixture
@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42

def test_other_data(some_other_data):
    pass