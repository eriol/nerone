nerone
======

`nerone` creates PyInstaller one-file executables with only dependencies for
the scripts in arguments.

The name is a pun related to how one-file executables work: when they are
started a temporary folder in the appropriate temp-folder location for the OS
is created and PyInstaller bootloader uncompresses the support files and writes
copies into the temporary folder.

The temporary folder is deleted after the code execution: this inspired the
name of the project.

See `PyInstaller documentation`_ for details.

.. _PyInstaller documentation: https://pyinstaller.readthedocs.io/en/stable/operating-mode.html#how-the-one-file-program-works

Installation
------------

.. code-block:: bash

   % pip install git+https://github.com/eriol/nerone

Usage
-----

Suppose to have the following script named `test.py`:

.. code-block:: python

   import sys

   import requests


   if __name__ == '__main__':
       print requests.head(sys.argv[2]).headers

To create a one-file executable with all the dependencies (in this case only
`requests`) you can just call `nerone` passing the script:

.. code-block:: bash

   % nerone test.py

Inside `dist` directory you will find the one-file executable witch embed the
dependencies for `test.py`.

.. code-block:: bash

   % ./dist/test test.py https://mornie.org
   {'Content-Encoding': 'gzip', 'Server': 'nginx/1.6.2', ...}
