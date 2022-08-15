"""
Bubble Sort Algorithm
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