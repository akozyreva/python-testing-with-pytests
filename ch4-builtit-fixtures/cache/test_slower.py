"""Code of pytest slow plugin """
from datetime import datetime
from random import random
import time
import pytest
@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(":", "_")
    # request.node.nodeid. = ch4-builtit-fixtures/cache/test_slower.py::test_slow_stuff[0]
    # nodeid's can have colons
    # keys become filenames withc .cache
    # replace colons with something filename safe
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = "this duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring    


#@pytest.mark.parametrize('i', range(5))
#def test_slow_stuff(i):
#    time.sleep(random())