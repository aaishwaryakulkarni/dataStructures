"""
Bubble Sort Algorithm

Note:
The second for loop ends at len(arr)-i-1
This is because everything at index greater than it is already sorted.

After 1st iteration, the largest element is at len(arr)-1
After 2nd iteration, the 2nd largest element is at end-1 position len(arr)-2
and so on.
"""

def bubbleSort(arr):

	for i in range(len(arr)):
		for j in range(0 , len(arr)-i-1):

			if(arr[j] > arr[j+1]):

				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

arr = [14,46,43,27,57,41,45,21,70,1,0]

print(f"Before sorting : {arr}")
bubbleSort(arr)
print(f"After sorting : {arr}")