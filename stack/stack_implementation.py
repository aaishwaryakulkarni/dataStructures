class Stack:
	def __init__(self,size):

		self.stack_arr = []
		self.capacity = size
		self.top = -1

	def push(self, value):

		if self.isFull():
			print(f"Stack is full, cannot push element {value}!")
			return

		self.top = self.top + 1
		self.stack_arr.append(value)

		print(f"Inserted element {value} into stack.")

	def pop(self):

		if self.isEmpty():
			print("Stack is empty, cannot pop element!")
			return

		popped = self.stack_arr[-1]

		#del(self.stack_arr[-1])
		self.stack_arr.pop()

		self.top = self.top - 1

		print(f"Removed element {popped} from stack.")

	def size(self):
		return self.top + 1

	def isFull(self):
		return self.size() == self.capacity

	def isEmpty(self):
		return self.size() == 0


mystack = Stack(5)
mystack.pop()
mystack.push(5)
mystack.push(2)
mystack.push(7)
mystack.push(1)
mystack.push(0)
mystack.push(19)
mystack.pop()
mystack.push(19)