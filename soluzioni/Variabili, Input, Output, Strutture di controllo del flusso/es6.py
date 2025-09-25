#es 6
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if n1 >= n2 and n1 >= n3:
    print("n1 è il maggiore")
else:
    #n1 non è il maggiore
    if n2 >= n3:
        print("n2 è il maggiore")
    else:
        #n2 non è il maggiore
        print("n3 è il maggiore")