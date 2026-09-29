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

def check_brackets(expression):
    stack = ArrayStack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        
        elif char in ")]}":
            if stack.is_empty():
                return False
            
            top_element = stack.pop()
            
            if top_element != pairs[char]:
                return False
            
    return stack.is_empty()

print(f"Test 1: {check_brackets('[([])]')} (Expected: True)")
print(f"Test 2: {check_brackets('{[(])}')} (Expected: False)")
print(f"Test 3: {check_brackets('((()))')} (Expected: True)")
print(f"Test 4: {check_brackets('(()')}    (Expected: False)")