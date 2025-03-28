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

else:
    # Verifica se l'account esiste
    nome = input("Inserisci il tuo nome per l'accesso: ")
    password = input("Inserisci la tua password: ")
    
    account_trovato = None
    for account in accounts:
        # account è [id, nome_account, password_account]
        if account[1] == nome and account[2] == password:
            account_trovato = account
            break

    if account_trovato is not None:
        print(f"Accesso riuscito. Benvenuto {account_trovato[1]} (ID: {account_trovato[0]}).")
        print("Conclusione dello script...")
        # Qui potresti far proseguire il programma oppure terminarlo
    else:
        print("Account non trovato o password errata. Impossibile concludere lo script.")
