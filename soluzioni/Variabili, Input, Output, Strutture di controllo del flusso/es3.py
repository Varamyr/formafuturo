# Es. 3 - Pari o dispari
# Chiedere all'utente un numero intero e stampare se è pari o dispari.

numero = int(input("Inserisci un numero intero: "))
resto = numero % 2

if resto == 0:
    print(f"Il numero ({numero}) inserito è PARI.")
else:
    print(f"Il numero ({numero}) inserito è DISPARI.")
