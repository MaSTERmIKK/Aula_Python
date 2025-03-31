# Esempio 1: If, Elif, Else
# Assegniamo un valore a "x" e lo valutiamo con delle condizioni.
x = 10

if x > 10:
    print("x è maggiore di 10")
elif x == 10:
    print("x è uguale a 10")
else:
    print("x è minore di 10")

# Esempio 2: Ciclo for con range()
# Stampiamo i numeri da 0 a 4 usando range(5).
for i in range(5):
    print("Valore di i nel for con range(5):", i)

# Esempio 3: Ciclo for per iterare su una lista
frutti = ["mela", "banana", "ciliegia"]
for frutto in frutti:
    print("Frutto:", frutto)

# Esempio 4: Ciclo while
# Contiamo da 1 a 5 utilizzando while.
contatore = 1
while contatore <= 5:
    print("Contatore mentre è in esecuzione il while:", contatore)
    contatore += 1  # Incrementiamo il contatore

# Esempio 5: Utilizzo di break e continue
numeri = [1, 2, 3, 4, 5, 6, 7]
for numero in numeri:
    if numero == 4:
        print("Trovato il 4, interrompo il ciclo con break.")
        break  # Interrompe il ciclo se numero è 4
    elif numero == 2:
        print("Trovato il 2, salto il resto di questa iterazione con continue.")
        continue  # Salta il resto dell'iterazione se numero è 2
    print("Numero elaborato:", numero)

# Esempio 6: Condizioni annidate
# Usiamo condizioni if annidate per verificare più criteri.
a = 5
b = 10
if a < b:
    print("\na è minore di b")
    if b == 10:
        print("b è esattamente 10")
else:
    print("a non è minore di b")

# Esempio 7: Ciclo while con condizione più complessa
# Continuiamo a chiedere un valore finché l'utente non inserisce "stop".
# (Se vuoi provare su un IDE interattivo, decommenta)
"""
valore = ""
while valore != "stop":
    valore = input("Digita qualcosa (digita 'stop' per terminare): ")
    print("Hai digitato:", valore)
"""

# Esempio 8: Uso di variabili per contare iterazioni
# Creiamo un ciclo for che itera su una lista e conta quanti elementi superano la soglia.
soglia = 3
valori = [1, 4, 2, 6, 3, 7, 2]
count_superiori = 0

for v in valori:
    if v > soglia:
        count_superiori += 1

print("\nNumero di elementi che superano la soglia di", soglia, ":", count_superiori)

# Esempio 9: If in linea (One-line if statement)
num = 20
messaggio = "Maggiore di 10" if num > 10 else "Minore o uguale a 10"
print("\nMessaggio:", messaggio)

# Esempio 10: Cicli for annidati
# Stampiamo le coordinate di una piccola griglia (2x2)
for riga in range(2):
    for colonna in range(2):
        print(f"Coordinate (riga={riga}, colonna={colonna})")
