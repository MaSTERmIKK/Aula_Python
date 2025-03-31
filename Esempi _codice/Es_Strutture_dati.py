"""
Esempi unificati di strutture dati in Python:
- Liste
- Tuple
- Set
- Dizionari
- Condizioni e cicli
- Funzioni
"""

def esempi_liste():
    """
    Mostra varie operazioni su liste:
    creazione, aggiunta, rimozione, slicing, cicli, etc.
    """
    print("=== LISTE ===")
    # Creazione di una lista
    numeri = [1, 2, 3, 4]
    parole = ["mirko","mirko","mirko"]
    misto =["mirko", 13, True, 13.23 ]
    vuota = []
    
    print("Lista Stringhe:", parole)
    print("Lista Misto:", misto)
    print("Lista iniziale:", numeri)
    
    # Aggiunta di un elemento alla fine (append)
    numeri.append(5)
    vuota.append(1)
    print("Dopo append(5):", numeri)
    
    # Inserimento in posizione specifica (insert)
    numeri.insert(2, 99)
    print("Dopo insert(2, 99):", numeri)
    
    # Rimozione di un elemento tramite valore (remove)
    numeri.remove(99)
    print("Dopo remove(99):", numeri)
    
    # Rimozione dell'ultimo elemento (pop)
    ultimo = numeri.pop()
    print(f"Dopo pop() -> elemento rimosso: {ultimo}, lista:", numeri)
    
    # Slicing
    # numeri[inizio:fine] => sotto-lista dall'indice 'inizio' fino a 'fine-1'
    print("Slicing numeri[0:2]:", numeri[0:2])
    
    # Iterazione su lista
    print("Iterazione sui valori di 'numeri':")
    for val in numeri:
        print(" -", val)
    
    # List comprehension: creiamo una lista di quadrati
    quadrati = [x*x for x in numeri]
    print("Quadrati dei numeri:", quadrati)


def esempi_tuple():
    """
    Mostra operazioni con tuple (immutabili).
    """
    print("\n=== TUPLE ===")
    # Creazione di una tupla
    coordinate = (10, 20)
    print("Tupla coordinate:", coordinate)
    print("Primo elemento:", coordinate[0])
    print("Secondo elemento:", coordinate[1])
    
    # Le tuple sono immutabili, non si può fare coordinate[0] = 100
    # coordinate[0] = 100 -> ERRORE
    
    # Possiamo iterare su una tupla come su una lista
    print("Iterazione sulla tupla:")
    for val in coordinate:
        print(" -", val)
    
    # Possiamo "spacchettare" (unpack) una tupla in più variabili
    x, y = coordinate
    print(f"x = {x}, y = {y}")


def esempi_set():
    """
    Mostra operazioni con i set (insiemi) in Python.
    """
    print("\n=== SET ===")
    # Creazione di un set
    lettere = {'a', 'b', 'c', 'a'}  # 'a' è duplicato, verrà ignorato
    print("Set iniziale (duplicati rimossi):", lettere)
    
    # Aggiunta di un elemento
    lettere.add('d')
    print("Dopo add('d'):", lettere)
    
    # Rimozione di un elemento (se esiste)
    lettere.discard('b')
    print("Dopo discard('b'):", lettere)
    
    # Verifica se un elemento è nel set
    if 'c' in lettere:
        print("L'elemento 'c' è nel set")
    else:
        print("L'elemento 'c' non è nel set")
    
    # Operazioni di unione, intersezione, differenza
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    unione = set1.union(set2)          # {1, 2, 3, 4, 5}
    intersezione = set1.intersection(set2)  # {3}
    differenza = set1.difference(set2)      # {1, 2}
    differenza2 = set2.difference(set1)      # {4, 5}
    
    print("Set1:", set1)
    print("Set2:", set2)
    print("Unione:", unione)
    print("Intersezione:", intersezione)
    print("Differenza:", differenza)
    print("Differenza 2:", differenza2)


def esempi_dizionari():
    """
    Mostra operazioni con i dizionari:
    creazione, accesso, aggiunta, rimozione, cicli, etc.
    """
    print("\n=== DIZIONARI ===")
    # Creazione di un dizionario
    persona = {
        "nome": "Mario",
        "eta": 30,
        "citta": "Roma"
        # qui si aggiungono nuovi elementi
    }
    print("Dizionario persona:", persona)
    
    # Accesso ai valori
    print("Nome:", persona["nome"])
    print("Età:", persona["eta"])
    
    # Aggiunta/aggiornamento di una chiave
    persona["professione"] = "Ingegnere"
    print("Dopo aggiunta 'professione':", persona)
    
    # Rimozione di una chiave
    del persona["citta"]
    print("Dopo rimozione 'citta':", persona)
    
    # Verifica se una chiave esiste
    if "eta" in persona:
        print("La chiave 'eta' esiste nel dizionario.")
    
    # Iterazione su chiavi e valori
    for chiave, valore in persona.items():
        print(f" - Chiave: {chiave}, Valore: {valore}")
    
    # Esempio di dizionario annidato
    rubrica = {
        "contatto1": {
            "nome": "Luigi",
            "numero": "123456789"
        },
        "contatto2": {
            "nome": "Anna",
            "numero": "987654321"
        }
    }
    print("\nRubrica annidata:", rubrica)
    
    # Iterazione su dizionario di dizionari
    for contatto_id, dati in rubrica.items():
        print(f"Contatto: {contatto_id}")
        for k, v in dati.items():
            print(f"  {k.capitalize()}: {v}")


def main():
    """
    Funzione principale che chiama le varie sezioni di esempio.
    """
    #esempi_liste()
    #esempi_tuple()
    esempi_set()
    #esempi_dizionari()


if __name__ == "__main__":
    main()
