from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def area(self):
        print("Area method called")

r = rectangle()
r.area()
