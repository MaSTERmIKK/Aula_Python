
"""
Esempi unificati di incapsulamento in Python:
- attributi 'privati' tramite convenzione (_ e __)
- uso di property (getter e setter)
- metodi pubblici vs metodi 'nascosti'
"""

# ==============================================================
# ESEMPIO 1: PERSONA CON ATTRIBUTE MANGEMENT (GETTER, SETTER)
# ==============================================================

class Persona:
    """
    Classe che dimostra un uso "classico" dell'incapsulamento in Python
    con getter e setter, tramite property.
    """
    def __init__(self, nome, eta):
        self._nome = nome     # Convenzione: attributo "protetto"
        self._eta = eta       # Convenzione: attributo "protetto"
    
    @property
    def nome(self):
        """
        Getter per il nome (uso della property).
        """
        return self._nome
    
    @nome.setter
    def nome(self, nuovo_nome):
        """
        Setter per il nome (uso della property).
        Qui possiamo aggiungere logiche di validazione.
        """
        if not nuovo_nome:
            raise ValueError("Il nome non può essere vuoto.")
        self._nome = nuovo_nome
    
    @property
    def eta(self):
        """
        Getter per l'età (property).
        """
        return self._eta
    
    @eta.setter
    def eta(self, nuova_eta):
        """
        Setter per l'età.
        """
        if nuova_eta <= 0:
            raise ValueError("L'età non può essere negativa.")
        self._eta = nuova_eta
    
    def descrivi(self):
        """
        Metodo pubblico per descrivere la Persona.
        """
        return f"Persona: {self._nome}, età: {self._eta}"


# ==============================================================
# ESEMPIO 2: CONTO BANCARIO CON INCAPSULAMENTO
# ==============================================================

class ContoBancario:
    """
    Classe che illustra l'uso del double underscore per "nascondere"
    effettivamente un attributo, e l'uso di metodi pubblici
    per controllarne l'accesso.
    """
    def __init__(self, intestatario, saldo_iniziale=0.0):
        self.intestatario = intestatario
        # Double underscore: Python "offusca" (name mangling) l'attributo
        self.__saldo = saldo_iniziale

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo da depositare deve essere positivo.")
        self.__saldo += importo

    def preleva(self, importo):
        if importo <= 0:
            raise ValueError("L'importo da prelevare deve essere positivo.")
        if importo > self.__saldo:
            raise ValueError("Saldo insufficiente per il prelievo.")
        self.__saldo -= importo

    def get_saldo(self):
        """
        Metodo pubblico per leggere il saldo, senza dare
        accesso diretto all'attributo interno __saldo.
        """
        return self.__saldo

    def descrivi(self):
        return f"Conto di {self.intestatario}, saldo: {self.__saldo:.2f} €"

    def _metodo_interno(self):
        """
        Convenzione di underscore singolo per indicare
        un metodo "interno" (non pensato per l'uso esterno).
        """
        # In pratica non viene impedito l'accesso,
        # ma è una convenzione d'uso.
        return "Metodo 'interno' di ContoBancario." + self.__metodo_interno2()
    
    def __metodo_interno2(self):
        """
        Convenzione di underscore singolo per indicare
        un metodo "interno" (non pensato per l'uso esterno).
        """
        # In pratica non viene impedito l'accesso,
        # ma è una convenzione d'uso.
        return "Metodo 'interno' di ContoBancario."


# ==============================================================
# ESEMPIO 3: UTILIZZO DI GETTER, SETTER E ATTRIBUTI 'PRIVATI'
# ==============================================================

def main():
    print("=== ESEMPIO 1: INCAPSULAMENTO IN 'Persona' CON PROPERTY ===")
    p = Persona("Mario", 30)
    print(p.descrivi())
    
    # Modifichiamo attributi tramite property
    p.nome = "Luigi"
    p.eta = 40
    print("Dopo aggiornamento property:", p.descrivi())
    
    # Se proviamo a impostare un valore scorretto, otteniamo un ValueError
    try:
        p.eta = -10
    except ValueError as e:
        print("Errore nell'impostazione di eta:", e)
    
    print("\n=== ESEMPIO 2: CONTO BANCARIO CON __saldo PRIVATO ===")
    conto = ContoBancario("Anna", 1000.0)
    print(conto.descrivi())
    
    # Depositare una somma
    conto.deposita(500)
    print("Dopo deposito di 500:", conto.descrivi())
    
    # Prelevare una somma
    conto.preleva(300)
    print("Dopo prelievo di 300:", conto.descrivi())
    
    # Accesso al saldo tramite metodo apposito
    print("Saldo attuale (via get_saldo()):", conto.get_saldo())
    
    # Tentativo di accedere direttamente a __saldo: non esiste come attributo pubblico
    # print(conto.__saldo)  # -> causerebbe un AttributeError
    # Python lo rende disponibile come _ContoBancario__saldo in maniera "nascosta"
    
    # Esempio di chiamata ad un metodo "interno"
    # convenzione _metodo_interno (non impedisce l'accesso, ma sconsiglia di usarlo)
    interno = conto._metodo_interno()
    print("Chiamata al metodo interno:", interno)


if __name__ == "__main__":
    main()
