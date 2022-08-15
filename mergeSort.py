"""
Merge Sort Algorithm

Approach:

Divide and Conquer

Split array in 2 equal halves.
Call merge function on both halves
Keep doing this till all elements are covered

for each left and right halves, check which element is smaller and 
add that to the list.

At a point one list will still remain to iterate completely.
Add all elements to the nlist

"""


def mergeSort(nlist):

    if len(nlist) > 1:

        # split array in 2 halves
        mid = len(nlist)//2
        left = nlist[:mid]
        right = nlist[mid:] 

        # recursively call merge sort on both halves
        mergeSort(left)
        mergeSort(right)

        # i for left, j for rigt, k for nlist
        i = j = k = 0

        # add the element which is less in nlist from index k = 0
        while((i < len(left)) and (j < len(right))):
            if left[i] < right[j]:
                nlist[k] = left[i]
                i = i + 1
            else:
                nlist[k] = right[j]
                j = j + 1
            k = k + 1

        # one of the 2 list may still have elements, add those in nlist
        while(i < len(left)):
            nlist[k] = left[i]
            i = i + 1
            k = k + 1

        while(j < len(right)):
            nlist[k] = right[j]
            j = j + 1
            k = k + 1

                     
nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)
