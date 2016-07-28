# coding: utf-8
"""
nerone.entrypoint
~~~~~~~~~~~~~~~~~

THIS SOFTWARE IS UNDER GPL-2+ LICENSE.
:copyright: (c) 2016 Daniele Tricoli <eriol@mornie.org>
:license: GPL-2+, see LICENSE for more details.
"""

import sys


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit('A script is required.')

    execfile(sys.argv[1])
