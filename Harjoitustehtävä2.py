# syöte pyytää merkkijonoa ja alijonoa
merkkijono = input("Anna merkkijono: ")
alijono = input("Anna alijono: ")

# saadaan ensimmäinen esiintymä selville
ensesiin = merkkijono.find(alijono)
# lisätään ensimmäisen esiintymän kohtaan 1, jottei koko alijonoa tule mukaan seuraavaan koodiin
ensesiin = ensesiin + 1
# luodaan uusi merkkijono, joka ei ota mukaan ensimmäistä alijonon esiintymää
ensesiin1 = merkkijono[ensesiin:]
# löydetään alijonon esiintymä uudesta merkkijonosta
toisesiin = ensesiin1.find(alijono)

# lisätään ensimmäisen ja toisen esiintymän kohta toisiinsa, jotta saadaan toisen alijonon esiintymäkohta alkuperäisestä merkkijonosta
kohta = ensesiin + toisesiin

# tulosta vastaus
print("Alijonon", alijono, "toinen esiintymä löytyy merkkijonosta", merkkijono, "indeksistä", kohta, "alkaen.")