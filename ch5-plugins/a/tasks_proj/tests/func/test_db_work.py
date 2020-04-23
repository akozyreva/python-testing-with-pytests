import pytest
import tasks
from tasks import Task


def test_db_eror_if_not_init():
    """ Check, that without initialization, method returns an error """
    with pytest.raises(Exception):
        tasks.count()


# it's better to write a fixture, and put test_db_eror_if_not_init
#  in test_api_exception,
# but I prefer to put all stuff in one file for learning
def test_db_has_no_signs_by_default():
    """Check, that after initialization db has 0 signes"""
    tasks.start_tasks_db(str("."), 'tiny')
    tasks.delete_all()
    cur_count = tasks.count()
    assert cur_count == 0
    tasks.stop_tasks_db()


def test_after_task_creation_db_count_changes():
    """ Check, that after task creation count chages """
    tasks.start_tasks_db(str("."), 'tiny')
    before_creation_count = tasks.count()
    task = Task('breathe', 'Brian', True)
    pytest.task_id = tasks.add(task)
    actual_count = tasks.count() 
    assert before_creation_count + 1 == actual_count
    tasks.stop_tasks_db()


def test_after_update_db_count_not_change():
    """ Check, that after update count doesn't change """
    tasks.start_tasks_db(str("."), 'tiny')
    before_update_count = tasks.count()
    tasks.update(pytest.task_id, Task(done=True))
    after_update_count = tasks.count()
    assert before_update_count == after_update_count
    tasks.stop_tasks_db()


def test_after_deletion_db_count_changes():
    """ Check, that after deletion count changes """
    tasks.start_tasks_db(str("."), 'tiny')
    before_deletion_count = tasks.count()
    tasks.delete(pytest.task_id)
    after_deletion_count = tasks.count()
    assert before_deletion_count - 1 == after_deletion_count
    tasks.stop_tasks_db()