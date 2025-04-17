import numpy as np

# Creazione di un array con valori mancanti (NaN)
data = np.array([1, 2, np.nan, 4, 5, np.nan, 7])

# Rimozione dei valori mancanti
clean_data = data[~np.isnan(data)]
print("Dati puliti:", clean_data)  # Output: [1. 2. 4. 5. 7.]


import numpy as np

# Creazione di un array di dati
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Definizione della finestra per la media mobile
window_size = 3

# Calcolo della media mobile
moving_average = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
print("Media mobile:", moving_average)  # Output: [2. 3. 4. 5. 6. 7. 8.]


import numpy as np

# Creazione di un segnale con due frequenze
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 20 * t)

# Calcolo della Trasformata di Fourier
fft_signal = np.fft.fft(signal)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_signal))

print("Trasformata di Fourier:", fft_signal)
print("Frequenze associate:", freqs)


import numpy as np

# Numero di simulazioni
num_simulations = 10000

# Generazione di rendimenti giornalieri casuali
daily_returns = np.random.normal(0, 0.01, num_simulations)

# Simulazione del valore finale di un investimento iniziale
initial_investment = 1000
final_value = initial_investment * np.cumprod(1 + daily_returns)

print("Valore finale simulato dell'investimento:", final_value[-1])


