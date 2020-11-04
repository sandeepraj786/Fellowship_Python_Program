"""
author - sandeep raj
date - 04/11/2020
time - 09:05
problem statement -" Write a Python program to find the available built-in modules."
"""

import sys
import textwrap
try:
 module_name = ', '.join(sorted(sys.builtin_module_names))
 print(textwrap.fill(module_name, width=70))
except:
    print("CheckedInBuiltMethodAndArgument")