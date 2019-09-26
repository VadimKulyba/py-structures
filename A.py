"""wg forge task-A"""
#!/usr/bin/python2
import sys

C = raw_input().split(' ')

if int(C[0])**int(C[1]) < int(C[1])**int(C[0]):
    print '<'
    sys.exit(0)
elif int(C[0])**int(C[1]) > int(C[1])**int(C[0]):
    print '>'
    sys.exit(0)

print '='
sys.exit(0)
