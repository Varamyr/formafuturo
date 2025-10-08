# #es3
#Sviluppa un programma che chieda all'utente di inserire una parola di esattamente 5 caratteri. Il programma deve verificare se la parola è simmetrica (palindroma) confrontando manualmente:
#Il primo carattere con l'ultimo, il secondo carattere con il penultimo, ecc.. fino al centro della parola. 
#Alla fine stampare "È simmetrica" oppure "Non è simmetrica". Ignora le differenze tra maiuscole e minuscole.

parola = input("Inserisci una parola di 5 caratteri: ").lower()

if len(parola) != 5:
    print("La parola non è di 5 caratteri.")
else:
    if parola[0] == parola[-1] and parola[1] == parola[-2]:
        print("La parola è palindroma")
    else:
        print("La parola non è palindroma")
