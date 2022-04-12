# 1417 - 국회의원 선거

N = int(input())
dasom = int(input())

candidates = []
count = 0

for _ in range(N - 1) :
  candidate = int(input())
  if candidate >= dasom :
    candidates.append(candidate)

while True :
  if len(candidates) == 0 :
    break

  candidates.sort(reverse=True)

  if candidates[0] >= dasom :
    
    candidates[0] -= 1
    dasom += 1
    count +=1
  if candidates[0] < dasom :
    candidates.pop(0)

print(count)