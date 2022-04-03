# 15649 N과 M

N, M = map(int, input().split())
arr = []

def BackTK(level):

    if level == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            BackTK(level + 1)
            arr.pop()

BackTK(0)