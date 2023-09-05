# Kysytään, kunnes käyttäjä antaa 4-merkkisen binääriluvun
while True:
    luku = input("Anna 4-bittinen binääriluku: ")
    if len(luku) != 4:
        print("Syötteesi ei ollut nelimerkkinen.")
    elif max(luku) > "1" or min(luku) < "0":
        print("Syötteesi ei ollut binäärinen.")
    else:
        break

# Yksilöidään kaikki bitit toisistaan
lukua = int(luku[0])
lukub = int(luku[1])
lukuc = int(luku[2])
lukud = int(luku[3])

# Muutetaan luku desimaaliin ja printataan se.
desimaali = lukua * 8 + lukub * 4 + lukuc * 2 + lukud * 1
print("Binääriluku", luku, "on desimaalilukuna", desimaali)
