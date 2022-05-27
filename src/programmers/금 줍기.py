from collections import deque

def main():
    N = int(input())
    arr = list(map(int, input().split()))

    left = deque()
    right_first = deque()
    right_second = deque()
    right_first_tmp=deque()
    right_second_tmp=deque()
    left_max = 0
    idx = 0
    
    for i in range(len(arr)):
        left.appendleft(arr[i])
        if len(left) == 3:
          if sum(left) > left_max:
            left_max = sum(left)
            idx = i
          left.popleft()
    
    if idx-3 > 3:
      right_first = arr[:idx-2]


    
    if len(arr) - idx > 3:
      right_second = arr[idx+1:]


        
        

if __name__=="__main__":
    main()