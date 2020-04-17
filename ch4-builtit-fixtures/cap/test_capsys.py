import sys
def greeting(name):
    print('Hi, {}'.format(name))


# you can test actually stdout with built-in fixtuer capsys
def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    assert out == 'Hi, Earthling\n'
    assert err == ''

    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''


def yikes(problem):
    print ('YIEKES! {}'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == '' 
    assert 'Out of coffee' in err


# if you want to see print statement anyway,
# you can use capsys.disabled() fixture
def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nalways print this')
    print('normal print, usually captured')