import pytest

# example of running with cmd 
# pytest -s --myopt --foo baz test_config.py 
# pytestconfig is also a fixture
def test_option(pytestconfig):
    """ 
    in cmd you can call 
    pytest -s --myopt --foo test_config.py   
    and options values will change to the values from conftest.py
    """
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt set to:', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('new test')
    print('foo set to ', foo)
    print('myopt set to ', myopt)


def test_pytestconfig(pytestconfig):
    print('exmaple of a configuration of pytestconfig options')
    print('args:                :', pytestconfig.args)
    print('inifile              :', pytestconfig.inifile)
    print('invocation_dir        :', pytestconfig.invocation_dir)
    print('rootdir          :', pytestconfig.rootdir)
    print('-k <Expresssion>', pytestconfig.getoption('keyword'))
    print('-v --verbose     :', pytestconfig.getoption('verbose'))
    # print('-q --quiet       :', pytestconfig.getoption('quiet'))
    print('-l --showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style           :', pytestconfig.getoption('tbstyle'))