#es2
#Il programma deve stampare la stessa frase in 4 modi diversi:
#Tutto in maiuscolo, tutto in minuscolo, con la prima lettera di ogni parola maiuscola, solo con la prima lettera della frase
#maiuscola e il resto minuscolo. (Usare stringa.upper(), stringa.lower(), stringa.title(), stringa.capitalize())
#     
frase = input("Inserisci una frase: ")

frase_maiuscola = frase.upper()
frase_minuscola = frase.lower()
frase_titolo = frase.title()
frase_prima_lettera_maisc = frase.capitalize()


print(frase_maiuscola)
print(frase_minuscola)
print(frase_titolo)
print(frase_prima_lettera_maisc)