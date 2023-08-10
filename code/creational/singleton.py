class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a Singleton!")


# Example usage with try-except block:

try:
    # Creating instances of the Singleton class
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    print(s1 is s2)  # Output: True

    # Trying to create a new instance raises an exception
    s3 = Singleton()  # Raises an exception: This class is a Singleton!

except Exception as e:
    print("Error:", str(e))
