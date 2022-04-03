n=int(input())

#분해합 생성자의 범위 
#분해합이 n일 때, 생성자는 n-1보다 작거나 같고 n에서 각 자릿수에 9를 곱한 값을 뺀 값보다 크거나 같다.
# n-n의자릿수*9 <= 생성자 <= n-1

def deConst(n):
    digit=len(str(n))
    end = n
    result=0

    if n-digit*9 < 0: #n이 digit*9보다 작을 때,
        start = 0 #탐색은 0에서 시작
    else:
        start = n-digit*9
    for i in range(start,end):
        isplitSum=0
        #print(i)
        for j in range(digit):
            isplitSum += int(str(i)[j])
        #print(int(i)+isplitSum)
        if (n==(i+isplitSum)):
            result=i
        return result

print(deConst(n))