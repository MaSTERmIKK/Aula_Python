# Esempio 1: Assegnazione di base
# Qui creiamo variabili di diversi tipi e stampiamo il loro valore.
numero_intero = 10            # Variabile di tipo intero
numero_decimale = 3.14        # Variabile di tipo float
testo = "Ciao Python"         # Variabile di tipo stringa
vero_falso = True             # Variabile booleana

print("Intero:", numero_intero)
print("Decimale:", numero_decimale)
print("Stringa:", testo)
print("Booleano:", vero_falso)

# Esempio 2: Assegnazione multipla
# Possiamo assegnare più variabili in una sola istruzione.
x, y, z = 1, 2, 3
print("\nAssegnazione multipla -> x:", x, "y:", y, "z:", z)

# Esempio 3: Ridefinizione di variabili
# In Python, una variabile può cambiare tipo in qualsiasi momento.
x = 100
print("\nDopo la ridefinizione, x:", x)
x = "Ora sono una stringa"
print("Dopo la ridefinizione, x:", x)

# Esempio 4: Operazioni aritmetiche con variabili
a = 5
b = 2
somma = a + b
differenza = a - b
prodotto = a * b
divisione = a / b
divisione_intera = a // b
resto = a % b
potenza = a ** b

print("\nOperazioni aritmetiche con a=5 e b=2:")
print("Somma:", somma)
print("Differenza:", differenza)
print("Prodotto:", prodotto)
print("Divisione:", divisione)
print("Divisione intera:", divisione_intera)
print("Resto:", resto)
print("Potenza:", potenza)

# Esempio 5: Utilizzo di variabili in espressioni logiche
maggiore = a > b
uguale = a == b
minore_o_uguale = b <= 2

print("\nEspressioni logiche:")
print("a > b :", maggiore)
print("a == b:", uguale)
print("b <= 2:", minore_o_uguale)

# Esempio 6: Variabili e concatenazione di stringhe
nome = "Mario"
cognome = "Rossi"
nome_completo = nome + " " + cognome
print("\nConcatenazione di stringhe -> nome completo:", nome_completo)

# Esempio 7: Variabili in liste
lista_numeri = [1, 2, 3]
lista_numeri[1] = 20  # Assegnazione di un nuovo valore a un elemento della lista
print("\nLista numeri dopo la modifica:", lista_numeri)

# Esempio 8: Variabili in tuple (immutabili)
# Le tuple, a differenza delle liste, non possono essere modificate dopo la creazione.
coordinate = (10, 20)
print("\nCoordinate (tuple):", coordinate)

# Esempio 9: Variabili in dizionari
dizionario = {
    "nome": "Mario",
    "eta": 30
}
print("\nDizionario iniziale:", dizionario)
dizionario["citta"] = "Roma"  # Aggiunta di una nuova chiave-valore
print("Dizionario dopo l'aggiunta di una chiave 'citta':", dizionario)

# Esempio 10: Gestione di variabili con funzioni (senza OOP)
def stampa_variabili():
    # Questa funzione usa variabili locali
    locale_a = 10
    locale_b = 20
    print("\nNella funzione, locale_a:", locale_a, "locale_b:", locale_b)

stampa_variabili()

# Esempio 11: Variabili globali
VALORE_GLOBALE = 100

def modifica_globale():
    global VALORE_GLOBALE
    VALORE_GLOBALE = 200  # Modifica la variabile globale

print("\nPrima della modifica:", VALORE_GLOBALE)
modifica_globale()
print("Dopo la modifica globale:", VALORE_GLOBALE)
