def esempio_completo(lista, dizionario, file_path):
    """
    Esegue diverse operazioni per illustrare il catch delle principali famiglie di errori:
      1) Accesso a lista e dizionario
      2) Apertura file
      3) Conversione e divisione aritmetica
    """
    try:
        # 1) LookupError: accesso a indice e chiave
        elemento = lista[2]                # può sollevare IndexError
        valore = dizionario["chiave"]      # può sollevare KeyError
        
        # 2) OSError: apertura file
        with open(file_path, 'r') as f:    
            contenuto = f.read().strip()
        
        # 3) ValueError/TypeError/ZeroDivisionError
        numero = int(contenuto)            # ValueError se contenuto non è numerico
        risultato = numero / 0             # ZeroDivisionError
        
        print("Risultato complessivo:", risultato)

    except IndexError as e:
        print("Errore di indice (LookupError):", e)

    except KeyError as e:
        print("Errore di chiave (LookupError):", e)

    except FileNotFoundError as e:
        print("File non trovato (OSError):", e)

    except PermissionError as e:
        print("Permessi insufficienti (OSError):", e)

    except ValueError as e:
        print("Conversione non valida (ValueError):", e)

    except TypeError as e:
        print("Tipo dati non compatibile (TypeError):", e)

    except ZeroDivisionError as e:
        print("Divisione per zero non permessa (ArithmeticError):", e)

    except Exception as e:
        # Qualunque altra eccezione imprevista
        print("Errore imprevisto:", e)

    else:
        # Eseguito solo se non è caduto alcun except
        print("Tutte le operazioni sono andate a buon fine.")

    finally:
        # Viene sempre eseguito
        print("Fine funzione esempio_completo.")

# --- Esempio di chiamata ---
if __name__ == "__main__":
    lis = [10, 20]                # lista troppo corta per lis[2]
    diz = {"altra": "valore"}     # non contiene "chiave"
    percorso = "non_esiste.txt"   # file inesistente

    esempio_completo(lis, diz, percorso)
