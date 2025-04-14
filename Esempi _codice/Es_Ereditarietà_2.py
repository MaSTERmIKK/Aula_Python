class Base:
    def __new__(cls, *args, **kwargs):
        # __new__ is called to create a new instance
        print(f"Creating instance of {cls.__name__} using __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        # Standard initializer
        print(f"Initializing {self.__class__.__name__}")

    def greet(self):
        print("Hello from Base")

    def __init_subclass__(cls, **kwargs):
        # Called when a class inherits from Base
        print(f"Initializing subclass {cls.__name__} from Base using __init_subclass__")
        super().__init_subclass__(**kwargs)


class Derived1(Base):
    def greet(self):
        print("Hello from Derived1")
        # Using super() to call the parent class method
        super().greet()


class Derived2(Base):
    def greet(self):
        print(" -")
        print("Hello from Derived2")
        


class Combined(Derived1, Derived2):
    def greet(self):
        print("Hello from Combined")
        # This will call the next method in the MRO
        super().greet()

  
if __name__ == '__main__':
    # Visualizzare il Method Resolution Order (MRO)
    print("Method Resolution Order (MRO) per Combined:")
    print(Combined.__mro__)
    print()

    # Visualizzare le classi base di Derived1
    print("Classi base (bases) di Derived1:")
    print(Derived1.__bases__)
    print()

    # Visualizzare le sottoclassi immediate di Base
    print("Sottoclassi immediate di Base:")
    print(Base.__subclasses__())
    print()

    # Creare un'istanza della classe Combined che attiva __new__ e __init__
    obj = Combined()
    print()

    # Chiamata al metodo greet() che utilizza super() e la MRO
    obj.greet()
    print()

    # Utilizzo di isinstance e issubclass
    print("Verifica con isinstance e issubclass:")
    print("obj è un'istanza di Derived1?", isinstance(obj, Derived1))
    print("obj è un'istanza di Base?", isinstance(obj, Base))
    print("Combined è una sottoclasse di Derived2?", issubclass(Combined, Derived2))
