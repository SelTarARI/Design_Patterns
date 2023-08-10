class State:
    def do_action(self, context):
        pass


class StateA(State):
    def do_action(self, context):
        print("State A action")
        context.state = StateB()


class StateB(State):
    def do_action(self, context):
        print("State B action")
        context.state = StateC()


class StateC(State):
    def do_action(self, context):
        print("State C action")
        context.state = StateA()


class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        self.state.do_action(self)


# Usage example
context = Context()
context.request()
context.request()
context.request()
