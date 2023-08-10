class Prototype:
    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        self.objects[name] = obj

    def unregister_object(self, name):
        del self.objects[name]

    def clone(self, name, **kwargs):
        obj = self.objects.get(name)
        if obj:
            cloned_obj = obj.clone(**kwargs)
            return cloned_obj
        else:
            raise ValueError(f"Object with name '{name}' does not exist.")

class ConcreteObject:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def clone(self, **kwargs):
        x = kwargs.get('x', self.x)
        y = kwargs.get('y', self.y)
        color = kwargs.get('color', self.color)
        obj = self.__class__(x, y, color)
        return obj

# Usage example
prototype = Prototype()

# Create an initial object and register it
initial_object = ConcreteObject(0, 0, 'red')
prototype.register_object('object1', initial_object)

# Clone the object with modified properties
cloned_object = prototype.clone('object1', x=10, color='blue')

# Output the properties of the cloned object
print(cloned_object.x)  # Output: 10
print(cloned_object.y)  # Output: 0
print(cloned_object.color)  # Output: blue

# Try to clone an unregistered object
try:
    cloned_object = prototype.clone('object2', x=5, color='green')
except ValueError as err:
    print(str(err))  # Output: Object with name 'object2' does not exist.
