class Mediator:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def notify(self, sender, event):
        for component in self.components:
            if component != sender:
                component.receive(event)


class Component:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, event):
        self.mediator.notify(self, event)

    def receive(self, event):
        print(f"Received event: {event}")


# Usage example
mediator = Mediator()

component1 = Component(mediator)
component2 = Component(mediator)
component3 = Component(mediator)

mediator.add_component(component1)
mediator.add_component(component2)
mediator.add_component(component3)

component1.send("Hello from Component 1!")
component2.send("Greetings from Component 2!")
component3.send("Salutations from Component 3!")
