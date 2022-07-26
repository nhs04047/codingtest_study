# 1026-보물

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a, reverse = True)
b = sorted(b)

s = 0
for i in range(n):
    s += a[i] * b[i]
print(s)

################################################
# 조건 - b 재배열 X

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

s = 0
for i in range(n):
    s += min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(s)