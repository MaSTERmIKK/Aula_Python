
"""
Esempi unificati di polimorfismo e utilizzo di classi in Python:
- classi semplici con __str__
- ereditarietà e polimorfismo (Animale, Cane, Gatto)
- dizionari contenenti istanze di classi diverse
- operator overloading (__add__) con la classe Contatore
- differenza tra __str__ e __repr__ (classe Punto)
"""

# ==============================================================
# ESEMPIO 1: CLASSE 'Persona' CON METODO __str__
# ==============================================================

class Persona:
    """
    Rappresenta una persona, con nome ed età.
    Il metodo __str__ restituisce una stringa descrittiva dell'oggetto.
    """
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def __str__(self):
        # Viene richiamato quando facciamo: print(istanza_di_Persona)
        return f"Persona(nome={self.nome}, eta={self.eta})"


# ==============================================================
# ESEMPIO 2: CLASSI PER IL POLIMORFISMO (Animale, Cane, Gatto)
# ==============================================================

class Animale:
    """
    Classe base (genitore) per vari tipi di animali.
    Definisce un metodo astratto 'verso' e un __str__ generico.
    """
    def __init__(self, nome):
        self.nome = nome
    
    def verso(self):
        """
        Metodo che dovrebbe essere implementato dalle sottoclassi.
        """
        raise NotImplementedError("Implementare il metodo 'verso' nella sottoclasse.")
    
    def __str__(self):
        """
        Restituisce una descrizione generica di un animale.
        """
        return f"Animale(nome={self.nome})"


class Cane(Animale):
    """
    Sottoclasse che estende Animale per rappresentare un Cane.
    """
    def verso(self):
        return "Bau!"
    
    def __str__(self):
        # Overriding del metodo __str__
        return f"Cane(nome={self.nome})"


class Gatto(Animale):
    """
    Sottoclasse che estende Animale per rappresentare un Gatto.
    """
    def verso(self):
        return "Miao!"
    
    def __str__(self):
        # Overriding del metodo __str__
        return f"Gatto(nome={self.nome})"


# ==============================================================
# ESEMPIO 3: UTILIZZO DI OGGETTI IN DIZIONARI, CICLI E CONDIZIONI
# ==============================================================

def esempio_dizionario_animali():
    """
    Crea un dizionario di animali (Cane e Gatto),
    itera sulle voci e mostra il polimorfismo di 'verso()'.
    """
    animali_domestici = {
        "Fido": Cane("Fido"),
        "Luna": Gatto("Luna"),
        "Miao": Gatto("Miao"),
        "Rex":  Cane("Rex")
    }
    
    for nome, animale in animali_domestici.items():
        print(f"Chiave: {nome} -> Oggetto:", animale)
        print("Verso:", animale.verso())  # Polimorfismo
        if isinstance(animale, Gatto):
            print("  -> Questo è un Gatto, si dice che ami le coccole a modo suo...")
        elif isinstance(animale, Cane):
            print("  -> Questo è un Cane, si dice che ami giocare con la palla...")
        print("---")


# ==============================================================
# ESEMPIO 4: OPERATOR OVERLOADING (__add__) CON LA CLASSE 'Contatore'
# ==============================================================

class Contatore:
    """
    Classe che tiene traccia di un contatore (valore numerico).
    Esempio di operator overloading su __add__.
    """
    def __init__(self, valore=0):
        self.valore = valore
    
    def __add__(self, altro):
        """
        Permette di usare l'operatore + tra due Contatore o
        tra un Contatore e un numero (int, float).
        """
        if isinstance(altro, Contatore):
            return Contatore(self.valore + altro.valore)
        elif isinstance(altro, (int, float)):
            return Contatore(self.valore + altro)
        else:
            raise TypeError(f"Operazione non supportata tra Contatore e {type(altro)}")
    
    def __str__(self):
        return f"Contatore(valore={self.valore})"


# ==============================================================
# ESEMPIO 5: __str__ VS __repr__ (classe 'Punto')
# ==============================================================

class Punto:
    """
    Rappresenta un punto 2D con coordinate x, y.
    Mostra la differenza tra __repr__ e __str__.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        # Usata ad esempio nella shell o in contesti di debug
        return f"Punto(x={self.x}, y={self.y})"
    
    def __str__(self):
        # Usata con print() per una rappresentazione più user-friendly
        return f"({self.x}, {self.y})"


# ==============================================================
# FUNZIONE MAIN PER DIMOSTRARE TUTTI GLI ESEMPI
# ==============================================================

def main():
    # Esempio 1: Persona con __str__
    print("===== ESEMPIO 1: Persona con __str__ =====")
    mario = Persona("Mario", 30)
    anna = Persona("Anna", 25)
    print(mario)
    print(anna)
    
    # Esempio 2: Polimorfismo con classi Animale, Cane, Gatto
    print("\n===== ESEMPIO 2: Polimorfismo con Animale, Cane, Gatto =====")
    fido = Cane("Fido")
    luna = Gatto("Luna")
    animali = [fido, luna]
    for animale in animali:
        print(animale, "| Verso:", animale.verso())
    
    # Esempio 3: Dizionario di animali
    print("\n===== ESEMPIO 3: Dizionario di Animali =====")
    esempio_dizionario_animali()
    
    # Esempio 4: Operator overloading con Contatore
    print("\n===== ESEMPIO 4: Operator overloading (Contatore) =====")
    c1 = Contatore(10)
    c2 = Contatore(5)
    c3 = c1 + c2
    c4 = c3 + 100
    print("c1:", c1)
    print("c2:", c2)
    print("c1 + c2 =", c3)
    print("c3 + 100 =", c4)
    
    # Esempio 5: __str__ vs __repr__ con Punto
    print("\n===== ESEMPIO 5: __str__ vs __repr__ (Punto) =====")
    p = Punto(3, 5)
    print("print(p) -> chiama __str__:", p)
    print("repr(p)  -> chiama __repr__:", repr(p))


# ==============================================================
# Avvio dello script (se eseguito come main)
# ==============================================================
if __name__ == "__main__":
    main()
