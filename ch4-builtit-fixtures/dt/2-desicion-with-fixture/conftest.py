import pytest
import unnecessary_math


@pytest.fixture(autouse=True)
def add_num(doctest_namespace):
    # it's equivalent to:
    # import unnecessary_math as um
    doctest_namespace['um'] = unnecessary_math