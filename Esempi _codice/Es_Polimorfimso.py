"""
Esempio unificato di polimorfismo in Python:
- Polimorfismo tramite ereditarietà (classe base Animale e sottoclassi Cane, Gatto)
- Polimorfismo con operator overloading (__add__) nella classe Contatore
- Polimorfismo "duck typing" con funzioni che accettano oggetti di tipo diverso
"""

# ==============================================================
# ESEMPIO 1: POLIMORFISMO CON EREDITARIETÀ (Animale, Cane, Gatto)
# ==============================================================

class Animale:
    """
    Classe base (genitore) per tutti i tipi di animali.
    Definisce un metodo 'verso' e un metodo 'descrivi', 
    pensati per essere sovrascritti dalle sottoclassi.
    """
    def __init__(self, nome):
        self.nome = nome
    
    def verso(self):
        """
        Metodo 'placeholder': verrà implementato dalle sottoclassi
        con suoni diversi ('Bau!', 'Miao!', ecc.).
        """
        raise NotImplementedError("Questo metodo deve essere implementato dalla sottoclasse.")
    
    def descrivi(self):
        """
        Descrizione generica di un animale.
        """
        return f"Animale di nome {self.nome}"

class Cane(Animale):
    """
    Sottoclasse di Animale che rappresenta un Cane.
    """
    def verso(self):
        return "Bau!"
    
    def descrivi(self):
        return f"Sono un Cane, mi chiamo {self.nome}"

class Gatto(Animale):
    """
    Sottoclasse di Animale che rappresenta un Gatto.
    """
    def verso(self):
        return "Miao!"
    
    def descrivi(self):
        return f"Sono un Gatto, mi chiamo {self.nome}"

def fai_parlare_animali(animali):
    """
    Funzione che prende una lista di oggetti di tipo 'Animale' (o derivati)
    e invoca i loro metodi in modo polimorfico.
    """
    for animale in animali:
        print(animale.descrivi())
        print("Il verso che faccio:", animale.verso())
        print("---")


# ==============================================================
# ESEMPIO 2: POLIMORFISMO CON OPERATOR OVERLOADING (__add__)
# ==============================================================

class Contatore:
    """
    Classe che mostra il polimorfismo con operator overloading.
    Ridefinisce __add__ per gestire la somma con altri Contatore o numeri.
    """
    def __init__(self, valore=0):
        self.valore = valore
    
    def __add__(self, altro):
        """
        Permette l'uso di 'c1 + c2' o 'c1 + numero'.
        """
        if isinstance(altro, Contatore):
            # Sommiamo i valori di entrambi i contatori
            return Contatore(self.valore + altro.valore)
        elif isinstance(altro, (int, float)):
            # Sommiamo il valore del contatore con un numero
            return Contatore(self.valore + altro)
        else:
            raise TypeError(f"Operatore + non supportato tra Contatore e {type(altro)}")
    
    def __str__(self):
        return f"Contatore({self.valore})"

def esempio_operator_overloading():
    """
    Esempio pratico di come l'overloading (__add__) permetta
    a Contatore di comportarsi in modo polimorfico con diversi tipi.
    """
    c1 = Contatore(10)
    c2 = Contatore(5)
    c3 = c1 + c2        # Somma tra due Contatore
    c4 = c3 + 100       # Somma tra Contatore e un intero
    #c5 = c3 + "100"       # Somma errata non consetita
    print("c1:", c1)
    print("c2:", c2)
    print("c1 + c2 =", c3)
    print("c3 + 100 =", c4)
    #print("c5", c5)



# ==============================================================
# ESEMPIO 3: POLIMORFISMO "DUCK TYPING"
# ==============================================================

def somma_elementi(iterabile):
    """
    Funzione che cerca di "sommare" tutti gli elementi di un iterabile
    (lista, tupla, stringa - in cui avviene concatenazione -, ecc.).
    Questo è un esempio di duck typing:
    se gli oggetti in 'iterabile' supportano l'operatore '+', la funzione funziona.
    """
    risultato = None
    for elem in iterabile:
        if risultato is None:
            risultato = elem
        else:
            risultato += elem
    return risultato

def esempio_duck_typing():
    """
    Esempio di come la funzione 'somma_elementi' 
    si comporta in modo polimorfico a seconda degli oggetti.
    """
    numeri = [1, 2, 3, 4]
    testo_list = ["Hello", " ", "World", "!"]
    stringa = "ABC"  # Ogni carattere sarà 'sommato' (concatenato)
    
    print("\nSomma elementi in list di interi:", numeri, "->", somma_elementi(numeri))
    print("Somma elementi in list di stringhe:", testo_list, "->", somma_elementi(testo_list))
    print("Somma (concatenazione) dei caratteri in:", stringa, "->", somma_elementi(stringa))


# ==============================================================
# FUNZIONE PRINCIPALE
# ==============================================================

def main():
    # Esempio 1: Polimorfismo con ereditarietà
    print("=== ESEMPIO 1: POLIMORFISMO CON EREDITARIETA' (Animale, Cane, Gatto) ===")
    lista_animali = [
        Cane("Fido"),
        Gatto("Micio"),
        Cane("Rex")
    ]
    fai_parlare_animali(lista_animali)
    
   # Sammy = Cane("Samantha")
    fai_parlare_animali([Sammy])

    # Esempio 2: Operator overloading con Contatore
    print("\n=== ESEMPIO 2: POLIMORFISMO CON OPERATOR OVERLOADING (Contatore) ===")
    esempio_operator_overloading()

    # Esempio 3: Duck typing
    print("\n=== ESEMPIO 3: POLIMORFISMO 'DUCK TYPING' ===")
    esempio_duck_typing()

if __name__ == "__main__":
    main()
