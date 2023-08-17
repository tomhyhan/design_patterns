class Coffee:
    def get_cost(self):
        pass
    
    def get_description(self):
        pass
    
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 5
    
    def get_description(self):
        return "Simple Coffee"
    
class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self._decorated_coffee = decorated_coffee
        
    def get_cost(self):
        return self._decorated_coffee.get_cost()
    
    def get_description(self):
        return self._decorated_coffee.get_description()

class Milk(CoffeeDecorator):
    def get_cost(self):
        return self._decorated_coffee.get_cost() + 2
    
    def get_description(self):
        return self._decorated_coffee.get_description() + "+Milk"

class Sugar(CoffeeDecorator):
    def get_cost(self):
        return self._decorated_coffee.get_cost() + 1
    
    def get_description(self):
        return self._decorated_coffee.get_description() + "+Sugar"
    
    
    
def decorator(fn):
    def wrapper():
        print("start")
        fn()
        print("end")
    return wrapper
    
@decorator
def hello():
    print("hello")

if __name__ == "__main__":
    # class
    simple_coffee = SimpleCoffee()
    coffee_with_milk_and_sugar = Sugar(Milk(simple_coffee))
    print(coffee_with_milk_and_sugar.get_description())
    hello()
