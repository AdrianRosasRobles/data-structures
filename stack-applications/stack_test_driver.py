class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()
    
stack = ArrayStack()

print("Is stack empty?", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", len(stack))
print("Top element:", stack.top())

print("Popped:", stack.pop())
print("Popped:", stack.pop())

print("Top after popping:", stack.top())
print("Current size:", len(stack))
print("Is stack empty?", stack.is_empty())
