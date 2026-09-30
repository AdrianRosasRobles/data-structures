import time

arr = []
start = time.time()

for i in range(100000):
    arr.append(i)

end = time.time()
print("Append time:", end - start)

arr = []
start = time.time()

for i in range(100000):
    arr.insert(0, i)

end = time.time()
print("Insert at beginning time:", end - start)
