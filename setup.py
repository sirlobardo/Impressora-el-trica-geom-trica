import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
  base = "Win32GUI"

executables = [Executable("main.py", base=base, icon="icon.ico")]

buildOptions = dict( packages = [],
                     includes = ["matplotlib.pyplot", "math", "numpy"],
                     include_files = ["impressora.py", "icon.ico"],
                     excludes = []
                   )

setup(name="Impressora de Elétrons",
      version = "0.1",
      description = "Simulador de Impressora de Elétrons",
      options = dict(build_exe = buildOptions),
      executables = executables
     )