"""wg forge task-A"""
#!/usr/bin/python2
import math
import sys

C = raw_input().split(' ')

A = int(C[0])
B = int(C[1])

LOG = A

if A != 1:
    LOG = A * math.log(B, A)
elif A == 1 and B != 1:
    print('<')
    sys.exit(0)

if B < LOG:
    print('<')
    sys.exit(0)
elif B > LOG:
    print('>')
    sys.exit(0)

print('=')
sys.exit(0)
