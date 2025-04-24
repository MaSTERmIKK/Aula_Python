import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Impostiamo uno stile seaborn
sns.set_theme(style="darkgrid")

# Generiamo dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creiamo il grafico
plt.figure(figsize=(8, 4))
sns.lineplot(x=x, y=y)
plt.title("Grafico di sin(x) con seaborn")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.show()


-------------------------------------------------------------


import seaborn as sns
import matplotlib.pyplot as plt

# Dati di esempio
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 9]

sns.set_theme(style="whitegrid", palette="muted")

plt.figure(figsize=(6, 4))
# Tracciamo entrambe le serie specificando un'etichetta e uno stile di marker
sns.lineplot(x=x, y=y1, marker="o", label="Serie 1")
sns.lineplot(x=x, y=y2, marker="s", label="Serie 2")

plt.title("Confronto Serie 1 e Serie 2 con seaborn")
plt.xlabel("Indice")
plt.ylabel("Valore")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()


-----------------------------------------------------------------


import seaborn as sns
import numpy as np

# Creiamo un DataFrame per sfruttare relplot
import pandas as pd
t = np.linspace(0, 2*np.pi, 200)
df = pd.DataFrame({
    "t": np.concatenate([t, t]),
    "valore": np.concatenate([np.sin(t), np.cos(t)]),
    "funzione": ["seno"]*len(t) + ["coseno"]*len(t)
})

# relplot genera automaticamente sottotrame se dividiamo per "funzione"
sns.set_theme(style="ticks")

g = sns.relplot(
    data=df,
    x="t", y="valore",
    kind="line",
    col="funzione",            # una colonna per ogni funzione
    height=4, aspect=1.5,       # dimensioni di ciascuna subplot
    facet_kws={"sharex": True}
)
g.set_axis_labels("Angolo (rad)", "Valore")
g.set_titles("{col_name}")
plt.show()

---------------------------------------------------------------

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Definiamo tema, font e palette
sns.set_theme(
    context="talk",            # dimensione del font pensata per presentazioni
    style="whitegrid",         # griglia chiara
    palette="coolwarm",        # palette dei colori
    font="serif",              # famiglia di font
    rc={                        # parametri rc aggiuntivi
        "axes.titlesize": 16,
        "axes.labelsize": 14,
        "lines.linewidth": 2,
        "lines.markersize": 8
    }
)

# Dati di esempio
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x) * np.exp(-x/10)

plt.figure(figsize=(7, 4))
sns.lineplot(x=x, y=y, marker="D", label="sin(x)·exp(-x/10)")
plt.title("Damping della sinusoide con seaborn")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



----------------------------------------------------------------------


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Dati 2D di esempio
X, Y = np.meshgrid(np.linspace(0, 1, 30), np.linspace(0, 1, 30))
Z = np.sin(X * np.pi) * np.cos(Y * np.pi)

sns.set_theme(style="dark")
plt.figure(figsize=(6, 5))
# Creiamo una heatmap con barra colore integrata
sns.heatmap(Z, 
            cmap="viridis",      # mappa dei colori
            cbar_kws={"label": "Intensità"},
            square=True,         # caselle quadrate
            xticklabels=5,       # mostra un tick ogni 5
            yticklabels=5)
plt.title("Heatmap di esempio con seaborn")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.show()

