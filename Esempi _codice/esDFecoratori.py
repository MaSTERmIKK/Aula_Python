def decoratore(funzione):
    def wrapper(*args, **kwargs):
        
        
        print (*args)
        x = args 
        x +=int(input("inserisci un numero"))
        if  x > 0:
            funzione(x) 
        else:
            print("sei un pippo")
    return wrapper






@decoratore
def quadrato(x):
    print(x*x)
    
@decoratore  
def cubo(x):
    print(x*x*x)
    
quadrato(2)
quadrato(-1)