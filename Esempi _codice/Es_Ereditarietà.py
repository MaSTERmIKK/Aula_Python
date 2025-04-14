#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esempi unificati di Ereditarietà in Python.
Mostra:
- Classe base e classi derivate
- Overriding di metodi
- Uso di super()
- Ereditarietà multipla
"""

# ==============================================================
# ESEMPIO 1: CLASSE BASE "Veicolo" E DUE SOTTOCLASSI "Auto" E "Moto"
# ==============================================================

class Veicolo:
    """
    Classe base per i veicoli.
    """
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def accendi_motore(self):
        """
        Metodo di base per l'accensione del motore.
        """
        return f"Motore di {self.marca} {self.modello} acceso."
    
    def descrivi(self):
        """
        Restituisce una stringa descrittiva del veicolo.
        """
        return f"Veicolo di marca {self.marca}, modello {self.modello}"

class Auto(Veicolo):
    """
    Sottoclasse di Veicolo che rappresenta un'automobile.
    """
    def __init__(self, marca, modello, porte):
        # Richiama il costruttore della classe base
        super().__init__(marca, modello)
        self.porte = porte
    
    def accendi_motore(self):
        """
        Esempio di overriding del metodo accendi_motore()
        """
        base_message = super().accendi_motore()
        return base_message + " (Auto) Rumore di un motore a benzina/diesel o elettrico..."
    
    def descrivi(self):
        """
        Sovrascrive descrivi() per aggiungere info sul numero di porte.
        """
        return f"Automobile {self.marca} {self.modello} con {self.porte} porte"

class Moto(Veicolo):
    """
    Sottoclasse di Veicolo che rappresenta una motocicletta.
    """
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.cilindrata = cilindrata
    
    def accendi_motore(self):
        return f"Motore della moto {self.marca} {self.modello} acceso! (Cilindrata {self.cilindrata}cc)"

# ==============================================================
# ESEMPIO 2: FUNZIONE CHE UTILIZZA IL POLIMORFISMO
# ==============================================================

def avvia_veicolo(veicolo):
    """
    Funzione che sfrutta il polimorfismo: richiede un oggetto di tipo 'Veicolo'
    (o derivato) e chiama i suoi metodi, senza preoccuparsi di quale sottoclasse sia.
    """
    print("Descrizione:", veicolo.descrivi())
    print("Accensione:", veicolo.accendi_motore())
    print("---")

# ==============================================================
# ESEMPIO 3: EREDITARIETÀ MULTIPLA (SEMPLICE ESEMPIO)
# ==============================================================

class Elettrico:
    """
    Mixin (o classe base separata) per veicoli elettrici.
    """
    def ricarica_batteria(self):
        return "Batteria in carica..."

class AutoElettrica(Auto, Elettrico):
    """
    Sottoclasse che eredita da Auto e dal mixin Elettrico.
    """
    def accendi_motore(self):
        # Overriding con comportamento specifico per auto elettrica
        base_message = super(Auto, self).accendi_motore()  # chiamata su Veicolo
        return base_message + " (AutoElettrica) Silenziosa all'accensione!"

# ==============================================================
# FUNZIONE PRINCIPALE
# ==============================================================

def main():
    # Creiamo istanze delle varie classi
    v = Veicolo("Generico", "Basic")
    a = Auto("Fiat", "Punto", 5)
    m = Moto("Yamaha", "XMAX", 300)
    ae = AutoElettrica("Tesla", "Model 3", 5)
    
    # Usiamo la funzione polimorfica avvia_veicolo() su ciascuna istanza
    print("=== ESEMPIO DI EREDITARIETA' CON VEICOLO, AUTO, MOTO ===")
    avvia_veicolo(v)
    avvia_veicolo(a)
    avvia_veicolo(m)
    
    print("=== ESEMPIO DI EREDITARIETA' MULTIPLA (AUTO ELETTRICA) ===")
    avvia_veicolo(ae)
    # Usiamo un metodo definito nella classe Elettrico
    print("Ricarica batteria:", ae.ricarica_batteria())

# ==============================================================

if __name__ == "__main__":
    main()
