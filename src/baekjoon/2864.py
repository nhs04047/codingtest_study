# 2864-5와 6 차이

num1, num2 = input().split()

result1 = int(num1.replace('6', '5'))+int(num2.replace('6', '5'))
result2 = int(num1.replace('5', '6'))+int(num2.replace('5', '6'))

print(result1, result2)
