#    Main Author(s): Martin Mathew Roy
#    Main Reviewer(s):



class Stack:
    
    def __init__(self, cap=10): 
        #initialization of Stack class data members, with a default capacity of 10 
        self._data = [None] * cap
        self._capacity = cap
        self._size = 0

    def capacity(self):
        #This function returns capacity.
        return self._capacity

    def push(self, data):
        #This function adds data to the top of the Stack. A resizing operation whould take place in this function if number of items stored to exceed the current capacity
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = data
        self._size += 1

    def pop(self):
        #This function removes the value at the top of the Stack and return the removed value. It raises an IndexError is this function is used on an empty Stack
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        self._size -= 1
        return self._data[self._size]

    def get_top(self):
        #This function returns the the newest value from the Stack without removing it. It returns None if the stack is empty
        if self.is_empty():
            return None
        return self._data[self._size - 1]

    def is_empty(self):
        #This function checks if the Stack is empty or not. Retruns True if empty, and False otherwise
        return self._size == 0

    def __len__(self):
        #This function returns the length of the stack
        return self._size

    def _resize(self):
        #This function is used to counter the sizing problem in the Stack. This is basically used to double the capacity, which is set to twice the current capacity. 
        #A new list (new_data) is created with the updated capacity, filled with None values initially.
        #The existing elements in the stack are copied from the old list (self._data) to the new list (new_data). This preserves the current elements of the stack.
        #The old list (self._data) is replaced with the new list (new_data). The capacity of the stack is also updated to the new capacity (self._capacity = new_capacity).
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity



class Queue:
    
    def __init__(self, cap=10):
        #initialization of Stack class data members, with a default capacity of 10 
        self._data = [None] * cap
        self._capacity = cap
        self._size = 0
        self._front = 0

    def capacity(self):
        #This function returns capacity.
        return self._capacity

    def enqueue(self, data):
        #This function adds data to the back of the Queue. A resizing operation whould take place in this function if number of items stored to exceed the current capacity
        if self._size == self._capacity:
            self._resize()
        index = (self._front + self._size) % self._capacity
        self._data[index] = data
        self._size += 1

    def dequeue(self):
        #This function removes the value at the end of the Queue and return the removed value. It raises an IndexError is this function is used on an empty Queue
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        front_element = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return front_element

    def get_front(self):
        #This function returns the the oldest value from the Queue without removing it. It returns None if the Queue is empty
        if self.is_empty():
            return None
        return self._data[self._front]

    def is_empty(self):
        #This function checks if the Queue is empty or not. Retruns True if empty, and False otherwise
        return self._size == 0

    def __len__(self):
        #This function returns the length of the stack
        return self._size
        
    def _resize(self):
        #This function is used to counter the sizing problem in the Queue. This is basically used to double the capacity, which is set to twice the current capacity. 
        #A new list (new_data) is created with the updated capacity, filled with None values initially.
        #The existing elements in the stack are copied from the old list (self._data) to the new list (new_data). This preserves the current elements of the stack.
        #The old list (self._data) is replaced with the new list (new_data). The self._front is reset to 0 because the elements are now placed starting from the beginning of new_data, and the self._capacity is updated to new_capacity. The capacity of the stack is also updated to the new capacity (self._capacity = new_capacity).
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_capacity



class Deque:
    
    def __init__(self, cap=10):
        #initialization of Deque class data members, with a default capacity of 10 
        self._data = [None] * cap
        self._capacity = cap
        self._size = 0
        self._front = 0

    def capacity(self):
        #This function returns capacity.
        return self._capacity

    def push_front(self, data):
        #This function adds data to the front of the Deque.
        if self._size == self._capacity:
            self._resize()
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = data
        self._size += 1


    def pop_front(self):
        #This function removes the value from the front of the Deque.
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        front_element = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return front_element

    def push_back(self, data):
        #This function adds data to the back of the Deque.
        if self._size == self._capacity:
            self._resize()
        index = (self._front + self._size) % self._capacity
        self._data[index] = data
        self._size += 1

    def pop_back(self):
        #This function removes the value from the back of the Deque.
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        back_index = (self._front + self._size - 1) % self._capacity
        back_element = self._data[back_index]
        self._size -= 1
        return back_element

    def get_front(self):
        #This function returns the value from the front of the Deque without removing it. 
        if self.is_empty():
            return None
        return self._data[self._front]

    def get_back(self):
         #This function returns the value from the back of the Deque without removing it.
        if self.is_empty():
            return None
        back_index = (self._front + self._size - 1) % self._capacity
        return self._data[back_index]

    def is_empty(self):
        #This function returns True if Deque is empty, False otherwise.
        return self._size == 0

    def __len__(self):
        #This function returns the number of values in the Deque. 
        return self._size

    def __getitem__(self, k):
        #This function returns the k'th value from the "front" of the Deque without removing it
        if k < 0 or k >= self._size:
            raise IndexError('Index out of range')
        return self._data[(self._front + k) % self._capacity]

    def _resize(self):
        #This function is used to counter the sizing problem in the Deueue. This is basically used to double the capacity, which is set to twice the current capacity. 
        #A new list (new_data) is created with the updated capacity, filled with None values initially.
        #The existing elements in the stack are copied from the old list (self._data) to the new list (new_data). This preserves the current elements of the stack.
        #The old list (self._data) is replaced with the new list (new_data). The self._front is reset to 0 because the elements are now placed starting from the beginning of new_data, and the self._capacity is updated to new_capacity. The capacity of the stack is also updated to the new capacity (self._capacity = new_capacity).
        new_capacity = self._capacity * 2
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_capacity
