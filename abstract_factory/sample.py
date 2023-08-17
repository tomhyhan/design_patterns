from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod    
    def create_product_b(self):
        pass
    
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()
    
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass
    
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass
    
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA):
        pass
    
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the {result}"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductB):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the {result}"

def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")
if __name__ == "__main__":
    factory_a = ConcreteFactory1()
    client_code(factory_a)