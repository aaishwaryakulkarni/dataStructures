"""
Quick Sort Algorithm

Approach:

Set pivot as first element

start = 0
end = len(arr)

increment start till elements on left are less than pivot
decrement end till elements on right are greater than pivot
swap start with end

once start > end:
we swap arr[low] with end. i.e. pivot with end


"""
def partition(arr, low, high):

	pivot = arr[low] #pivot is first element
	start = low
	end = high

	while(start < end):

		while((start < len(arr)) and (arr[start] <= pivot)):
			start = start + 1

		while(arr[end] > pivot):
			end = end - 1

		if(start < end):
			temp = arr[start]
			arr[start] = arr[end]
			arr[end] = temp

	temp = arr[low]
	arr[low] = arr[end]
	arr[end] = temp 

	return end

def quickSort(arr, low, high):

	if low < high:

		p = partition(arr, low, high)
		quickSort(arr, low, p - 1)
		quickSort(arr, p + 1, high)


arr = [14,46,43,27,57,41,45,21,70,1,0]
print(f"Before sorting : {arr}")
quickSort(arr, 0, len(arr)-1)
print(f"After sorting : {arr}")