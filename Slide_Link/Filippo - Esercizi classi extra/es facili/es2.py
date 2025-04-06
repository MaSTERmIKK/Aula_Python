#🟠 Esercizio 2: Classe "Contatore"

class Contatore:
    def __init__(self): # costruttore che non accetta parametri esterni
        self.valore = 0
        
    def incrementa(self): # funzione per incrementare il valore
        self.valore += 1
        print("Valore incrementato con successo")
        
    def azzera(self):
        if self.valore == 0: # verifica che il valore sia già uguale a 0 prima di azzerare
            print("Il valore è già uguale a zero, non c'è bisogno di azzerarlo")
        self.valore = 0
        print("Valore azzerato con successo")
        
    def mostra(self): # mostra il valore 
        print(f"Il valore è: {self.valore}")

c = Contatore() # istanzia un oggetto senza passarne parametri
    
while True: # menù per chiedere all'utente cosa fare
    whatdo = int(input("Cosa vuoi fare?\nIncrementare di uno il valore del contatore (1)\nAzzerare il valore del contatore (2)\nMostrare il valore del contatore (3)\nUscire (4)\n"))
    match whatdo:
        case 1:
            c.incrementa()
        case 2:
            c.azzera()
        case 3:
            c.mostra()
        case 4:
            break
        case _:
            break