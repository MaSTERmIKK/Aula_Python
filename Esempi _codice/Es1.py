import numpy as np

# Creazione di un array unidimensionale
array_1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensionale:", array_1d)

# Creazione di un array bidimensionale
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array bidimensionale:", array_2d)


# np.arange è utilizzato per generare array con valori in un intervallo specificato.
# Array da 0 a 9
array_range = np.arange(10)
print("Array da 0 a 9:", array_range)

# Array da 10 a 20 con step di 2
array_step = np.arange(10, 20, 2)
print("Array da 10 a 20 con step di 2:", array_step)


# np.reshape permette di cambiare la forma di un array esistente senza cambiare i suoi dati.
# Reshape di un array 1D in un array 2D (2 righe, 5 colonne)
array_1d = np.arange(10)
array_reshaped = array_1d.reshape((2, 5))
print("Array reshape da 1D a 2D:", array_reshaped)

# Reshape automatico con -1
array_reshaped_auto = array_1d.reshape((-1, 2))
print("Array reshape con -1 per inferire automaticamente le dimensioni:", array_reshaped_auto)



