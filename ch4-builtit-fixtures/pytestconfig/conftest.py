# it's possible to add more options to the console. 
# you can see it via pytest --help


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store",
                     default="bar", help="foo: bar or baz")
