# 1316

chNum = int(input())

count = chNum
for _ in range(chNum):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                count -= 1
                break
print(count)