from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    includes = ['board', 'shape', 'tetrominoe'],
    include_files = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('tetris.py', base=base)
]

setup(name='Tetris',
      version = '1.0',
      description = 'A PyQt Tetris Program',
      options = dict(build_exe = buildOptions),
      executables = executables)
