import time


def test_passing():
    time.sleep(0.1)
    assert (1, 2, 3) == (1, 2, 3)