class Car():
    def __init__(self) -> None:
        self.options = []
    
    def add(self, option) -> None:
        self.options.append(option)
    

class Builder():
    def __init__(self) -> None:
        self.car=Car()

    def option_A(self) -> None:
        self.car.add("option_A")
        print("Car has option A")

    def option_B(self) -> None:
        self.car.add("option_B")
        print("Car has option B")
        
    def option_C(self) -> None:
        self.car.add("option_C")
        print("Car has option C")

if __name__ == '__main__':
    car=Builder()
    car.option_A()

    