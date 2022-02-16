# 2231 분해합


def elementSum(inputNum):

    for i in range(inputNum):

        numElement = list(map(int, str(i)))
        const = sum(numElement)+i

        if const == inputNum:
            return(i)
        
    return(0)
            

inputNum = int(input())
print(elementSum(inputNum))
