from typing import Union

# Define the strategies

class Strategy:
    def do_operation(self, num1, num2):
        pass

class AddStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2

class SubtractStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2

class MultiplyStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 * num2


# Define the context

class Context:
    def __init__(self, strategy: Union[AddStrategy, SubtractStrategy, MultiplyStrategy]):
        self.strategy = strategy

    def execute_strategy(self, num1, num2):
        return self.strategy.do_operation(num1, num2)


# Usage

# Create the strategies
add_strategy = AddStrategy()
subtract_strategy = SubtractStrategy()
multiply_strategy = MultiplyStrategy()

# Create the context with the desired strategy
context = Context(add_strategy)

# Execute the strategy
result = context.execute_strategy(5, 3)
print("Result:", result)  # Output: 8

# Change the strategy dynamically
context.strategy = subtract_strategy
result = context.execute_strategy(5, 3)
print("Result:", result)  # Output: 2

# Change the strategy again
context.strategy = multiply_strategy
result = context.execute_strategy(5, 3)
print("Result:", result)  # Output: 15
