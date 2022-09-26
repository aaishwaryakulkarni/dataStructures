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

def numIslands(grid):

	visited = set()
	islands = 0

	rows = len(grid)
	cols = len(grid[0])

	directions = [[-1,0], [1,0],[0,-1],[0,1]]

	def bfs(r, c):

		q = collections.deque()
		visited.add((r, c))
		q.append((r, c))

		while q:

			row, col = q.popleft()

			for dr in directions:

				new_r, new_c = row + dr[0], col + dr[1]

				if ((new_r in range(rows)) and 
					(new_c in range(cols)) and
					(grid[new_r][new_c] == '1') and
					(new_r, new_c) not in visited):

					q.append((new_r, new_c))
					visited.add((new_r, new_c))


	for r in range(rows):
		for c in range(cols):

			if((grid[r][c] == '1') and 
				((r,c) not in visited)):

				bfs(r, c)

				islands = islands + 1

	return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))