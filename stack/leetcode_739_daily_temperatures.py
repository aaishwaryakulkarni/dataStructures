"""
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

"""


def dailyTemperatures(temperatures):

	days = [0] * len(temperatures)
	stack = []

	for index, temp in enumerate(temperatures):
		while stack and temp > stack[-1][1]:
			
			sindex, stemp = stack.pop()
			days[sindex] = (index - sindex)

		stack.append((index, temp))

	return days

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))


"""
stack = [(0,73),]
74 > 73. pop 73, diff = 1-0 = 1

stack = [(1, 74)]
75 > 74. pop 74, diff = 2-1 = 1

stack = [(2,75)]
71 < 75, 69 < 71

stack = [(2,75), (3,71), (4,69)]

72 > 69
pop (4, 69) diff = 5-4 = 1

72 > 71

pop(3, 71) diff = 5-3 = 2

"""