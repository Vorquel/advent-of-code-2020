#!/usr/bin/python
import re
import sys
good_1 = 0
good_2 = 0
for line in sys.stdin:
 match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
 low = int(match[1])
 high = int(match[2])
 letter = match[3]
 password = match[4]
 if low <= len(re.findall(letter, password)) <= high:
  good_1 += 1
 if (password[low-1]==letter) + (password[high-1]==letter) == 1:
  good_2 += 1
print(f'There are {good_1} good passwords by the first measure')
print(f'There are {good_2} good passwords by the second measure')
print(good_1)
print(good_2)
