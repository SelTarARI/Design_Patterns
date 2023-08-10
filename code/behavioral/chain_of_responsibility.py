class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandlerA handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandlerB handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("ConcreteHandlerC handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)


# Usage example
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_c = ConcreteHandlerC()

handler_a._successor = handler_b
handler_b._successor = handler_c

handler_a.handle_request('B')
