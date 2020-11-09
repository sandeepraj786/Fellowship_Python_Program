"""
author -sandeep raj
date -09-11-2020
time -18:00
package -String
problem Statement-'Write a Python program to display formatted text (width=50) as output..
"""

import textwrap
sample_text = '''
  GitHub, Inc. is an American multinational corporation that provides hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration and wikis for every project.[4] Headquartered in California, it has been a subsidiary of Microsoft since 2018.[5
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()

