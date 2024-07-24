from cx_Freeze import setup, Executable
import sys

#Specify the base for the executable for Windows GUI application 
base=None
if sys.platform=="win32":
    base="Win32GUI"


executables=[Executable('Main.py',base=base,icon='icon.ico',targetName="Frustum.exe")]     
    
setup(name="Frustum",
      version="0.1",
      options={"build_exe": {"include_files": ["Pyr.png","icon.ico"]}},
      description="Calculate volume of truncated pyramid-frustum",
      executables= executables)
