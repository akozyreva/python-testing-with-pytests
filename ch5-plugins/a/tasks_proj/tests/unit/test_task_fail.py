""" Use the Task type to show test failures."""
from tasks import Task


def test_task_equality():
    """Different tasks shouldn't be equl. """
    t1 = Task('sit there', 'brian')
    t2 = Task('do something', 'okken')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts shouldn't be equal. """
    t1_dict = Task("make_sandwich", "okken")._asdict()
    t2_dict = Task("make_sandwich", "okkem")._asdict()
    assert t1_dict == t2_dict