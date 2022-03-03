# 15651 N과 M (3)

N, M = map(int, input().split())
arr = []

def dfs(level):

    if level == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
            arr.append(i)
            dfs(level + 1)
            arr.pop()

dfs(0)