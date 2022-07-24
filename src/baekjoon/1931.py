# 1931-회의실 배정

import sys

def greedy(meetings):
    count = 0
    time = 0
    
    for meeting in meetings:
        if meeting[0] >= time:
            time = meeting[1]
            count += 1
    return count


meetCount = int(sys.stdin.readline())
meetings = []

for _ in range(meetCount):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))
meetings = sorted(meetings, key=lambda time:time[0])
meetings = sorted(meetings, key=lambda time:time[1])

print(greedy(meetings))
