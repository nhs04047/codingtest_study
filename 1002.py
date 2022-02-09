import math

def getk(x1, y1, x2, y2):
    return math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    k = getk(x1, y1, x2, y2)

    if k == 0:
        if r1 == r2:    
            print(-1)
        else:    
            print(0)
    else:
        if k < r1+r2 and k>abs(r1-r2):    
            print(2)
        elif k == r1+r2 or k == abs(r1-r2):
            print(1)
        else:
            print(0)