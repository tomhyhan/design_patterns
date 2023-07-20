from abc import abstractmethod, ABC
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

    
class Red(Color):
    def apply_color(self):
        return "Red"


class Blue(Color):
    def apply_color(self):
        return "Blue"
    

class Shape(ABC):
    def __init__(self, color = None):
        self.color = color

    def draw(self):
        color = None
        if self.color is None:
            color = "Black" 
        else:
            color = self.color.apply_color()
        return color 

    
class Circle(Shape):
    def draw(self):
        color = super().draw()
        print(f"Drawing {color} Circle")  
        

class Sqaure(Shape):
    def draw(self):
        color = super.draw()
        return f"Drawing {self.color.apply_color()} Sqaure" 

    
def client_code(shape):
    shape.draw()
    pass

if __name__ == "__main__":
    red = Red()
    circle = Circle()
    client_code(circle)