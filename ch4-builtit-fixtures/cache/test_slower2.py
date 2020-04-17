import pytest
from collections import namedtuple
from datetime import datetime
import time
from random import random
Duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/test_durations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.now()
    yield
    duration = (datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration
    if d.last.get(nodeid, None) is not None:
        error_string = "test duration over 2x last duratoin"
        assert duration <= (d.last[nodeid] * 2), error_string


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random())