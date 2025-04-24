import matplotlib.pyplot as plt
import numpy as np

# Generiamo dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creiamo il grafico
plt.figure(figsize=(8, 4))            # imposta la dimensione della figura (larghezza, altezza)
plt.plot(x, y)                        # disegna y in funzione di x
plt.title("Grafico di sin(x)")        # titolo del grafico
plt.xlabel("Asse X")                  # etichetta asse X
plt.ylabel("Asse Y")                  # etichetta asse Y
plt.grid(True)                        # mostra la griglia
plt.show()                            # visualizza il grafico


----------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Dati di esempio
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]    # serie 1
y2 = [1, 4, 6, 8, 9]     # serie 2

plt.figure(figsize=(6, 4))

# Serie 1: linea rossa tratteggiata con marker a cerchio
plt.plot(x, y1,
         color='red',          # colore linea
         linestyle='--',       # stile linea (tratteggiata)
         marker='o',           # marker a cerchio
         label='Serie 1')      # etichetta per la legenda

# Serie 2: linea blu continua con marker a quadrato
plt.plot(x, y2,
         color='blue',
         linestyle='-',
         marker='s',           # marker a quadrato
         label='Serie 2')

plt.title("Confronto Serie 1 e Serie 2")
plt.xlabel("Indice")
plt.ylabel("Valore")
plt.legend(loc='upper left')   # posiziona la legenda in alto a sinistra
plt.grid(linestyle=':')         # griglia punteggiata
plt.tight_layout()              # ottimizza spaziatura
plt.show()



----------------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 200)

# Creiamo una figura con 2 righe e 1 colonna di subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Primo subplot: seno
ax1.plot(t, np.sin(t), color='purple')
ax1.set_title("Funzione seno")
ax1.grid(True)

# Secondo subplot: coseno
ax2.plot(t, np.cos(t), color='green')
ax2.set_title("Funzione coseno")
ax2.set_xlabel("Angolo (rad)")
ax2.grid(True)

plt.tight_layout()
plt.show()


----------------------------------------------------------------------------



import matplotlib.pyplot as plt
import numpy as np

# Modifichiamo i parametri globali di matplotlib
plt.rcParams['font.size'] = 12         # dimensione font di default
plt.rcParams['font.family'] = 'serif'  # famiglia di font
plt.rcParams['axes.titlesize'] = 14    # dimensione del titolo degli assi
plt.rcParams['axes.labelsize'] = 12    # dimensione delle etichette degli assi
plt.rcParams['lines.linewidth'] = 2    # spessore linea di default
plt.rcParams['lines.markersize'] = 8   # dimensione marker di default

# Dati di esempio
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x) * np.exp(-x/10)

plt.figure(figsize=(7,4))
plt.plot(x, y, marker='D', label='sin(x)·exp(-x/10)')
plt.title("Damping della sinusoide")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


----------------------------------------------------------------------------



import matplotlib.pyplot as plt
import numpy as np

# Dati
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, label='sin(x)')

# Punto di massimo
max_idx = np.argmax(y)
x_max, y_max = x[max_idx], y[max_idx]
plt.scatter([x_max], [y_max], color='red')  # evidenziamo il punto
plt.annotate("Massimo locale",
             xy=(x_max, y_max),              # coordinate del punto
             xytext=(x_max+0.5, y_max-0.3),  # posizione del testo
             arrowprops=dict(arrowstyle="->", lw=1.5))  # freccia

plt.title("Annotazione di un punto critico")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()

