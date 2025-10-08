#es5
#Chiedi all’utente di digitare una frase di 5 parole.
#Il programma deve stampare quante parole ci sono nella frase e quale è la parola più lunga (stampa solo il testo della parola più lunga).
frase = input("Inserisci una frase di 5 parole: ")

parole = frase.split()

if len(parole) != 5:
    print("La frase inserita non è della lunghezza corretta.")
else:
    parola_lunga = max(parole, key=len)
    print(parola_lunga)