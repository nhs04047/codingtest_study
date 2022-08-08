# 15904 - UCPC는 무엇의 약자일까?

s = input()
u = ''
alp = [chr(i) for i in range(65, 91)]
for i in s:
    if i in alp:
        u += i
if u == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')
