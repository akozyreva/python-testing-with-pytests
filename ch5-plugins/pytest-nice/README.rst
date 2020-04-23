pytest-nice : A pytest plugin =============================
Makes pytest output just a bit nicer during failures.
Features 
--------
- Includes user name of person running tests in pytest output. - Adds ``--nice`` option that:
- turns ``F`` to ``O``
- with ``-v``, turns ``FAILURE`` to ``OPPORTUNITY for improvement``
Installation 
------------
Given that our pytest plugins are being saved in .tar.gz form in the shared directory PATH, then install like this:
::
Usage -----
::
$ pytest --nice