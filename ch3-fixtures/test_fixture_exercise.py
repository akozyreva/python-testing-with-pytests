import pytest


@pytest.fixture()
def worker_names():
    return ['Mike', 'John', 'Tom']


@pytest.fixture(scope="session")
def worker_shedule():
    """ By using a yield statement instead of return, all
    the code after the yield statement serves as the teardown code:
    When you use return, all code after return doesn't execute
    """
    print("begining of fixtrue")
    yield {
        'name': 'Mike',
        'morning': 'Go to work',
        'afternoon': 'Go to lunch',
        'evening': 'Go to home'
    }
    print("end of fixture")


def test_worker_names_not_empty(worker_names):
    assert len(worker_names) != 0


def test_work_schedule_whole_day(worker_shedule):
    assert (bool(worker_shedule.get("afternoon")),
            bool(worker_shedule.get("morning")),
            bool(worker_shedule.get("evening"))) == (True, True, True)


def test_work_shedule_lunch_on_afternoon(worker_shedule):
    assert worker_shedule['afternoon'] == 'Go to lunch'