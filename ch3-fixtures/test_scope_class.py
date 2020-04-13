""" Demo fixture scope. """
import pytest

@pytest.fixture(scope='class')
def class_scope():
    """ A class scope fixture. """



@pytest.mark.usefixtures('class_scope')
class TestSomth():
    """ Demo class scope fixtures. """
    
    def test_3(self):
        """ Test using a class scope fixture. """
    
    def test_4(self):
        """ Again, multiple tests are more fun. """