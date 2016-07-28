# coding: utf-8
"""
nerone.spec
~~~~~~~~~~~

THIS SOFTWARE IS UNDER GPL-2+ LICENSE.
:copyright: (c) 2016 Daniele Tricoli <eriol@mornie.org>
:license: GPL-2+, see LICENSE for more details.
"""

import ast
import inspect

# Following imports are needed by PyInstaller.building.makespec.main.
import os
from PyInstaller.building.makespec import (
    DEFAULT_SPECPATH,
    HOMEPATH,
    Path,
    bundleexetmplt,
    bundletmplt,
    cipher_absent_template,
    cipher_init_template,
    expand_path,
    is_cygwin,
    is_darwin,
    is_win,
    logging,
    main,
    make_path_spec_relative,
    onedirtmplt,
    quote_win_filepath,
)

from . import ENTRYPOINT_PATH


__all__ = ['mkspec']

onefiletmplt = """# -*- mode: python -*-
%%(cipher_init)s
a = Analysis(%(entrypoint)s,
             pathex=%%(pathex)s,
             binaries=None,
             datas=None,
             hiddenimports=%%(hiddenimports)r,
             hookspath=%%(hookspath)r,
             runtime_hooks=%%(runtime_hooks)r,
             excludes=%%(excludes)s,
             win_no_prefer_redirects=%%(win_no_prefer_redirects)s,
             win_private_assemblies=%%(win_private_assemblies)s,
             cipher=block_cipher)
b = Analysis(%%(scripts)s,
             pathex=%%(pathex)s,
             binaries=None,
             datas=None,
             hiddenimports=%%(hiddenimports)r,
             hookspath=%%(hookspath)r,
             runtime_hooks=%%(runtime_hooks)r,
             excludes=%%(excludes)s,
             win_no_prefer_redirects=%%(win_no_prefer_redirects)s,
             win_private_assemblies=%%(win_private_assemblies)s,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          b.pure, b.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          # b.scripts,
          b.binaries,
          b.zipfiles,
          b.datas,
          name='%%(name)s',
          debug=%%(debug)s,
          strip=%%(strip)s,
          upx=%%(upx)s,
          console=%%(console)s %%(exe_options)s)
""" % {'entrypoint': [ENTRYPOINT_PATH]}


def _factory():
    tree = ast.parse(inspect.getsource(main))
    tree.body.insert(
        0,
        ast.Assign(
            targets=[ast.Name(id='onefiletmplt', ctx=ast.Store())],
            value=ast.Str(s=onefiletmplt))
    )
    tree = ast.fix_missing_locations(tree)
    exec compile(tree, '<string>', 'exec')

    return main

mkspec = _factory()
