import math 

# syöte pyytää a, b ja c arvoja
a = input("Anna a: ")
b = input("Anna b: ")
c = input("Anna c: ")

# muuta annetut arvot luvuiksi
a = int(a)
b = int(b)
c = int(c)

# lasketaan arvo, jos ± käytetään + merkkiä
juuri1 = ((b * -1) + (math.sqrt((b ** 2) - 4 * a * c))) / (2 * a)
# lasketaan arvo, jos ± käytetään - merkkiä
juuri2 = ((b * -1) - (math.sqrt((b ** 2) - 4 * a * c))) / (2 * a)

# tulosta vastaukset
print("Juuret ovat", juuri1, "ja", juuri2)