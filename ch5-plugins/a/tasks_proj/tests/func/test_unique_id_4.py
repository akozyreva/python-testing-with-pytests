import pytest
import tasks


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield   # this is where testing happens
    # Teardown: stop db
    tasks.stop_tasks_db

@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                    reason="supported from 0.2.0 version")
def test_unique_id():
    """Calling unique_id() twice should return different numbers. """
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_is_not_a_duck():
    """Demonstrate xpass.
    Expected to fail, but passed
    """
    uid = tasks.unique_id()
    assert uid != 'a duck'