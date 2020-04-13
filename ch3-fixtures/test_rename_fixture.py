""" Demonstrate fixture renaming. """
import pytest


@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    """ Return ultimate answer """
    return 42


def test_everyth(lue):
    """Use the shorter name."""
    assert lue == 42
