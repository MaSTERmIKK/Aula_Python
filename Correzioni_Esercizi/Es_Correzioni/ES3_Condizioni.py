accounts = []   # Lista di account, ognuno è [id, nome, password]
next_id = 1     # Contatore per l'ID progressivo

scelta = input("Vuoi creare un nuovo account? (s/n): ")

if scelta.lower() == 's':
    # Creazione di un nuovo account
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    
    # Costruiamo la lista con i dati
    nuovo_account = [next_id, nome, password]
    accounts.append(nuovo_account)
    
    print(f"Account creato con successo! ID assegnato: {next_id}")
    next_id += 1


