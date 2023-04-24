import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
    for filename in filenames:
        sys.path.append(os.path.join(dirpath, filename))

