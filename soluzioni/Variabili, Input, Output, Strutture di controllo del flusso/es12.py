#es 12
secondi = int(input("Inserisci il numero di secondi: "))

giorni_in_secondi = 24*60*60
ore_in_secondi = 60*60
minuti_in_secondi = 60

giorni = secondi // giorni_in_secondi
resto = secondi % giorni_in_secondi

ore = resto // ore_in_secondi
resto = resto % ore_in_secondi

minuti = resto // minuti_in_secondi
resto = resto % minuti_in_secondi

print(f"{secondi} secondi equivalgono a {giorni} giorni, {ore} ore, {minuti} minuti e {resto} secondi.")