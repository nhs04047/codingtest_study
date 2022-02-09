# 2941

ch = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

a = input()

for i in ch:
    a = a.replace(i, '*')

print(len(a))