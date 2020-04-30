import pytest
import tasks
from tasks import Task


def something_plugin():
    return None


def something_plugin2():
    return None


def pytest_configure():
    pytest.task_id = something_plugin()


@pytest.fixture(scope='session', params=['tiny', 'mongo'])
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield   # this is where testing happens
    # Teardown: stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def init_tasks_db(tasks_db_session):
    """ An empty tasks db. """
    tasks.delete_all()


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by db
@pytest.fixture(scope='session')
def tasks_just_a_few():
    """ All summaries and owners are unique. """
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """ Several owners with several tasks each. """
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Cook a lunch', 'Michelle'),
        
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(init_tasks_db, tasks_just_a_few):
    """ Connected db with 3 tasks. all unique. """
    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_multi_per_owner(init_tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for task in tasks_mult_per_owner:
        tasks.add(task)