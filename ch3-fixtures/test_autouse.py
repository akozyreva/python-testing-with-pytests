""" Demonstrate autouse fixtures.
This fixtures run depend on their scope.
It doesn't matter after/before what actually test.
If you want to see print statements, use -s option.
"""

import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """ Report the time at the end of a session"""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """ Report test durations after each function. """
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1():
    """Simulate slightly longer test."""
    time.sleep(1.23)


def test_2():
    """ Simulate long-ish running test. """
    time.sleep(1)