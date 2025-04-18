def leggi_file_e_dividi(nome_file, divisore):
    """
    Questa funzione tenta di:
      1) Aprire un file e leggerne il contenuto come numero.
      2) Dividere quel numero per un divisore passato come parametro.
    Gestisce possibili errori di I/O e di divisione per zero.
    """
    try:
        # Provo ad aprire il file in modalità lettura di testo
        with open(nome_file, 'r') as f:
            contenuto = f.read().strip()       # Leggo tutto e tolgo eventuali spazi
            numero = float(contenuto)          # Converto la stringa in numero float

        # Provo a dividere il numero per il divisore
        risultato = numero / divisore

    except FileNotFoundError as e:
        # Questo blocco viene eseguito se il file non esiste
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return None

    except ValueError as e:
        # Se la conversione in float fallisce (es. contenuto non numerico)
        print(f"Errore: contenuto del file non valido per la conversione a numero ({e}).")
        return None

    except ZeroDivisionError as e:
        # Gestione specifica della divisione per zero
        print("Errore: non posso dividere per zero!")
        return None

    except Exception as e:
        # Blocco generico per qualsiasi altra eccezione non prevista
        print(f"Si è verificato un errore inatteso: {e}")
        return None

    else:
        # Questo blocco viene eseguito solo se non ci sono state eccezioni
        print(f"Divisione completata con successo: {numero} / {divisore} = {risultato}")
        return risultato

    finally:
        # Viene sempre eseguito, sia che l’operazione abbia avuto successo, sia che ci sia stato un errore
        print("Fine della funzione leggi_file_e_dividi.")

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    # Caso 1: file esistente, numero valido, divisore diverso da zero
    leggi_file_e_dividi("dati.txt", 2)

    # Caso 2: file inesistente
    leggi_file_e_dividi("non_esiste.txt", 5)

    # Caso 3: file presente ma contenuto non numerico
    leggi_file_e_dividi("stringa.txt", 3)

    # Caso 4: tentativo di divisione per zero
    leggi_file_e_dividi("dati.txt", 0)
