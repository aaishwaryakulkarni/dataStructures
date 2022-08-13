"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in 
constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack():
	def __init__(self):

		self.stack_arr = []

	def push(self, val):

		if not self.stack_arr:
			self.stack_arr.append((val, val))
		else:
			self.stack_arr.append((val, min(val,self.stack_arr[-1][1])))


	def pop(self):

		if self.stack_arr:
			self.stack_arr.pop()

		else:
			print("Stack is empty! Cannot pop top value!")

	def top(self):

		if self.stack_arr:
			return self.stack_arr[-1][0]
		else:
			print("Stack is empty! Cannot print top value!")
			return


	def getMin(self):

		if self.stack_arr:
			return self.stack_arr[-1][1]
		else:
			print("Stack is empty! Cannot return minimum value!")


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())    
print(minStack.getMin())