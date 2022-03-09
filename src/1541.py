# 1541 잃어버린 괄호

q = input().split('-')

def makeBracket(arr) :
    result = 0
    
    for i in arr[0].split('+'):
        result += int(i)

    for i in arr[1:] :
        for j in i.split('+'):
            result -= int(j)

    return result

print(makeBracket(q))