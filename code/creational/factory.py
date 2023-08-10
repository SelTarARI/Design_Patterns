#Define a Factory class
class Creator():
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        if product:
            product.operation()

#Define Factory subclasses
class ConcreteCreator_1(Creator):
    def factory_method(self):
        return Car_1()

class ConcreteCreator_2(Creator):
    def factory_method(self):
        return Car_2()

#Define a Car class
class Car():
    def operation(self):
        pass

#Define Car subclasses
class Car_1(Car):
    def operation(self):
        print("Producing Car_1")

class Car_2(Car):
    def operation(self):
        print("Producing Car_2")

# Example usage
creator = ConcreteCreator_1()
creator.operation()

creator = ConcreteCreator_2()
creator.operation()
