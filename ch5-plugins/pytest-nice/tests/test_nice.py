import pytest
@pytest.fixture
def sample_test(testdir):
    # create a temprorary pytest test module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
     """)
    return testdir

# I added * at the end of matcning lines. it seems, it's a bug in pytest.
# it's not a good desicion. another solution:
# use assert thanks_msg not in result.stdout.str()
def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    print(result.stdout.str())
    result.stdout.fnmatch_lines(['*.O*', ])  # . for Pass, O for Fail
    assert result.ret == 1

def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*'
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*'])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks tester for running tests.'])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_msg = 'Thanks tester for running tests.'
    assert thanks_msg not in result.stdout.str()

def test_help_msg(testdir):
    result = testdir.runpytest('--help')
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: turn failures into opportunities'
    ])