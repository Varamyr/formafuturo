#es4
frase = input("Inserisci una frase: ").lower()
parola = input("Inserisci una parola da censurare: ").lower()

lunghezza_parola = len(parola)
censura = "*" * lunghezza_parola

frase_censurata = frase.replace(parola, censura)

print(frase_censurata)