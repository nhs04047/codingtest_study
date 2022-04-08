# 카드 2

from collections import deque

def solution(N) :

  cards = deque(list(range(1, N+1)))

  while True :
    if len(cards) <= 1:
      return cards.pop()
    cards.popleft()
    # cards.append(cards.popleft())
    cards.rotate(-1)

N = int(input())    
print(solution(N))