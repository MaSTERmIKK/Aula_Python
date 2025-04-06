"""
🔵 Esercizio 2: Sistema di gestione prodotti
Crea una classe Prodotto e una classe Magazzino.

Classe Prodotto:
Attributi: nome, prezzo, quantità

Classe Magazzino:
Attributo: prodotti (lista di oggetti Prodotto)

Metodi:

aggiungi_prodotto(prodotto)

valore_totale() → calcola il valore totale del magazzino (somma di prezzo × quantità)

cerca_prodotto(nome) → ritorna il prodotto se esiste, altrimenti un messaggio di errore

Obiettivo: esercitarsi con gestione di liste, ricerca, moltiplicazioni e strutture condizionali.
"""
class Prodotto:
    def __init__(self, nome, prezzo,quantita): # costruttore con parametri nome, prezzo e quantità
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        
class Magazzino:
    def __init__(self): # costruttore
        self.listaProdotti = []
        self.totale = 0
        
    def aggiungi_prodotto(self):
        nome = input("Inserisci il nome del prodotto da aggiungere: ")
        nome = nome.capitalize() # prima lettera maiuscola
        prezzo = float(input("Inserisci il prezzo del prodotto (usare il punto (.) per i centesimi): "))
        quantita = int(input("Inserisci il numero intero di pezzi da aggiungere: "))
        p = Prodotto(nome, prezzo, quantita) # istanzia un oggetto Prodotto con attributi nome, prezzo, quantità
        self.listaProdotti.append(p) # aggiunge l'oggetto Prodotto alla lista dei prodotti

    def valoreTotale(self): 
        self.totale = 0  # Reset della somma totale
        for prodotto in self.listaProdotti: # per ogni oggetto nella lista prende i valori prezzo e quantità
            self.totale += prodotto.prezzo * prodotto.quantita
        print(f"Il valore totale del tuo magazzino è {self.totale:.2f}")

    def cerca_prodotto(self):
        cercare = input("Inserisci il nome del prodotto da cercare: ")
        cercare = cercare.capitalize() # prima lettera maiuscola
        trovato = False # impostato su false per cercare i prodotti
        for prodotto in self.listaProdotti:
            if prodotto.nome == cercare:
                print(f"Prodotto: {prodotto.nome}, prezzo: {prodotto.prezzo}, quantità: {prodotto.quantita}")
                trovato = True
                break
            print("Il prodotto non è presente nel magazzino")
            
m = Magazzino() # istanzia oggetto magazzino senza passarne parametri
print("Il tuo magazzino al momento è vuoto! Aggiungi almeno un prodotto!")

while True:
    m.aggiungi_prodotto() # aggiunge il prodotto al magazzino
    scelta = input("Vuoi aggiungere un altro prodotto? (s/n): ").lower()
    if scelta != "s":
        break

while True:
    scelta = int(input("\nCosa desideri fare adesso?\nCercare un prodotto (1)\nVisionare il valore totale del magazzino (2)\nAggiungere un altro prodotto (3)\nUscire (4): "))
    match scelta: #menu
        case 1:
            m.cerca_prodotto()
            
        case 2:
            m.valoreTotale()
        
        case 3:
            m.aggiungi_prodotto()
        
        case 4:
            break
        
        case _: # caso standard che si verifica che non ci sono corrispondenze
            break