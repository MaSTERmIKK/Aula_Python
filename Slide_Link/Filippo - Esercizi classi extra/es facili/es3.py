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
    def __init__(self, nome, cognome, voti):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
        
    def aggiungi_voto(self):
        pass