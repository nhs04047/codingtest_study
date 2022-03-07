# 11047 동전0

def greedy(num, mony):
    coins = []

    for i in range(num):
        coins.append(int(input()))

    count = 0
    for i in reversed(range(num)):
        count += mony//coins[i]
        mony = mony%coins[i] 

    return count

N, K = map(int, input().split()) 
print(greedy(N, K))