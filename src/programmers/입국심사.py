'''
입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238
'''
'''
이분탐색의 핵심은 '어떤 값을 이분 탐색 할건지?' 와 '기준을 무엇으로 잡아야 하는지?'임
이 문제에서는 시간을 가지고 이분탐색을 하면서 임의의 시간에 얼마나 많은 사람을 심사 할 수 있는 지 찾고, 임의의 시간을 줄여 왼쪽 기준으로, 또는 시간을 늘려 오른쪽 기준으로 넘어 갈 건지 정하면서 진행

n = 6
times = [7, 10]

left <= 0
right <= max(times) * n

loop 탈출 조건 : left>=right

* loop 1
0 1 2 3 ... 29 30 31 ... 58 59 60
left		 mid		     right
mid 시간 동안 심사가 가능한 사람 수 => 7명 ( 30//7 + 30//10 = 4+3)
mid 시간은 n명보다 많은 사람을 심사 가능 => 30을 기준으로 왼쪽 탐색 -> right = mid-1
answer <= 30

* loop 2
0 1 2 3 ... 14 15 16 ... 27 28 29
left		 mid		    right
mid 시간 동안 심사가 가능한 사람 수 => 3명 ( 15//7 + 15//10 = 2+1)
mid 시간은 n명보다 적은 사람을 심사 가능 => 15를 기준으로 오른쪽 탐색 -> left = mid+1

* loop 3
16 17 18 ... 21 22 23 ... 27 28 29
left		  mid		     right
mid 시간 동안 심사가 가능한 사람 수 => 5명 ( 22//7 + 22//10 = 3+2)
mid 시간은 n명보다 적은 사람을 심사 가능 => 22을 기준으로 오른쪽 탐색 -> left = mid+1

* loop 4
23 24 25 26 27 28 29
left       mid	        right
mid 시간 동안 심사가 가능한 사람 수 => 5명 ( 26//7 + 26//10 = 3+2)
mid 시간은 n명보다 적은 사람을 심사 가능 => 36을 기준으로 오른쪽 탐색 -> left = mid+1

* loop 5
 27   28   29
left  mid  right
mid 시간 동안 심사가 가능한 사람 수 => 6명 ( 28//7 + 28//10 = 4+2)
mid 시간은 n명과 같은 사람 수를 심사 가능 => 28을 기준으로 오른쪽 탐색 -> right = mid-1
answer <= 28

* loop 6
left, right 둘 다 27
loop 탈출
answer은 28
'''
def solution(n, times):
    answer = 0
    # 이분탐색 할 대상은 시간
    # 이분탐색을 위한 최솟값과 최댓값 설정
    left = 0
    right = max(times) * n
    
    while left <= right:
        # 한 심사관에게 주어지는 시간
        mid = (left + right)//2
        count = 0 # 입국심사가 완료된 사람 수 정의
        for time in times:
            count += mid//time
            #일단 총 사람 수(n)보다 넘으면 반복문 종료
            if count >= n:
                break
        # 심사할 수 있다면 그 시간을 저장하고
        # 더 짧은 시간 내에 심사할 수 있는지 확인
        if count >= n:
            answer = mid
            right = mid-1
        # 모슨 사람을 심사 할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        elif count < n:
            left = mid+1
    
    return answer