# 4796-캠핑

import sys

count = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L+P+V == 0:
        break
    cam = ((V // P) * L) + min((V % P), L)

    print("Case {}: {}".format(count, cam))
    count += 1
