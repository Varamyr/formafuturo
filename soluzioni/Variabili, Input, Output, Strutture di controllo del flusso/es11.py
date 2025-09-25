#es 11
var_giorni = int(input("giorni: "))
var_ore = int(input("ore: "))
var_minuti = int(input("minuti: "))

minuti_in_secondi = 60 * var_minuti
ore_in_secondi = 60 * 60 * var_ore
giorni_in_secondi = 24 * 60 * 60 * var_giorni

secondi_totali = minuti_in_secondi + ore_in_secondi + giorni_in_secondi

print(f"{var_giorni} giorni, {var_ore} ore e {var_minuti} minuti")
print("Corrispondono a ", secondi_totali, " secondi")