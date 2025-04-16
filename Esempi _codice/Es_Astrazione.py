"""
Esempio di astrazione in Python:
- Uso del modulo abc (Abstract Base Class)
- Classe astratta Shape con metodi astratti area() e perimetro()
- Sottoclassi Circle e Rectangle che implementano i metodi astratti
- Funzione che sfrutta il polimorfismo sulle classi astratte
"""

import math
from abc import ABC, abstractmethod

# ==============================================================
# CLASSE ASTRATTA
# ==============================================================

# classe astratta
class Shape(ABC):
    """
    Classe astratta (non istanziabile direttamente) che rappresenta
    una figura geometrica generica. Definisce i metodi area() e perimetro()
    come astratti, obbligando le sottoclassi a implementarli.
    """
    @abstractmethod
    def area(self):
        """
        Restituisce l'area della figura geometrica.
        (Da implementare nelle sottoclassi.)
        """
        pass

    @abstractmethod
    def perimetro(self):
        """
        Restituisce il perimetro della figura geometrica.
        (Da implementare nelle sottoclassi.)
        """
        pass
    
    # metodi reale, metodo di istanza
    def descrivi(self):
        """
        Metodo facoltativo (non astratto) che può essere usato, sovrascritto
        o esteso dalle sottoclassi, se desiderato.
        """
        return "Sono una forma geometrica."


# ==============================================================
# SOTTOCLASSI CHE IMPLEMENTANO L'ASTRAZIONE
# ==============================================================

class Circle(Shape):
    """
    Sottoclasse di Shape che rappresenta un cerchio.
    Deve implementare area() e perimetro() definiti come astratti.
    """
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * (self.raggio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raggio

    def descrivi(self):
        """
        Sovrascrive descrivi() per aggiungere info sul raggio del cerchio.
        """
        return f"Sono un Cerchio con raggio={self.raggio:.2f}"


class Rectangle(Shape):
    """
    Sottoclasse di Shape che rappresenta un rettangolo.
    """
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza

    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)

    def descrivi(self):
        return f"Sono un Rettangolo con larghezza={self.larghezza} e altezza={self.altezza}"


# ==============================================================
# FUNZIONI DI ESEMPIO
# ==============================================================

def stampa_info_shape(shape_obj):
    """
    Funzione che accetta un oggetto di tipo Shape (o derivato) e ne stampa le info:
    - descrizione
    - area
    - perimetro
    """
    print(shape_obj.descrivi())
    print(f"Area: {shape_obj.area():.2f}")
    print(f"Perimetro: {shape_obj.perimetro():.2f}")
    print("---")


def main():
    # Non possiamo istanziare Shape direttamente, perché è una classe astratta:
    # shape = Shape()  # -> Errore: TypeError: Can't instantiate abstract class

    # Creiamo invece istanze delle sottoclassi concrete:
    circle = Circle(raggio=5)
    rectangle = Rectangle(larghezza=3, altezza=7)

    # Usiamo la stessa funzione polimorfica su oggetti di sottoclassi diverse
    print("=== ESEMPIO DI ASTRATTAZIONE CON SHAPE, CERCHIO E RETTANGOLO ===")
    stampa_info_shape(circle)
    stampa_info_shape(rectangle)


if __name__ == "__main__":
    main()
