import pytest
import tasks
from tasks import Task


def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'Brian', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should be the same
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check 2 tasks for equivalence."""
    # Compare everything but the if field
    return (
        (t1.summary == t2.summary) and
        (t1.owner == t2.owner) and
        (t1.done == t2.done)
    )


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield   # this is where testing happens
    # Teardown: stop db
    tasks.stop_tasks_db()

@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('ware, brian'),
                                  Task('breathe', 'BRIAN', True),
                                  Task('exercise', 'BrIaN', False)
                                  ])
def test_add_2(task):
    """ Demonstrate parametrize with 1 parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('summary, owner, done', 
                         [
                             ('sleep', None, False),
                             ('wake', 'brian', False),
                             ('breathe', 'BRIRAN', True),
                             ('eat eggs', 'BrIaN', False)
                         ])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


tasks_to_try = (
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)
)
@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """ Slightly different take. """
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    

# for formatting output in console!
task_ids = [
    'Task({}, {}, {})'.format(t.summary, t.owner, t.done)
    for t in tasks_to_try
]
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids.
    You see data in console.
    """
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """ Demonstrate parametrize and test classes
    Parametrized data will be sent to all methods
    """
    def test_equivalent(self, task):
        """ Similar test, just within a class. """
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """ We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id

# specify your own ids for tests!
@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done'),
])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)