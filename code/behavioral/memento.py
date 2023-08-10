class Originator:
    #user interface for changing and restoring states
    def __init__(self):
        self._state = None
        self._caretaker = Caretaker()
    
    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state
        self._caretaker.add_memento(Memento(self._state))
    
    def restore_state(self, index):
        memento = self._caretaker.get_memento(index)
        self._state = memento.get_state()
        print(f"State restored to: {self._state}")


class Memento:
    #is a container that stores states
    def __init__(self, state):
        self._state = state
    
    def get_state(self):
        return self._state


class Caretaker:
    #keeps track of the stored data of states
    def __init__(self):
        self._mementos = []
    
    def add_memento(self, memento):
        self._mementos.append(memento)
    
    def get_memento(self, index):
        return self._mementos[index]


# Usage example
originator = Originator()

originator.set_state("State 1")
originator.set_state("State 1")
originator.set_state("State 1")

originator.restore_state(2)
