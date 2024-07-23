"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

import collections

class Solution(object):
	def numIslands(self, grid):
		
		if not grid:
			return 0
		
		islands = 0
		visited = set()
		rows, cols = len(grid), len(grid[0])
		directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

		def bfs(r, c):
			q = collections.deque()

			visited.add((r, c))
			q.append((r, c))

			while q:
				cur_r, cur_c = q.popleft()

				for dr, dc in directions:

					new_dr = cur_r + dr
					new_dc = cur_c + dc

					if (new_dr in range(rows) and new_dc in range(cols) and
						grid[new_dr][new_dc] == "1" and (new_dr, new_dc) not in visited):
						
						visited.add((new_dr, new_dc))
						q.append((new_dr, new_dc))

		for r in range(rows):
			for c in range(cols):
				if (grid[r][c] == "1" and 
					(r, c) not in visited):
					bfs(r, c)
					islands += 1
		
		return islands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

soln = Solution()
print(soln.numIslands(grid))