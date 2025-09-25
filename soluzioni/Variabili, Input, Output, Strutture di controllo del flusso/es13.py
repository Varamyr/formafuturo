#es 13
import math

print("1 - Area cerchio")
print("2 - Area quadrato")
print("3 - Area rettangolo")
print("4 - Area triangolo")
scelta = int(input("Inserisci il numero di un'operazione: "))

if scelta == 1:
    raggio = int(input("Inserisci il valore del raggio: "))
    area = math.pi * (raggio**2)
    print("L'area del cerchio è ", area)
elif scelta == 2:
    lato = int(input("Inserisci il valore del lato: "))
    area = lato**2
    print("L'area del quadrato è ", area)
elif scelta == 3:
    lato1 = int(input("Inserisci il valore del lato 1: "))
    lato2 = int(input("Inserisci il valore del lato 2: "))
    area = lato1  * lato2
    print("L'area del quadrato è ", area)
elif scelta == 4:
    base = int(input("Inserisci il valore dell': "))
    altezza = int(input("Inserisci il valore del lato 2: "))
    area = (base  * altezza)/2
    print("L'area del triangolo è ", area)
else:
    print("Il valore inserito non è riconosciuto.")