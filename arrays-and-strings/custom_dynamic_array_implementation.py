class SimpleDynamicArray:



    def __init__(self):

        self.capacity = 1

        self.size = 0

        self.data = [None] * self.capacity



    def append(self, value):

        if self.size == self.capacity:

            self.resize()

        self.data[self.size] = value

        self.size += 1





    def resize(self):

        print("Resizing from:", self.capacity, "to", self.capacity * 2)

        self.capacity *= 2

        new_data = [None] * self.capacity

        for i in range(self.size):

            new_data[i] = self.data[i]

        self.data = new_data



arr = SimpleDynamicArray()



for i in range(10):

    arr.append(i)
