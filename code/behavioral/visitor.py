# Define the Visitor interface
class Visitor:
    def visit(self, element):
        pass

# Define the elements that can be visited
class ElementA:
    def accept(self, visitor):
        visitor.visit(self)

class ElementB:
    def accept(self, visitor):
        visitor.visit(self)

# Define concrete visitors
class ConcreteVisitor1(Visitor):
    def visit(self, element):
        print("ConcreteVisitor1 visiting", element.__class__.__name__)

class ConcreteVisitor2(Visitor):
    def visit(self, element):
        print("ConcreteVisitor2 visiting", element.__class__.__name__)

# Example usage
elements = [ElementA(), ElementB()]
visitors = [ConcreteVisitor1(), ConcreteVisitor2()]

for element in elements:
    for visitor in visitors:
        element.accept(visitor)
