#Base de depart 
choix = int(input("choisis une base 2, 10, 16 : "))
def reset():
    nombre = base
    quotient = nombre
    reset = 0


#verification que la base selectionner est dispo 
if choix in (2, 10, 16):
    #si la base selectionner est la base 10
    if choix == 10:

        base = int(input("choisis un nombre base 10 : "))
        nombre = base
        quotient = nombre

        while quotient != 0:
            quotient = int(nombre) // 2
            reste = int(nombre) % 2
            nombre = quotient
            print(reste)
        reset()
        print("________________")
        reste = base
        dicoHexa = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A", 
            11: "B", 
            12: "C", 
            13: "D", 
            14: "E", 
            15: "F"
        }
        while reste != 0:
            reste = int(nombre) // 16
            #if reste <= 10:
            reste = nombre
            lettre = dicoHexa.get(nombre, '?')
            print(lettre)
                
            


        
        
        
    #si la base selectionner est la base 2
    elif choix == 2:
        print("a suivre")
    #si la base selectionner est la base 16
    else:
        print("a suivre")


    print("fin")
else:
    print("erreur base non disponible")
    exit


    
