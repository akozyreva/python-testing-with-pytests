import pytest
import tasks
from tasks import Task


def something_plugin():
    return None


def something_plugin2():
    return None


def pytest_configure():
    pytest.task_id = something_plugin()


@pytest.fixture()
def init_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield   # this is where testing happens
    # Teardown: stop db
    tasks.stop_tasks_db()