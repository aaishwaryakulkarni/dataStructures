"""
Selection Sort

"""

def selectionSort(arr):

	for i in range(len(arr)):

		min_index = i

		for j in range(i+1, len(arr)):

			if arr[j] < arr[min_index]:
				min_index = j

		arr[i],arr[min_index] = arr[min_index], arr[i]

arr = [14,46,43,27,57,41,45,21,70,1,0]

print(f"Before sorting : {arr}")
selectionSort(arr)
print(f"After sorting : {arr}")