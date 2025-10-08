#es1
#Scrivi un programma che chieda all'utente di inserire una parola. Il programma deve stampare:
#Quanti caratteri ha la parola, se il primo carattere è una vocale (a, e, i, o, u), se l'ultimo carattere è un numero, se la parola inizia con una lettera maiuscola. (stringa.isupper() per verificare se maiuscola, txt.isdigit() per verificare se numero)


parola = input("Inserisci una parola: ")
print(f"La parola inserita ha: {len(parola)} caratteri.")

vocali = "aeiou"

if parola[0] in vocali:
    print(f"La prima lettera è una vocale.")
else:
    print(f"La prima lettera è una consonante.")
    
if parola[-1].isdigit():
    print(f"L'ultima lettera è un numero.")

if parola[0].isupper():
    print(f"La prima lettera è maiuscola.")