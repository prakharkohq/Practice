"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.)

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation:
Only need one meeting room

"""
import heapq


class Solution:
  def minMeetingRooms(self, intervals) -> int:
    minHeap = []  # Store end times of each room.
    sorted_intervls =  sorted(intervals)
    for start, end in sorted_intervls:
      # No overlap, we can reuse the same room.
      if minHeap and start >= minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, end)

    return len(minHeap)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([(0,30),(4,10),(1,23),(15,20)]))