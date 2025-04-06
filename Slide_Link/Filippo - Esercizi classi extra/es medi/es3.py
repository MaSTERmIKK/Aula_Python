"""
🔵 Esercizio 3: Gestione Playlist Musicale
Crea una classe Brano e una classe Playlist.

Classe Brano:
Attributi: titolo, artista, durata (in minuti, es. 3.5)

Classe Playlist:
Attributo: brani (lista di oggetti Brano)

Metodi:

aggiungi_brano(brano)

durata_totale() → somma tutte le durate

cerca_per_artista(nome) → stampa tutti i titoli dei brani di quell’artista

Obiettivo: gestione di tuple o oggetti con cicli, somma e filtri.

"""

class Brano:
    def __init__(self, titolo, artista, durata): # costruttore con parametri passati
        self.titolo = titolo
        self.artista = artista
        self.durata = durata
        
class Playlist:
    def __init__(self): # costruttore 
        self.listaBrani = [] # lista dove aggiungere oggetti Brano
        self.durata = 0
        
    def aggiungi_brano(self): # aggiunge un brano alla playlist
        titolo = input("Inserisci il titolo del brano: ")
        artista = input("Inserisci il titolo dell'artista: ")
        durata = float(input("Inserisci la durata del brano in minuti (es. 3.5): "))
        titolo, artista = titolo.capitalize() , artista.capitalize() # prima lettera maiuscola
        c = Brano(titolo, artista, durata)
        self.listaBrani.append(c)
        
    def durata_totale(self): # durata totale playlist
        self.durata = 0
        for canzone in self.listaBrani:
            self.durata += canzone.durata # somma la durata di ogni canzone
        durataOre = self.durata / 60 # divide i minuti per 60 in modo da ottenere le ore
        print(f"La durata totale della tua playlist è di {self.durata} minuti o, se preferisci, {durataOre:.2f} ore")
        
    def cerca_per_artista(self): # cerca canzone nella lista
        artistaDaCercare = input("Inserisci il nome dell'artista: ")
        artistaDaCercare = artistaDaCercare.capitalize()
        trovato = False # impostato False per la ricerca
        for artista in self.listaBrani:
            if artistaDaCercare == artista.artista:
                print(f"Canzoni associate all'artista: {artista.titolo}")
                trovato = True # impostato a True per non esaudire la condizione nella riga successiva
        if not trovato:
            print("Artista non trovato")
            
    def elimina_canzone(self): # rimuove canzone dalla lista brani
        titoloDaEliminare = input("Inserisci il titolo della canzone da eliminare: ")
        ArtistaDaEliminare = input("Inserisci l'artista della canzone da eliminare: ") # per evitare ridondanze di titoli richiede anche l'artista della canzone
        titoloDaEliminare, ArtistaDaEliminare = titoloDaEliminare.capitalize(), ArtistaDaEliminare.capitalize()
        trovato = False
        for canzone in self.listaBrani:
            if titoloDaEliminare == canzone.titolo and ArtistaDaEliminare == canzone.artista: # verifica che ci siano corrispondenze di titolo e artista contemporaneamente
                self.listaBrani.remove(canzone) # rimuove la canzone interessata
                print("Canzone rimossa")
                trovato = True
                break
        if not trovato:
            print("Canzone non trovata")
            
    def playlist_completa(self): # stampa intera playlist con titolo,artista e durata per ogni canzone
        if len(self.listaBrani) == 0:
            print("La playlist è vuota")
        else:
            for canzone in self.listaBrani:
                print(f"Titolo: {canzone.titolo}, artista: {canzone.artista}, durata {canzone.durata}")
                    
p = Playlist() #istanzia un oggetto Playlist    
  
print("La tua playlist al momento è vuota! Aggiungi almeno un brano!")
while True:
    p.aggiungi_brano() # aggiungi brano alla playlist
    scelta = input("Vuoi continuare ad aggiungere brani? (s/n): ").lower()
    if scelta != "s":
        break
    
while True:
    scelta = int(input("\nCosa vuoi fare?\nAggiungi un brano (1)\nStampa durata playlist (2)\nCerca canzoni per artista (3)\nRimuovi una canzone dalla playlist (4)\nStampa intera playlist (5)\n Esci (6): "))
    match scelta: # menu
        case 1:
            p.aggiungi_brano()
        
        case 2:
            p.durata_totale()
            
        case 3:
            p.cerca_per_artista() 
            
        case 4:
            p.elimina_canzone()
            
        case 5:
            p.playlist_completa()

        case 6:
            break
        
        case _: 
            break