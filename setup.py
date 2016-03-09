from distutils.core import setup
import py2exe

from distutils.filelist import findall
import matplotlib

opts = {"py2exe": {
    "packages" : ['matplotlib'],
    "includes": ['scipy', 'scipy.integrate', 'scipy.special.*','scipy.linalg.*'],
	           'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                'libgobject-2.0-0.dll',
                'libgdk_pixbuf-2.0-0.dll']
                         }
               }
	
setup(
      windows = [{'script': "Moment_Final.py"}], zipfile = None,
      options= opts,
      data_files = matplotlib.get_py2exe_datafiles()
    )
