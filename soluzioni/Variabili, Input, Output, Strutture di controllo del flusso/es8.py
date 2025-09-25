#es 8
    
voto = int(input("Inserisci un voto: "))

if voto < 0 or voto > 100:
    print("Valore inserito non valido")
elif voto >= 90 and voto <= 100:
    print("Ottimo")
elif voto >= 80 and voto <= 89:
    print("Distinto")
elif voto >= 70 and voto <= 79:
    print("Buono")
elif voto >= 60 and voto <= 69:
    print("Sufficiente")
elif voto < 60:
    print("Insufficiente")