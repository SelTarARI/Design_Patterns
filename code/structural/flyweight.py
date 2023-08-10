class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight: shared state({self.shared_state}) and unique state({unique_state})")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]


if __name__ == '__main__':
    factory = FlyweightFactory()

    flyweight1 = factory.get_flyweight("Shared State 1")
    flyweight1.operation("Unique State 1")

    flyweight2 = factory.get_flyweight("Shared State 1")
    flyweight2.operation("Unique State 2")

    flyweight3 = factory.get_flyweight("Shared State 2")
    flyweight3.operation("Unique State 3")
