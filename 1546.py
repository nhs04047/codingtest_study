# 1546

num = int(input())
M = list(map(int, input().split()))
M_max = max(M)

for i in range(num):
    M[i] = M[i]/M_max*100
avg = sum(M)/ num
print("%.2f" %avg)