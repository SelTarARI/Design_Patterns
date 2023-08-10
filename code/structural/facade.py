# Subsystem 1
class Subsystem1:
    def method1(self):
        print("Subsystem 1: Method 1")

    def method2(self):
        print("Subsystem 1: Method 2")


# Subsystem 2
class Subsystem2:
    def method1(self):
        print("Subsystem 2: Method 1")

    def method2(self):
        print("Subsystem 2: Method 2")


# Facade
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        self.subsystem1.method1()
        self.subsystem1.method2()
        self.subsystem2.method1()
        self.subsystem2.method2()


# Client
def main():
    facade = Facade()
    facade.operation()


if __name__ == "__main__":
    main()
