# 2217-로프

import sys

N = int(input())  # 로프의 개수

rope = [int(sys.stdin.readline()) for i in range(N)]  # 각 로프가 버틸 수 있는 최대 중량

rope.sort()

result = 0

for i in range(len(rope)):
    if result < N * rope[i]:
        result = N * rope[i]
        N -= 1
    else:
        N -= 1

print(result)
