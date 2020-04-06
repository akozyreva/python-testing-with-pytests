# python-testing-with-pytests
## Description
This project is a tutorial for learning pytest, based on book "Python testing with pytest"

## Useful commands
How to create virtualenv
```
$ pip3 install -U virtualenv
$ python3 -m virtualenv -p $(which python3) python-testing-with-pytests
$ source venv/bin/activate
$ pip install pytest
```
How to activate virtualenv
```
source <project-name>/bin/activate
```
How to deactivate virtualenv
```
deactivate
```
In order to see all installed packages in current env: `pip list`

In order to run tests - go to the desired  directory and run `pytest`
or `pytest tasks/`
or `pytest tasks/test_three.py`

Run one test

```$ pytest -v tasks/test_four.py::test_asdict```

Pytest Options

| Option      | Description | Example |
| ----------- | ----------- | -------- |
| --collect-only| shows all modules and functions  | pytest tasks/ --collect-only |
|-k <expression>| allows to select tests via expression | pytest tasks/ -k "asdict" --collect-only |
|-m <decorator-name> | run tests with specified decorator | pytest tasks/ -m run_these_please |
-x, -exitfirst | if used, running stops on 1 failure | pytest -x | 
| -maxfail=num | max couts of tests, which can be failed | pytest -maxfail=2 |
| --tb=no | disabled showing traceback | pytest --tb=no |
| --tb=short | provides short info about error | pytest --tb=no |
| --tb=line | shows 1 line of error | pytest --tb=line |
|-s | allows to see print statement in console | pytest -s |
| --lf | allows to rerun failed tests | pytest --lf |
| --ff | runs firstly 1 fail and then all other tests | pytest --ff |
| -v | allows to see add info | pytests -v |
| -q | decreases info about test running to minimum | pytest -q |
| -l | shows local variables, if test fails | pytest -l |
| --durations=N | shows the N numbers slowest tests | pytest --durations=3# python-testing-with-pytests