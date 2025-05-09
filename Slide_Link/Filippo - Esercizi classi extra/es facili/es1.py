# 🟠 Esercizio 1: Classe "Libro"

class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione): # costruttore
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.recente = False # Attributo che sarà aggiornato se il libro è recente
        
    def descrizione(self): # stampa la descrizione del libro
        return f"Il libro {self.titolo}, scritto da {self.autore}, è stato pubblicato nel {self.anno_pubblicazione}"
    
    def e_recente(self): # verifica se è recente
        if self.anno_pubblicazione >= 2020: 
            self.recente = True # se la data di pubblicazione è nel 2020 o dopo, la variabile viene riscritta come True
            return f"Il libro è recente?....{self.recente}" 

titolo = input("Inserisci il titolo del libro: ")
autore = input("Inserisci l'autore del libro: ")
anno_pubblicazione = int(input("Inserisci l'anno di pubblicazione: "))

l = Libro(titolo, autore, anno_pubblicazione) # Istanzia un oggetto di tipo Libro con i parametri forniti: titolo, autore e anno_pubblicazion

print(l.descrizione())
print(l.e_recente())