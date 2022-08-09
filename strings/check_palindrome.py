"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""
import re

input_str = "A man, a plan, a canal: Panama"

def isPalindorme(input_str):
	cleaned_str = re.split('[^a-zA-Z0-9]',input_str)
	check = ''.join(cleaned_str).lower()
	
	if check == check[::-1]:
		return True
	else:
		return False

valid = isPalindorme(input_str)
print(valid)
