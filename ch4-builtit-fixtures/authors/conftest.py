""" Demonstrate tmpdir_factory. """
import json
import pytest

#  created fixture, which uses tmpdir_factory but with module scope
@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """ Write some authors to a data file . """
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }
    file_json = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file: {}'.format(str(file_json)))
    with file_json.open('w') as f:
        json.dump(python_author_data, f)
    return file_json
