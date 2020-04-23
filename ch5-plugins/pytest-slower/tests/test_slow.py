import pytest
@pytest.fixture
def sample_test(testdir):
    # create a temprorary pytest test module
    testdir.makepyfile("""
        import time
        def test_pass():
            time.sleep(0.1)

        def test_fail_if_slow():
            time.sleep(2.1)
     """)
    return testdir


def test_with_slow(sample_test):
    result = sample_test.runpytest('--slower')
    result.stdout.fnmatch_lines(['*.E*', ])  # . for Pass, E for Error
    assert result.ret == 1


def test_help_msg(testdir):
    result = testdir.runpytest('--help')
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'slower:',
        '*--slower*slow: fail slowest tests'
    ])