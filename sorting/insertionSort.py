"""
Insertion Sort

i pointer will move forword from 1st index
j will move backward from i-1th index

"""

def insertionSort(arr):

	for i in range(1,len(arr)):

		temp = arr[i]
		j = i - 1

		while(j >= 0 and temp < arr[j]):
			arr[j + 1] = arr[j]
			j = j - 1

		arr[j + 1] = temp



arr = [14,46,43,27,57,41,45,21,70,1,0]

print(f"Before sorting : {arr}")
insertionSort(arr)
print(f"After sorting : {arr}")