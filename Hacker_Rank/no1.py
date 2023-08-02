#!/bin/python3

import math
import os
import random
import re
import sys
import heapq



def getMinRooms(meetingTimings):
    #시작 시간을 기준으로 회의 시간을 정렬
    meetingTimings.sort(key = lambda x: x[0])

    #회의의 종료 시간을 담기 위한 우선 순위 큐
    queue = []

    for meeting in meetingTimings:
        #만약 회의의 시작 시간이 가장 이른 회의의 종료 시간보다 작지 않다면
        #그 회의실은 비어 있고, 이른 시간에 참가할 수 있음
        if queue and meeting[0] >= queue[0]:
            heapq.heappop(queue)

        # 현재 회의의 종료 시간을 큐에 푸시
        heapq.heappush(queue, meeting[1])

    #큐의 크기는 필요한 최소 회의실 수를 제공
    return len(queue)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    meetingTimings_rows = int(input().strip())
    meetingTimings_columns = int(input().strip())

    meetingTimings = []

    for _ in range(meetingTimings_rows):
        meetingTimings.append(list(map(int, input().rstrip().split())))

    result = getMinRooms(meetingTimings)

    fptr.write(str(result) + '\n')

    fptr.close()

# On a given day, there are n meetings scheduled.
# There is a list of the meetings given as a 2D array, meetingTimings, of size n x m, that contains the start and end times of the meetings. Determine the minimum number of meeting rooms needed to conduct all the meetings so that no meetings overlap in a meeting room.
# Note: Meetings can end and begin at the same time in one room. For example, meetings at times [10,15], and [15, 20] can be held in the same room.
# Example
# Suppose n = 5, meetingTimings = [[1, 4], [1, 5], [5, 6], [6, 10], [7, 9]].
# At least two meeting rooms are required. Meetings 1 and 2 overlap, as do 4 and 5. Return 2 as the answer

# Function Description
# Complete the function getMinRooms in the editor below.
# getMinRooms has the following parameter:
# int meeting Timings[n][2]: the start and end times of the meetings

# Returns
#     Int : the minimum number of meeting rooms required

# Constraints
# • 1 ≤n≤2 * 105
# • 1 ≤ meeting Timings[il[0] ≤ meeting Timings [i_[1] ≤ 2 *106
