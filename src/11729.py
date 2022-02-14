# 11729
# 재귀함수-하노이탑 : https://www.youtube.com/watch?v=aPYE0anPZqI


def hanoi(num, rot1, rot2, rot3):
    if num == 1:
        print(rot1, rot3)
    else:
        hanoi(num-1, rot1, rot3, rot2)
        print(rot1, rot3)
        hanoi(num-1, rot2, rot1, rot3)

num = int(input())
print(2**num - 1)
hanoi(num, 1, 2, 3)