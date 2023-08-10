# Implementing the Abstraction class
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


# Implementing the Concrete Implementor classes
class RedColor:
    def fill_color(self):
        return "Red"


class BlueColor:
    def fill_color(self):
        return "Blue"


# Implementing the Refined Abstraction classes
class Circle(Shape):
    def draw(self):
        return f"Drawing Circle with {self.color.fill_color()} color"


class Square(Shape):
    def draw(self):
        return f"Drawing Square with {self.color.fill_color()} color"


# Example usage
red_color = RedColor()
blue_color = BlueColor()

circle = Circle(red_color)
print(circle.draw())  # Output: Drawing Circle with Red color

square = Square(blue_color)
print(square.draw())  # Output: Drawing Square with Blue color
