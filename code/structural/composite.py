from abc import ABC, abstractmethod

# Abstract base class for components
class Component:
    def operation(self):
        pass

# Leaf component
class Leaf(Component):
    def operation(self):
        print("Leaf operation")

# Composite component
class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        print("Composite operation")
        for child in self._children:
            child.operation()

# Client code
if __name__ == "__main__":
    # Create leaf components
    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()

    # Create a composite component
    composite = Composite()

    # Add leaf components to the composite
    composite.add(leaf1)
    composite.add(leaf2)

    # Create another composite component
    composite2 = Composite()

    # Add a leaf and the first composite component to the second composite
    composite2.add(leaf3)
    composite2.add(composite)

    # Call operations on the composite, which in turn calls operations on its children
    composite.operation()
    print("-----------")
    composite2.operation()
