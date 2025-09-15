# Es. 5 - Calcolo pagine
# Dato il numero di elementi e numero di elementi per pagina, calcolare quante pagine servono.

elementi = int(input("Inserisci il numero totale di elementi: "))
max_elem_pagina = int(input("Inserisci il massimo numero di elementi per pagina: "))

pagine = elementi // max_elem_pagina
resto = elementi % max_elem_pagina

if resto > 0:
    pagine = pagine + 1
    
print("Il numero di pagine necessarie è: ", pagine)