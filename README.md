# Truncated Pyramid Volume Calculator

## Description
This Python application provides a graphical user interface for calculating the volume of truncated pyramids (frustums). 
It's designed for engineers and professionals working with earthwork calculations.

## Features
- Easy-to-use GUI built with PyQt5
- Accurate volume calculations for truncated pyramids
- Visual representation of the frustum
- Error handling and input validation

## Installation
1. Clone the repository: https://github.com/ProdromosKarasavvidis/Frustum

2. Install required packages: pip install PyQt5 cx_Freeze


Application Deployment Instructions:
File Organization:
Ensure all Python source files (.py) are consolidated within a single directory. 
This includes Main.py, vol_trap.py, vol_trap_form.py, and setup.py.

Execution:
a. For direct Python execution:
Launch the application by running Main.py using a Python interpreter.

b. For creating a standalone executable:
i.  Open a command prompt or terminal.
ii. Navigate to the directory containing the source files.
iii. Execute the following command:
python setup.py build
This process will generate an executable (.exe) version of the application, 
enabling usage on systems without a Python environment installed.

Note: Ensure all necessary dependencies, including PyQt5 and cx_Freeze, 
are properly installed in your Python environment before attempting to build the executable."

## Usage
1. Run the application: Main.py

2. Enter the required measurements:
- Area 1 (E) in m²
- Area 2 (e) in m²
- Height (h) in m
3. Click "Calculate Volume" to get the result.

## Creating an Executable
To create a standalone .exe file:
1. Open a command prompt in the project directory.
2. Run:
