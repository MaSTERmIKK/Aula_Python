"""
🟠 Esercizio 3: Classe "Studente"
Scrivi una classe Studente con:

attributi: nome, cognome, voti (lista di interi)

metodo aggiungi_voto(voto) per aggiungere un voto alla lista

metodo media() per calcolare e restituire la media dei voti

metodo scheda() che stampa nome, cognome e media

Obiettivo: lavorare con attributi mutabili (liste) e semplici logiche di calcolo.
"""

class Studente:
    def __init__(self, nome, cognome, voti): # costruttore
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
        
    def aggiungi_voto(self): # funzione per aggiungere un voto alla lista passata
        while True:
            votoNuovo = int(input("Inserisci il voto da aggiungere alla lista: "))
            self.voti.append(votoNuovo)
            whatdo = input("Vuoi aggiungere altri voti? (s/n)").lower()
            if whatdo != "s":
                break
        
    def media(self): # calcola la media effettuando la somma dei parametri nella lista per poi dividerla per il numero dei parametri
        media = sum(self.voti) / len(self.voti) if len(self.voti) > 0 else 0 # se la lista è vuota restituisce 0
    
    def scheda(self, media): # prende il valore della media passato dalla funzione media
        print(f"Nome: {self.nome}\nCognome: {self.cognome}\nMedia: {media}")
        
voti = [1,4,6,3,2,7,8,4,2] # lista voti da passare
f = Studente("Filippo", "pippo", voti)
f.aggiungi_voto()
media = f.media()
f.scheda(media)