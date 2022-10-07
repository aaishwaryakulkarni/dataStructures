"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

def setZeroes(matrix):

	rows = len(matrix)
	cols = len(matrix[0])
	row_zero = False

	for r in range(rows):
		for c in range(cols):

			if matrix[r][c] == 0:
				matrix[0][c] = 0

				if r > 0:
					matrix[r][0] = 0
				else:
					row_zero = True

	for r in range(1, rows):
		for c in range(1, cols):

			if matrix[r][0] == 0 or matrix[0][c] == 0:
				matrix[r][c] = 0

	if matrix[0][0] == 0:
		for r in range(rows):
			matrix[r][0] = 0

	if row_zero:
		for c in range(cols):
			matrix[0][c] = 0

	return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))