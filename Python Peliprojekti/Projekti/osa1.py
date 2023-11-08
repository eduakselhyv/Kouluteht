import random
import string

def sekoitaLista(luvut):
    a = ""
    for i in range(0, 20, 1):
        b = random.randint(0, len(luvut) - 1)
        a = luvut[b]
        luvut.remove(a)
        luvut.append(a)
    return luvut

def tulostaLista(luvut):
    print(sekoitaLista(luvut))

def xysijainnit(lista):
    for i in range(0, 1000, 1):
        x = random.randint(0,100)
        y = random.randint(0,100)
        x = str(x)
        y = str(y)
        xy = x + ',' + y
        lista.append(xy)
    return lista


# random numero
print(random.randint(1, 10))

# random nopan silmäluku
print("Silmäluku:", random.randint(1, 6))

# random kolikonheitto
kolikko = ["kruuna", "klaava"]
print(random.choice(kolikko))

# random salasana
salasana = ""
for i in range(0, 8, 1):
    salasana = salasana + random.choice(string.ascii_lowercase)
print(salasana)

# random lista
luvut = [1, 2, 3, 4, 5, 6, 7, 8]
sekoitaLista(luvut)
tulostaLista(luvut)

# random vihollisen sijainti
xykoordinaatti = []
print(xysijainnit(xykoordinaatti))

# listan järjestäminen
lista = []
for i in range(0, 10, 1):
    lista.append(random.randint(0,10))
lista.sort()
print(lista)

# pistelista
pelaajalista = []
while True:
    pelaaja = input("Anna pelaaja: ")

    if pelaaja == "lopeta":
        for i in range(0, len(pelaajalista), 1):
            if pelaajalista[i] == min(pelaajalista):
                paraspelaaja = pelaajalista[i - 1] + ","
                paraspiste = pelaajalista[i]
                break
        break

    pisteet = input("Anna pisteet: ")
    pelaajalista.append(pelaaja)
    pelaajalista.append(pisteet)

print (paraspelaaja, paraspiste) 