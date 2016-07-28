# coding: utf-8
"""
nerone.cli
~~~~~~~~~~

This module implements CLI interface of nerone.

THIS SOFTWARE IS UNDER GPL-2+ LICENSE.
:copyright: (c) 2016 Daniele Tricoli <eriol@mornie.org>
:license: GPL-2+, see LICENSE for more details.
"""

import os

import click
import PyInstaller.building.build_main

from . import ENTRYPOINT_PATH
from .spec import mkspec

BASE_CONFIG = {
    'bundle_identifier': None,
    'clean_build': False,
    'console': True,
    'debug': False,
    'excludes': [],
    'hiddenimports': [],
    'hookspath': [],
    'icon_file': None,
    'key': None,
    'loglevel': 'INFO',
    'manifest': None,
    'name': None,
    'noupx': False,
    'onefile': True,
    'pathex': [],
    'resources': [],
    'runtime_hooks': [],
    'strip': False,
    'uac_admin': False,
    'uac_uiaccess': False,
    'upx': False,
    'upx_dir': None,
    'version_file': None,
    'win_no_prefer_redirects': False,
    'win_private_assemblies': False,
}
DEFAULT_DIST_DIR = 'dist'
DEFAULT_WORK_DIR = 'build'


@click.command()
@click.argument('scripts', nargs=-1, required=True, type=click.Path(exists=True))  # noqa
def main(scripts):

    scripts = click.format_filename(scripts)
    basepath = os.path.dirname(os.path.abspath(scripts[0]))
    distpath = os.path.join(basepath, DEFAULT_DIST_DIR)
    workpath = os.path.join(basepath, DEFAULT_WORK_DIR)

    config_makespec = {
        'ascii': False,
        'distpath': distpath,
        'noconfirm': False,
        'specpath': None,
        'workpath': workpath,
    }
    config_makespec.update(BASE_CONFIG)

    spec = mkspec(scripts, **config_makespec)

    config_build = {
        'distpath': distpath,
        'filenames': [ENTRYPOINT_PATH],
        'specpath': spec,
        'workpath': workpath,
    }
    config_build.update(BASE_CONFIG)

    PyInstaller.building.build_main.main(None, spec, False, **config_build)
