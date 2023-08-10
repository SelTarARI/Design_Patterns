class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        print(value)  # Print the value inside the iterator
        return value


# Example usage
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for my_list in my_iterator:
    pass  # Iterate over the items without storing the values explicitly
