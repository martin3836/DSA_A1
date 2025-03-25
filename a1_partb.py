#    Main Author(s): Vatsal Bhatt
#    Main Reviewer(s):




class SortedList:
	""" 
	Sorted doubly linked list that uses sentinel nodes

	Attributes: 
		front: Sentinel node at the front of the list
		back: Sentinel node at the end of the list
		size: The number of nodes in the list
	"""

	class Node:
		"""
		A node in a doubly linked list
		
		Attributes:
			data: Data stored in the node
			next: Reference to the next Node in the list
			prev: Reference to the previous Node in the list
		"""

		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next 
			self.prev = prev

		def get_data(self):
			"""
			Returns the data stored in the node
			"""
			return self.data

		def get_next(self):
			"""
			Returns the reference to the next node in the list
			"""
			return self.next

		def get_previous(self):
			"""
			Returns the reference to the previous node in the list
			"""
			return self.prev

	def __init__(self):
		self.front = self.Node(None) # Sentinel node at the front
		self.back = self.Node(None, None, self.front) # Sentinel node at the end
		self.front.next = self.back
		self.size = 0

	def get_front(self):
		"""
		Returns the first data node in the list
		"""
		if self.size > 0:
			return self.front.next
		else: 
			return None

	def get_back(self):
		"""
		Returns the last data node in the list
		"""
		if self.size > 0:
			return self.back.prev
		else:
			return None

	def is_empty(self):
		"""
		Returns: True if the list is empty, False otherwise
		"""
		return self.size == 0

	def __len__(self):
		"""
		Returns the number of data nodes in the list
		"""
		return self.size

	def insert(self, data):
		"""
		Inserts a new data node into the list in a sorted order

		Params: 
			data: Data to be inserted into the list
		Returns:
			Refernce to the newly inserted node
		"""
		new_node = self.Node(data)
		current = self.front.next
		while current != self.back and current.data < data:
			current = current.next
		
		new_node.next = current
		new_node.prev = current.prev
		current.prev.next = new_node
		current.prev = new_node
		self.size += 1
		return new_node

	def erase(self, node):
		"""
		Removes a given node from list

		Params:
			node: the node to be removed

		Returns: ValueError if node cannot be found
		"""
		if node is None or node == self.front or node == self.back:
			raise ValueError('Cannot erase node referred to by None')
		
		node.prev.next = node.next
		node.next.prev = node.prev
		self.size -= 1

	def search(self, data):
		"""
		Searches the list for the node with specified data

		Params:
			data: Data to search for
		Returns: Refernce to the node containing data, if found; None, Otherwise
		"""
		current = self.front.next
		while current != self.back:
			if current.data == data:
				return current
			current = current.next

		return None