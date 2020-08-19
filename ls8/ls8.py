#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
# print(sys.argv)
cpu.load(f'{sys.argv[1]}')
cpu.run()
