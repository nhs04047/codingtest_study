# 11651

N = int(input())
 
li = [] # 2차원리스트
for _ in range(N):
    xy = list(map(int,input().split()))
    li.append([xy[1],xy[0]])
 
li.sort()
 
for i in li:
    print(i[1],i[0])