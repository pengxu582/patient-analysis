"""
This module counts the no. of line in standard input
Input: a string
"""

import sys

count =0
for line in sys.stdin:
	count  += 1
print(count, "lines in standard input")
