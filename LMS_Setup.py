import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Library_Management_Systen.py", base=base, icon="LMSICON.ico")]


cx_Freeze.setup(
    name = "Library Management System",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["LMSICON.ico",'tcl86t.dll','tk86t.dll', 'Library_images','database']}},
    version = "1.0",
    description = "Library Management System | Developed By Krishna Raj Singh",
    executables = executables
    )