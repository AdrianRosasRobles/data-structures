import sys

arr = []

print("Initial Size", sys.getsizeof(arr))

for i in range(20):
    arr.append(i)
    print(f"Length: {len(arr)}, Size in bytes {sys.getsizeof(arr)}")