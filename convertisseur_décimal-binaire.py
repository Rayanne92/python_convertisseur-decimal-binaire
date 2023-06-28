def convertir(n): # On va procéder à une division euclidienne | 'def' est une fonction
    if n > 1:
        convertir(n // 2) # // c'est le quotien de la division euclidienne
    print(n % 2, end='') # % c'est le reste de la division euclidienne

nbr = int(input("Entrez un nombre decimal : "))
convertir(nbr)