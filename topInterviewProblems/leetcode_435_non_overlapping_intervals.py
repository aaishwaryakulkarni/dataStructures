"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return
the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

def eraseOverlapIntervals(intervals):

	result = 0
	intervals.sort()

	prev_end = intervals[0][1]

	for s, e in intervals[1:]:

		if s >= prev_end:
			prev_end = e

		else:
			result = result + 1
			prev_end = min(prev_end, e)

	return result

intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))