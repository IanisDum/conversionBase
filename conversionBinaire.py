
base = input("choisis un nombre base 10 : ")
reste = 0
quotient = None

while quotient != 0:
    quotient = int(base) // 2
    reste = int(base) % 2
    base = quotient
    print(reste)


print("fin")

#fais par ianis (marche nickel)