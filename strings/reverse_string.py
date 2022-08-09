"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

arr_original = ["h","e","l","l","o"]

print('Original array : {}'.format(arr_original))

last_element_index = len(arr_original) - 1

for i in range(len(arr_original)):
	if i < last_element_index:
		starting_element = arr_original[i]

		arr_original[i] = arr_original[last_element_index]
		arr_original[last_element_index] = starting_element
		last_element_index = last_element_index - 1


print('Reserved array : ',arr_original)