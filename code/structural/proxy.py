from abc import ABC, abstractmethod


# Subject interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# RealSubject class
class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")


# Proxy class
class ProxyImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()


# Usage example
if __name__ == "__main__":
    image1 = ProxyImage("image1.jpg")
    image1.display()  # The image will be loaded and displayed

    print("---")

    image2 = ProxyImage("image2.jpg")
    image2.display()  # The image will be loaded and displayed (not loaded again)
