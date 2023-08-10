class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    #This is an example of object composition.
    #To adapt with inheritance we take Adaptee as an argument, and we will not need an initiator (constructor).
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    #Client code is crucial (requests can change) but the target interface must be met.
    try:
        print(target.request(), end="")
    except AttributeError as error:
        print(f"Error: {error}")

#Usage Examples

# Example 1: Using the Target directly
print("Example 1: Using the Target directly")
target = Target()
client_code(target)
# Output: Target: The default target's behavior.

# Example 2: Using the Adapter to translate Adaptee's specific_request
print("\nExample 2: Using the Adapter to translate Adaptee's specific_request")
adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)
# Output: Adapter: (TRANSLATED) Special behavior of Adaptee.

# Example 3: Using the Adapter with a different Adaptee instance
print("\nExample 3: Using the Adapter with a different Adaptee instance")
adaptee2 = Adaptee()
adapter2 = Adapter(adaptee2)
client_code(adapter2)
# Output: Adapter: (TRANSLATED) Special behavior of Adaptee.

# Example 4: Using the Adaptee directly
print("\nExample 4: Using the Adaptee directly")
adaptee3 = Adaptee()
try:
    client_code(adaptee3)
except AttributeError as error:
    print(f"Error: {error}")
# Output: Error: 'Adaptee' object has no attribute 'request'
