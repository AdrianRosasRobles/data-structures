class ArrayQueue:
    def _init_(self):
        self._data = [None] * 10
        self._size = 0
        self._front = 0

    def _len_(self):
        return self._size
    
    def is_empty(self):
        return self._size ==0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -=1

    def enqueue(self, e):
        if self._size == len(self._data):
            raise Exception("Queue is full")
        
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._soze +=1
    
