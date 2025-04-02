# Esempio 1: Funzione semplice senza parametri e senza return
def saluta():
    
    #Questa funzione stampa un saluto.
    #Non prende parametri e non restituisce alcun valore.
    
    print("Ciao! Questa è una funzione che non richiede parametri.")

# Chiamata della funzione
saluta()



# Esempio 2: Funzione con parametri e return
def somma(x, y):
    """
    Questa funzione prende due parametri (x, y),
    calcola la somma e restituisce il risultato.
    """
    risultato = x + y
    return risultato

# Esempio di utilizzo della funzione 'somma'
valore1 = 5
valore2 = 10
risultato_somma = somma(valore1, valore2)     # uguale a scrivere valore 1 + valore 2
print("Somma di", valore1, "e", valore2, "=", risultato_somma)
print (somma(valore1, valore2))


# Esempio 3: Funzione con parametri opzionali (default)
def moltiplica(a, b=2):
    """
    Questa funzione moltiplica 'a' e 'b'.
    'b' ha un valore di default di 2.
    """
    return a * b

# Chiamate della funzione 'moltiplica' con e senza parametro opzionale
print("\nMoltiplicazione con parametro opzionale b=2:", moltiplica(3))
print("Moltiplicazione con b specificato a 4:", moltiplica(3, 4))

# e uguale a fare
moltx = moltiplica(2,3)
print(f"il risultato è {moltx}")
# e uguale 
print("il risultato è ", moltx)

risultato2 = moltiplica(moltiplica(3,3) , moltiplica(3,3))
risultato3=moltiplica(9,9)
risultato2 = moltiplica( moltiplica(2,5) , moltiplica(2,5))
risultato3 = (10,10)


# Esempio 4: Funzione che utilizza condizioni (if-elif-else)
def descrivi_numero(num):
    """
    Se num > 0: stampa "Positivo"
    Se num < 0: stampa "Negativo"
    Altrimenti: stampa "Zero"
    """
    if num > 0:
        return print("\nIl numero", num, "è Positivo.")
    elif num < 0:
        return print("\nIl numero", num, "è Negativo.")
    else:
        return print("\nIl numero è Zero.")

# Chiamate di esempio
descrivi_numero(10)
descrivi_numero(-5)
descrivi_numero(0)


# Esempio 5: Funzione che utilizza un ciclo for
def stampa_lista_elementi(lista_elementi):
    """
    Itera su una lista e stampa ogni elemento.
    """
    print("\nStampa degli elementi della lista:")
    for elem in lista_elementi:
        print(" -", elem)

# Lista di esempio da passare alla funzione
frutti = ["Mela", "Banana", "Ciliegia"]
stampa_lista_elementi(frutti)

#quindi sono identici i funzionamenti con tutti i tipi
numeri = [1,2,3,4]
stampa_lista_elementi(numeri)


# Esempio 6: Funzione che utilizza un ciclo while
def conta_fino_a_n(n):
    """
    Conta da 1 fino a n utilizzando un ciclo while e stampa ogni valore.
    """
    contatore = 0
    print("Conta da 1 fino a ", n)
    while contatore <= n:
        print(contatore, end=" ")
        contatore += 1
    print()  # Stampa di un a capo finale

# Chiamata della funzione
conta_fino_a_n(5)


# Esempio 7: Funzione che utilizza break e continue

def cerca_valore(lista_valori, valore_cercato):
    """
    Cerca 'valore_cercato' in 'lista_valori'.
    Se lo trova, interrompe il ciclo (break).
    Salta qualsiasi valore pari (continue), e non lo valuta.
    """
    for val in lista_valori:
        # Se è un numero pari, continua alla prossima iterazione
        if val % 2 == 0:
            continue
        
        if val == valore_cercato:
            print(f"\nValore {valore_cercato} trovato, interrompo la ricerca.")
            break
        else:
            print(f"Valore {val} non è quello cercato.")

# Chiamata della funzione con un esempio
numeri = [2, 4, 5, 7, 11, 12, 13]
cerca_valore(numeri, 11)


# Esempio 8: Funzione con cicli annidati
def stampa_tabella_moltiplicazione(dim):
    """
    Stampa la tabella di moltiplicazione da 1 a 'dim'.
    Utilizza cicli for annidati.
    """
    print(f"\nTabella di moltiplicazione 1x{dim}:")
    for i in range(1, dim+1):
        for j in range(1, dim+1):
            print(f"{i*j:4d}", end="")  # Formattazione per allineare i risultati
        print()  # A capo dopo ogni riga

# Chiamata della funzione
stampa_tabella_moltiplicazione(5)


# Esempio 9: Funzione ricorsiva (facoltativo, mostra un uso particolare delle funzioni)
def fattoriale(n):
    """
    Calcola il fattoriale di 'n' ricorsivamente.
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n <= 1:
        return 1
    else:
        return n * fattoriale(n - 1)

# Chiamata della funzione ricorsiva
numero = 5
print(f"\nFattoriale di {numero}:", fattoriale(numero))




def quadrato_iterno(n):
    risultato = n*n
    print(risultato)


def quadrato(n):
    return n*n


num = int(input())
quadrato(num)

def quadrato2():
    x= int(input())
    return x*x

print(quadrato())

def cubo(n):
    return n*n*n


