choix = int(input("choisis une base 2, 10, 16 : "))

def B10xB2():
    base = int(input("choisis un nombre base 10 : "))
    quotient = base
    
    while quotient != 0:
        
        quotient = int(base) // 2
        reste = int(base) % 2
        base = quotient
        print(reste)



if choix in (2, 10, 16):
    if choix == 10:
        B10xB2()
    elif choix == 2:
        print("a suivre")
    else:
        print("a suivre")


    print("fin")
else:
    print("erreur base non disponible")
    exit


    
