

def findTriplet(nums):

	nums.sort()

	for i in range(len(nums)-1,0,-1):
		
		left = 0
		right = i - 1

		while(left < right):

			c = nums[i]*nums[i]

			a = nums[left]*nums[left]
			b = nums[right]*nums[right]

			c_check = a + b

			if(c == (c_check)):
				print(a,b,c)
				return True

			elif(c_check > c):
				right = right - 1

			else:
				left = left + 1



nums = [5,6,3,2,4]
print(findTriplet(nums))