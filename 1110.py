# 1110번

num = int(input())
count = 0

newNum = num
while True:
    
    if( newNum < 10):
        a = newNum * 10
        b = newNum
        newNum = a + b
    else:
        a = (newNum % 10) * 10
        b = ((newNum // 10) + (newNum % 10)) % 10
        newNum = a + b
    
    count = count + 1
    if(newNum == num):
        print(count)
        break
    