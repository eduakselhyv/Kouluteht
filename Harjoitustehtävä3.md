# Luodaan muuttuja a
a = True

# Niin kauan kuin muuttuja a on tosi,
while a:
    # Pyytää 4-bittistä binäärilukua
    luku = input("Anna 4-bittinen binääriluku: ")
    # Tarkistaa, onko syöte on nelimerkkinen
    if len(luku) != 4:
        print("Syötteesi ei ollut nelimerkkinen.")
    # Tarkistaa, onko syöte binääriä
    elif luku[0] != "1" and luku[0] != "0":
        print("Syötteesi ei ollut binäärinen")
    elif luku[1] != "1" and luku[1] != "0":
        print("Syötteesi ei ollut binäärinen")
    elif luku[2] != "1" and luku[2] != "0":
        print("Syötteesi ei ollut binäärinen")
    elif luku[3] != "1" and luku[3] != "0":
        print("Syötteesi ei ollut binäärinen")
    # Jos syöte on nelimerkkinen ja binääriä, lopeta toisto muuttamalla a epätodeksi
    else:
        a = False

# Muuta annettu syöte yksittäisiksi luvuiksi, jotta sen desimaalimuoto voidaan laskea
lukua = int(luku[0])
lukub = int(luku[1])
lukuc = int(luku[2])
lukud = int(luku[3])

# Laske annetun binäärin desimaaliarvo
desimaali = lukua * 8 + lukub * 4 + lukuc * 2 + lukud * 1
# Tulosta arvo
print("Binääriluku", luku, "on desimaalilukuna", desimaali)
