print("=== Controllo a 3 livelli con numeri ===")

# Primo livello
numero1 = int(input("Inserisci un numero per sbloccare il Livello 1 (>= 10 richiesto): "))
if numero1 >= 10:
    print("Livello 1 sbloccato!")
    
    # Secondo livello
    numero2 = int(input("Inserisci un numero per sbloccare il Livello 2 (>= 20 richiesto): "))
    if numero2 >= 20:
        print("Livello 2 sbloccato!")
        
        # Terzo livello
        numero3 = int(input("Inserisci un numero per sbloccare il Livello 3 (>= 30 richiesto): "))
        if numero3 >= 30:
            print("Livello 3 sbloccato! Hai ottenuto l’accesso completo.")
        else:
            print("Numero troppo piccolo per sbloccare il Livello 3. Accesso negato.")
    else:
        print("Numero troppo piccolo per sbloccare il Livello 2. Accesso negato.")
else:
    print("Numero troppo piccolo per sbloccare il Livello 1. Accesso negato.")
