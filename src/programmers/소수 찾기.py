'''
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
'''

from itertools import permutations

def solution(numbers):
    
  answer = []
  cards = list(num for num in numbers)
  numTmp = []
  newNumbers = []
  newNumbersSet = []
  
  for i in range(1, len(cards)+1):
    numTmp += (permutations(cards, i))
  
  for i in numTmp:
    newNumbers.append(int(("").join(i)))
  
  for i in newNumbers:
    if i not in newNumbersSet:
      newNumbersSet.append(i)
  
  for i in newNumbersSet:
    if i < 2:
      continue
    answer.append(i)
      
    for j in range(2, int(i/2)+1):
      if i % j == 0:
        answer.pop()
        break
              
  
  return len(answer)