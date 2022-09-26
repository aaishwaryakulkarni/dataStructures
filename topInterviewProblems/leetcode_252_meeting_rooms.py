"""
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""

def canAttendMeetings(intervals):

	intervals.sort(key = lambda i: i[0])

	for i in range(1, len(intervals)):

		if intervals[i][0] < intervals[i-1][1]:
			return False

intervals = [[15,20],[0,30],[5,10]]
print(canAttendMeetings(intervals))