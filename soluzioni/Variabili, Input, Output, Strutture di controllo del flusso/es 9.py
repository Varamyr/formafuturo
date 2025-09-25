# es 9
carattere = input("Inserisci un carattere: ")

if len(carattere) > 1:
    print("L'input è troppo lungo, inserisci un solo carattere.")
else:
    if carattere == 'a' or carattere == 'e' or carattere == 'i' or carattere == 'o' or carattere == 'u':
        print("Il carattere è una vocale.")
    else:
        print("Il carattere non è una vocale.")