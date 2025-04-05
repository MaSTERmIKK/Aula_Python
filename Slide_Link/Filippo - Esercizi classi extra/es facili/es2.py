"""
🟠 Esercizio 2: Classe "Contatore"
Crea una classe chiamata Contatore che simula un contatore numerico. Deve avere:

un attributo valore, inizializzato a 0

un metodo incrementa() che aumenta valore di 1

un metodo azzera() che riporta valore a 0

un metodo mostra() che stampa il valore corrente

Obiettivo: gestire lo stato di un oggetto con metodi semplici.

"""

class Contatore:
    def __init__(self):
        self.valore = 0
        
    def incrementa(self):
        self.valore += 1
        print("Valore incrementato con successo")
    def azzera(self):
        if self.valore == 0:
            print("Il valore è già uguale a zero, non c'è bisogno di azzerarlo")
        self.valore = 0
        print("Valore azzerato con successo")
        
    def mostra(self):
        print(f"Il valore è: {self.valore}")

c = Contatore()
    
while True:
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