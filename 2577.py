# 2577

a = int(input())
b = int(input())
c = int(input())

d = a * b * c

num_list = list(map(str,str(d)))

for i in range(0, 10):
    print(num_list.count(str(i)))