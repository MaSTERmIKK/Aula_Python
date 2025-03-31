# Menu testuale che permette di:
# 1) Aggiungere un elemento
# 2) Rimuovere un elemento
# 3) Visualizzare la lista
# 4) Svuotare/eliminare tutta la lista
# 5) Uscire

lista_elementi = []

while True:
    print("\n--- MENU ---")
    print("1) Aggiungi elemento")
    print("2) Rimuovi elemento")
    print("3) Visualizza lista")
    print("4) Elimina tutta la lista")
    print("5) Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        elemento = input("Inserisci l'elemento da aggiungere: ")
        lista_elementi.append(elemento)
        print(f"Elemento '{elemento}' aggiunto con successo.")

    elif scelta == "2":
        elemento = input("Inserisci l'elemento da rimuovere: ")
        if elemento in lista_elementi:
            lista_elementi.remove(elemento)
            print(f"Elemento '{elemento}' rimosso con successo.")
        else:
            print(f"Elemento '{elemento}' non trovato nella lista.")

    elif scelta == "3":
        print("Contenuto della lista:")
        if len(lista_elementi) == 0:
            print("[Lista vuota]")
        else:
            for elem in lista_elementi:
                print(f"- {elem}")

    elif scelta == "4":
        lista_elementi.clear()
        print("Lista completamente eliminata.")

    elif scelta == "5":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida, riprova.")
