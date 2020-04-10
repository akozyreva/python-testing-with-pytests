import pytest 
import tasks
from tasks import Task


@pytest.mark.smoke
def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")

@pytest.mark.get
@pytest.mark.smoke
def test_start_tasks_db_raises():
    """ Make sure unsupproted db raises an exception. """
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


def test_add_task_with_id():
    """ try to add task with id already set. - raise an exception """
    with pytest.raises(ValueError):
        tasks.add(Task('run', 'brian', True, '12345'))


def test_add_task_with_not_string_summary():
    """ try to add task with summary != string"""
    with pytest.raises(ValueError):
        tasks.add(Task(summary=12345))


def test_add_task_owner_raises():
    """ try to add task with owner != string"""
    with pytest.raises(ValueError) as excinfo:
        tasks.add(Task(summary='run', owner=12345))
    exception_msg = excinfo.value.args[0]
    assert exception_msg == 'task.owner must be string or None)'