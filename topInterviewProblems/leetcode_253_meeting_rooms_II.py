"""
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""

def minMeetingRooms(intervals):

	start = sorted([i[0] for i in intervals])
	end = sorted([i[1] for i in intervals])

	min_rooms = 0
	count = 0
	s = 0
	e = 0

	while(s < len(intervals)):

		if start[s] < end[e]:
			s = s + 1
			count = count + 1

		# start[s] == end[e] and start[s] > end[e]
		else:
			e = e + 1
			count = count - 1

		min_rooms = max(min_rooms, count)


	return min_rooms

intervals = [[15,20],[0,30],[5,10]]
print(minMeetingRooms(intervals))