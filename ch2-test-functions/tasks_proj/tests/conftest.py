import pytest

def something_plugin():
    return None

def something_plugin2():
    return None

def pytest_configure():
    pytest.task_id = something_plugin()
