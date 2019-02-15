Hello!!

Dependencies
============
- `virtualenv <http://www.virtualenv.org>`_
- `pip <http://www.pip-installer.org>`_
- `git <http://git-scm.com>`_
- `bundler <http://gembundler.com>`_


Installation
============
::

    $ git clone https://github.com/jfilipe/filipe.ca
    $ cd filipe.ca
    $ virtualenv --no-site-packages --distribute env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ... wait a bit
    $ bundle install
    ... wait a bit
    $ fab serve


Deploying
=========
::

    $ fab publish
