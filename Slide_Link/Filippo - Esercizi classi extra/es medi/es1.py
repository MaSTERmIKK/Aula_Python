# 🔵 Esercizio 1: Registro Studenti

# Avviso: l'esercizio contiene funzioni e procedimenti aggiuntivi non richiesti esplicitamente nelle tracce

idStudenti = 0  # Variabile globale per assegnare un ID unico a ogni studente, utile per calcolare il miglior studente

class Studente:
    def __init__(self, nome, cognome): # costruttore che accetta parametri
        self.nome = nome
        self.cognome = cognome
        self.registro_materie = {
            "Matematica": [],
            "Italiano": [],
            "Storia": [],
            "Scienze": [],
            "Inglese": []
        } # chiave,materia: valore,lista dei voti

    def aggiungi_voto(self): # funzione per aggiungere voti alla lista grazie al ciclo
        while True:
            materiaVoto = input("Lista materie:\nMatematica, Italiano, Storia, Scienze, Inglese.\nInserisci la materia a cui vuoi aggiungere il voto: ")
            materiaVoto_capitalizzata = materiaVoto.capitalize() # rende la prima lettera maiuscola

            if materiaVoto_capitalizzata in self.registro_materie: # verifica che la materia scelta sia presente nel dizionario delle materie
                votoDaAggiungere = int(input("Inserisci il voto da aggiungere: "))
                self.registro_materie[materiaVoto_capitalizzata].append(votoDaAggiungere) # aggiunge il valore alla lista
                continuare = input("Aggiungere un altro voto? (s/n): ").lower()
                if continuare != "s":
                    break
            else:
                print("Materia non valida, riprova.")

    def media_voti(self): # calcola la media delle materie
        mediaMaterie = [] # lista che contiene la media di ogni materia
        
        # Cicla su ogni coppia chiave-valore del dizionario delle materie dello studente
        # 'materia' sarà il nome della materia (es. "Matematica"), 'voti' la lista dei voti associati
        for materia, voti in self.registro_materie.items():
            mediaMateria = sum(voti) / len(voti) if len(voti) > 0 else 0 # calcola la media, se la lista è vuota restituisce 0
            mediaMaterie.append(mediaMateria)
        mediaFinale = sum(mediaMaterie) / len(mediaMaterie) if len(mediaMaterie) > 0 else 0 # calcola la media, se la lista è vuota restituisce 0
        print(f"La media generale di {self.nome} {self.cognome} è {mediaFinale:.2f}")
        return mediaFinale # restituisce il valore perchè serve per calcolare la media della classe


class Registro:
    def __init__(self):
        self.dizStudenti = {} # chiave, idstudente: valore, istanza Studente creata
        self.trovaStudenti = {} # ad ogni id, associa il nome dello studente
        self.mediaStudenti = [] # lista che contiene i valori delle medie finali di ogni studente

    def aggiungi_studenti(self): # funzione per istanziare oggetti di classe Studente
        global idStudenti
        while True: 
            nomeStudente = input("Inserisci il nome dello studente: ")
            cognomeStudente = input("Inserisci il cognome dello studente: ")
            s = Studente(nomeStudente, cognomeStudente)

            s.aggiungi_voto() # richiama il metodo della classe Studente

            self.dizStudenti[idStudenti] = s # associa id a oggetto studente nel dizionario
            self.trovaStudenti[idStudenti] = nomeStudente # associa id a nome studente nel dizionario
            print(f"{nomeStudente}, il tuo ID è {idStudenti}")
            idStudenti += 1

            mediaFinale = s.media_voti() # memorizza la media finale per passarla alla funzione media classe
            self.mediaStudenti.append(mediaFinale)

            continuare = input("Continuare ad aggiungere studenti? (s/n): ").lower()
            if continuare != "s":
                break
        return self.mediaStudenti

    def media_classe(self): # calcola la media della classe considerando la lista delle medie degli studenti
        if len(self.mediaStudenti) == 0:
            print("Nessuno studente registrato.")
            return
        mediaClasse = sum(self.mediaStudenti) / len(self.mediaStudenti)
        print(f"La media della classe è: {mediaClasse:.2f}") # formatta il numero con 2 cifre decimali

    def migliore_studente(self, medie): # trova il miglior studente
        if not medie:
            print("Nessuno studente registrato.")
            return

        media_massima = max(medie)  # Trova la media più alta
        id_migliore = medie.index(media_massima)  # Prende l'indice (che è anche l'ID)

        nome_migliore = self.trovaStudenti.get(id_migliore)  # Recupera il nome dallo studente
        print(f"Il miglior studente è {nome_migliore} con una media di {media_massima:.2f}")


            

# Esecuzione del programma
r = Registro()
medie = r.aggiungi_studenti()
r.media_classe()
r.migliore_studente(medie)

        