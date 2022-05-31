def solution(numbers, hand):
    answer = ''

    left_hand = '*'   ## 초기 왼손 위치
    right_hand = '#'  ## 초기 오른손 위치
    
    
    ## 키패드 생성
    keypad = {1 : [0,0], 2 : [0,1], 3 : [0,2], 
              4 : [1,0], 5 : [1,1], 6 : [1,2], 
              7 : [2,0], 8 : [2,1], 9 : [2,2],
              '*':[3,0], 0 : [3,1], '#':[3,2]}
              
    for i in numbers:
        if i in [1,4,7]:   ## 1,4,7인 경우 왼손
            answer += 'L'
            left_hand = i
        elif i in [3,6,9]: ## 3,6,9인 경우 오른손
            answer += 'R'
            right_hand = i
        else:			## 2,5,8,0인 경우 거리계산
            left_axis = keypad[left_hand]  ## 왼손 키패드 위치
            right_axis = keypad[right_hand] ## 오른손 키패드 위치
			
            ## 거리 절댓값 이용
            left_dist = abs(left_axis[0] - keypad[i][0]) + abs(left_axis[1] - keypad[i][1])
            right_dist = abs(right_axis[0] - keypad[i][0]) + abs(right_axis[1] - keypad[i][1])
            
            if left_dist < right_dist : # 왼손이 가까운 경우
                answer += 'L'
                left_hand = i
            elif left_dist > right_dist : # 오른손이 가까운 경우
                answer += 'R'
                right_hand = i
            else:						# 거리가 동일한 경우
                if hand == 'left':
                    answer += 'L'
                    left_hand = i
                else:
                    answer += 'R'
                    right_hand = i
    return answer