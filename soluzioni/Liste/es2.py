# Esercizio 2
# Realizza un programma che richieda all’utente una riga contenente numeri separati da spazi. 
# Il programma deve leggere quella riga, calcolare la somma di tutti i numeri e stampare il risultato.
#

numeri = input("Inserisci una lista di numeri separati da virgole: ") #"1,2,3,4,5"
numeri = numeri.split(",") #['1', '2', '3', '4', '5']

somma = 0
if len(numeri) == 5:
    somma = int(numeri[0]) + int(numeri[1]) + int(numeri[2]) + int(numeri[3]) + int(numeri[4])
    print(f"La somma  è: {somma}")
else:
    print(f"Hai inserito un numero di valori diverso da 5: len(numero) = {len(numeri)}")