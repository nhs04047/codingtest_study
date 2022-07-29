T = int(input())

if T >= 300:
    a = T//300
    T %= 300
else:
    a = 0

if T >= 60:
    b = T//60
    T %= 60
else:
    b = 0

if T >= 10:
    c = T//10
    T %= 10
else:
    c = 0

if T != 0:
    print(-1)
else:
    print(a, b, c)
