 #11399 ATM
 
def atm(num, time) :
    sum = 0
    result = 0
    time.sort()

    for  i in range(num):
        sum += time[i]
        result += sum
    
    return result

N = int(input())
P = list(map(int, input().split()))

print(atm(N, P))