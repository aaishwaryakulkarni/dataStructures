"""
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that 
only push to back, peek/pop from front, size and is empty operations 
are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue) 
as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Approach:
We will use deque. It can be used as a stack or a queue.
So we will use it as a queue but write logic to make it work as a stack.

We will use normal append.
We will use popleft as its a queue
We will use queue[0] as top() as its a queue

push(1):
deque = 1

push(2):
deque = 1-2
now popleft and add it to stack again
deque = 2-1

push(3):
deque = 2-1-3
now popleft 2 times and add it to stack again
deque = 1-3-2 (1st time)
deque = 3-2-1 (2nd time)


"""
import collections
class MyStack:

	def __init__(self):
		self.queue = collections.deque()

	def pop(self):
		if len(self.queue) !=0:
			self.queue.popleft()
		else:
			print("No elements to pop!")

	def top(self):
		if len(self.queue) !=0:
			return self.queue[0]
		print("No element in stack!")

	def push(self, val):
		self.queue.append(val)

		for i in range(len(self.queue) - 1):
			self.queue.append(self.queue.popleft())

	def empty(self):
		return not len(self.queue)


myStack = MyStack();
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
print(myStack.top())
myStack.pop()
print(myStack.top())
myStack.empty()