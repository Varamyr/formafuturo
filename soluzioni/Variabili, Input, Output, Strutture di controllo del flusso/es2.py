# Es. 2 - Somma di tre numeri
# Chiedere 3 numeri all’utente (possono essere float) e stampare la somma e la media.

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

somma = n1 + n2 + n3
media = somma / 3

print(f"La somma è: {somma} \nLa media è: {media}")
