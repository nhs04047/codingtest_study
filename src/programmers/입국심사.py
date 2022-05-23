'''
입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238
'''
'''
이분탐색의 핵심은 '어떤 값을 이분 탐색 할건지?' 와 '기준을 무엇으로 잡아야 하는지?'임
이 문제에서는 시간을 가지고 이분탐색을 하면서 임의의 시간에 얼마나 많은 사람을 심사 할 수 있는 지 찾아 임의의 시간을 줄여 왼쪽 기준으로, 또는 시간을 늘려 오른쪽 기준으로 넘어 갈 건지 정하면서 진행
'''
def solution(n, times):
    answer = 0
    # 이진탐색 할 대상은 시간
    # 이진 탐색을 위한 최솟값과 최댓값 설정
    left = 0
    right = max(times) * n
    
    while left <= right:
        # 한 심사관에게 주어지는 시간
        mid = (left + right)//2
        count = 0
        for time in times:
            count += mid//time
            if count >= n:
                break
        # 모든 사람을 심사 할 수 있으면 시간을 줄여봄
        if count >= n:
            answer = mid
            right = mid-1
        # 모슨 사람을 심사 할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        elif count < n:
            left = mid+1
    
    return answer