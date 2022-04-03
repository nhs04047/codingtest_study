# 10872 팩토리얼

def fac(n):
    if n < 2:
        return 1
    else:
        return n*fac(n-1)
    
a = int(input())
print(fac(a))