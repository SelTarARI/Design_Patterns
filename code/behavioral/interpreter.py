# Abstract Expression
class Expression:
    def interpret(self, context):
        pass

# Terminal Expression
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# Terminal Expression
class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Context
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable(self, variable):
        return self.variables.get(variable)

# Usage
# Create the syntax tree: 5 + (6 + 7)
expression = Plus(Number(5), Plus(Number(6), Number(7)))

# Create the context
context = Context()

# Set variables if needed
context.set_variable('x', 10)
context.set_variable('y', 20)

# Interpret the expression
result = expression.interpret(context)
print(f"Result: {result}")
