import tasks
from tasks import Task
import pytest

class TestUpdate():
    """Test expected exceptions with tasks.update()."""
    def test_bad_id(self):
        """A non-int id should raise and exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict_instead': 1},
                         task=tasks.Task())
    
    def test_bad_task(self):
        """A non-Task task should raise an exception. """
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')