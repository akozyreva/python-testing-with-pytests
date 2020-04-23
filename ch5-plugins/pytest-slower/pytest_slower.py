""" Code for pytest slow plugin. """
from datetime import datetime
from random import random
import time
import pytest


def pytest_addoption(parser):
    """ Turn nice features on with --slow option. """
    group = parser.getgroup('slower')
    group.addoption("--slower", action="store_true",
                    help="slow: fail slowest tests")
        

def pytest_runtest_call(config, cache, request):
    if config.getoption('slower'):
        key = 'duration/' + request.node.nodeid.replace(":", "_")
        start_time = datetime.now()
        yield
        stop_time = datetime.now()
        this_duration = (stop_time - start_time).total_seconds()
        last_duration = cache.get(key, None)
        cache.set(key, this_duration)
        if last_duration is not None:
            errorstring = "this duration over 2x last duration"
            assert this_duration <= last_duration * 2, errorstring    