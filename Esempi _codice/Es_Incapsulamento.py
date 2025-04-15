class Encapsulated:
    def __init__(self, name, age):
        # Imposta gli attributi interni
        self._name = name
        self._age = age

    def __getattribute__(self, attr):
        # Intercetta ogni accesso agli attributi
        print(f"__getattribute__: Accesso a '{attr}'")
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        # Chiamato solo se l'attributo non esiste
        print(f"__getattr__: '{attr}' non trovato, restituisco None")
        return None

    def __setattr__(self, attr, value):
        # Controlla ogni assegnazione agli attributi
        print(f"__setattr__: Impostazione di '{attr}' a {value}")
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        # Controlla l'eliminazione degli attributi
        print(f"__delattr__: Eliminazione dell'attributo '{attr}'")
        object.__delattr__(self, attr)

    @property
    def name(self):
        # Getter per la proprietà 'name'
        print("property getter: Recupero 'name'")
        return self._name

    @name.setter
    def name(self, value):
        # Setter per la proprietà 'name'
        print("property setter: Imposto 'name' a", value)
        self._name = value

    @name.deleter
    def name(self):
        # Deleter per la proprietà 'name'
        print("property deleter: Eliminazione di 'name'")
        del self._name


if __name__ == '__main__':
    print("Creazione dell'oggetto Encapsulated:")
    obj = Encapsulated("Alice", 30)
    print()

    # Accesso diretto tramite property e attributo
    print("Accesso a 'name' tramite property:")
    print(obj.name)  # Attiva __getattribute__ e il getter della property
    print()

    print("Accesso diretto a '_age':")
    print(obj._age)  # Attiva __getattribute__
    print()

    # Accesso ad un attributo inesistente per attivare __getattr__
    print("Tentativo di accesso a 'salary' (non esistente):")
    print(obj.salary)
    print()

    # Uso dei built-in getattr, setattr, hasattr, delattr
    print("Uso di hasattr per 'name':", hasattr(obj, "name"))
    print("Uso di getattr per 'name':", getattr(obj, "name"))
    print()

    print("Uso di setattr per aggiornare 'name' a 'Bob':")
    setattr(obj, "name", "Bob")  # Attiva __setattr__ e il setter della property
    print("Nome aggiornato:", obj.name)
    print()

    print("Uso di delattr per eliminare l'attributo '_age':")
    delattr(obj, "_age")  # Attiva __delattr__
    print("Tentativo di accesso a '_age' dopo eliminazione:",
          getattr(obj, "_age", "Non trovato"))
    print()

    print("Uso del deleter della property 'name':")
    del obj.name  # Attiva il deleter della property, e di conseguenza __delattr__
    print("Tentativo di accesso a 'name' dopo eliminazione:",
          getattr(obj, "name", "Non trovato"))
