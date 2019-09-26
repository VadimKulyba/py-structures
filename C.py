"""wg forge task-C"""
#!/usr/bin/python2

N, M, K = raw_input().split(' ')

RESULT = []
for i in range(1, int(N) + 1):
    RESULT.append(i)
    for j in range(2, int(M) + 1):
        RESULT.append(i * j)

RESULT.sort()
print RESULT[int(K) - 1]
