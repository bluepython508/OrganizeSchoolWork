import os

from cx_Freeze import setup, Executable
import sys
# Dependencies are automatically detected, but it might need
# fine tuning.
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
buildOptions = dict(packages=[], excludes=[])
buildOptions.update({

    'include_files': [
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
    ],
})

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('gui.py', base=base, targetName='OrganizeSchoolWork.exe', shortcutName='OrganizeSchoolWork',shortcutDir='DesktopFolder')
]

setup(name='OrganizeSchoolWork',
      version='1.0',
      description='',
      options=dict(build_exe=buildOptions),
      executables=executables, requires=['cx_Freeze'])
