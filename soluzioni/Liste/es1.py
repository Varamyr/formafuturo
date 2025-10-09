#Esercizio 1
#Scrivi un programma che chieda all’utente di inserire, su una singola riga,
# una sequenza di numeri separati da virgole (es.: 10, 5, 42).
# Il programma deve leggere questa riga e stampare a video la lista dei numeri inseriti (come una struttura dati lista).
#
# 
numeri = input("Inserisci una lista di numeri separati da virgole") #1,2,3,4,5

numeri = numeri.split(",") #[1,2,3,4,5]

print(numeri)