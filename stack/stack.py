"""
Stack in Python can be implemented using following ways:

list
collections.deque
queue.LifoQueue

"""


# from collections import deque 

# stack = deque() 

# stack.append('a') 
# stack.append('b') 
# stack.append('c') 
  
# print('Initial stack:') 
# print(stack) 
 
# print('\nElements poped from stack:') 
# print(stack.pop()) 
# print(stack.pop()) 
# print(stack.pop()) 

# print('\nStack after elements are poped:') 
# print(stack) 


"""
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using put() function and get() takes data out from the Queue.
There are various functions available in this module:

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.
"""

from queue import LifoQueue 
  
# Initializing a stack 
stack = LifoQueue(maxsize = 3) 
  
# qsize() show the number of elements 
# in the stack 
print(stack.qsize()) 
   
# put() function to push 
# element in the stack 
stack.put('a') 
stack.put('b') 
stack.put('c') 
  
print("Full: ", stack.full())  
print("Size: ", stack.qsize())  

# stack.put('d')
  
print('\nElements popped from the stack') 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 
  
print("\nEmpty: ", stack.empty()) 
