# Define the base component interface
class Component:
    def operation(self):
        pass

# Concrete component
class ConcreteComponent(Component):
    def operation(self):
        print("Performing the operation in the concrete component.")

# Base decorator class
class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

# Concrete decorator class
class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        self.additional_operation()

    def additional_operation(self):
        print("Adding additional operation in ConcreteDecoratorA.")

# Another concrete decorator class
class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        self.additional_operation()

    def additional_operation(self):
        print("Adding additional operation in ConcreteDecoratorB.")

# Usage
if __name__ == "__main__":
    # Create a concrete component
    component = ConcreteComponent()

    # Create decorators and wrap the component
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)

    # Call the operation
    decorator_b.operation()
