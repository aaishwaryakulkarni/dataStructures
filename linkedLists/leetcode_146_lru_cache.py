"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Approach:

LRU (self.left)  MRU (self.right)

"""

class Node:

	def __init__(self, key, value):

		self.key = key
		self.value = value
		self.prev = None
		self.right = None

class LRUCache:
	
	def __init__(self,capacity):

		self.capacity = capacity
		self.dict_map = {}

		#left node for LRU, right node for MRU
		self.left = Node(0, 0)
		self.right = Node(0, 0)

		#at start left's next is right and right's prev is left
		self.left.next = self.right
		self.right.prev = self.left

	def remove(self, node):

		prev = node.prev
		nxt = node.next

		prev.next = nxt
		nxt.prev = prev

	def insert(self, node):

		prev = self.right.prev
		nxt = self.right

		prev.next = node
		nxt.prev = node

		node.prev = prev
		node.next = nxt


	def get(self, key):

		if key in self.dict_map:

			#remove the node and insert it to right i.e MRU side
			self.remove(self.dict_map[key])
			self.insert(self.dict_map[key])

			return self.dict_map[key].value

		else:
			return -1

	def put(self, key, value):

		if key in self.dict_map:
			self.remove(self.dict_map[key])

		self.dict_map[key] = Node(key, value)
		self.insert(self.dict_map[key])

lRUCache = LRUCache(2)
lRUCache.put(1, 1); 
lRUCache.put(2, 2); 
lRUCache.get(1);    
lRUCache.put(3, 3); 
lRUCache.get(2);    
lRUCache.put(4, 4); 
lRUCache.get(1);    
lRUCache.get(3);    
lRUCache.get(4);    