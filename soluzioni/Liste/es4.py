# Esercizio 4
#Chiedere all'utente di inserire una riga di 5 numeri separata da spazi.
#Se ci sono duplicati all'interno della riga rimuoverli.

numeri = input("Inserisci una lista di numeri separati da virgole: ") # "1,1,2,2,5"
numeri = numeri.split(",") # ["1", "1", "2", "5", "2"]

if len(numeri) > 5:
    print("Hai inserito troppi numeri.")
elif len(numeri) < 5:
    print("Hai inserito pochi numeri.")
else:
    num1 = numeri[0]
    num2 = numeri[1]
    num3 = numeri[2]
    num4 = numeri[3]
    num5 = numeri[4]
    
    if numeri.count(num1) > 1:
        numeri.pop(numeri.index(num1))
        
    if numeri.count(num2) > 1:
        numeri.pop(numeri.index(num2))
        
    if numeri.count(num3) > 1:
        numeri.pop(numeri.index(num3))
        
    if numeri.count(num4) > 1:
        numeri.pop(numeri.index(num4))
        
    if numeri.count(num5) > 1:
        numeri.pop(numeri.index(num5))
        
print(f"{numeri}")