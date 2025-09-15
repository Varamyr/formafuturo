# Es. 4 – Verifica età
# Chiedere l'età e stampare 'puoi guidare' se è uguale o superiore 18, altrimenti 'non puoi guidare’. 

eta = int(input("Inserisci la tua età: "))
if eta >= 18:
    print("Puoi guidare.")
else:
    print(f"Non puoi guidare, ti mancano {18 - eta} anni.")
