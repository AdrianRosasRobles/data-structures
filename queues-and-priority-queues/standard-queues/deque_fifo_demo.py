from collections import deque

fifo_queue = deque(['apple', 'banana', 'orange'])

fifo_queue.append('cherry')

first_item = fifo_queue.popleft()
second_item = fifo_queue.popleft()

print(f"Removed: {first_item}, {second_item}")
print(f"Remaining queue: {list(fifo_queue)}")
