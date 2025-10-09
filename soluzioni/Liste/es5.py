# Esercizio 5
# Scrivi un programma che chieda all’utente di inserire una frase e poi stampi la stessa frase
# con l’ordine delle parole invertito (l’ultima parola diventa la prima, e così via).
#
# 
frase = input("Inserisci una frase: ") #"ciao mondo come mi diverto"
frase = frase.split() # ["ciao", "mondo", "come", "mi", "diverto"]

print(frase[-1], frase[-2], frase[-3], frase[-4], frase[-5])

print(" ".join(frase[::-1]))