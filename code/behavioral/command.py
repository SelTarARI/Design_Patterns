# Receiver class
class Light:
    def turn_on(self):
        print("Light is on.")

    def turn_off(self):
        print("Light is off.")


# Command interface
class Command:
    def execute(self):
        pass


# Concrete command classes
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Invoker class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command is not None:
            self.command.execute()
        else:
            print("No command is set.")


# Client code
if __name__ == "__main__":
    # Create receiver object
    light = Light()

    # Create command objects
    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    # Create invoker object
    remote = RemoteControl()

    # Set commands for the remote
    remote.set_command(turn_on_command)

    # Press the button on the remote
    remote.press_button()  # Light is on.

    # Set a different command
    remote.set_command(turn_off_command)

    # Press the button again
    remote.press_button()  # Light is off.

    # Press the button without setting a command
    remote.set_command(None)
    remote.press_button()  # No command is set.
