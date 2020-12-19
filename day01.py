#!/usr/bin/python
import sys
ints = [int(line) for line in sys.stdin]
for i,x in enumerate(ints):
 for j,y in enumerate(ints[i+1:]):
  if x+y==2020:
   print(f'{x} + {y} = {x+y}')
   print(f'{x} * {y} = {x*y}')
   print(x*y)
  for z in ints[j+1:]:
   if x+y+z==2020:
    print(f'{x} + {y} + {z} = {x+y+z}')
    print(f'{x} * {y} + {z} = {x*y*z}')
    print(x*y*z)
