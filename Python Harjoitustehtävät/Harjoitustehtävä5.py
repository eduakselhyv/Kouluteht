while True:
    def vasenSuunta(luku, askel):
        for i in range(0, askel, 1):
            a = luku[0]
            b = luku + a
            c = b[1:len(luku) + 1]

            luku = c

            if i + 1 == askel:
                print(c)

    def oikeaSuunta(luku, askel):
        for i in range(0, askel, 1):
            a = luku[0:len(luku) - 1]
            b = luku + a    
            c = b[len(luku) - 1:]

            luku = c

            if i + 1 == askel:
                print(c)

    luku = input("Anna luku: ")

    a = True

    while a:
        askel = input("Anna askelten määrä: ")
        try:
            askel = int(askel)
            a = False
        except:
            continue

    b = True

    while b:
        suunta = input("Anna pyörimissuunta (Vasen/Oikea): ")
        if suunta == "Vasen" or suunta == "vasen" or suunta == "Oikea" or suunta == "oikea":
            b = False

    if suunta == "Vasen" or suunta == "vasen": 
        vasenSuunta(luku, askel)

    if suunta == "Oikea" or suunta == "oikea":
        oikeaSuunta(luku, askel)
