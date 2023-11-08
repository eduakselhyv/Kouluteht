# Tuodaan kirjasto Random, jotta voidaan luoda random lista.
import random

# Luodaan muuttuja "i" ja tyhjä lista "lista".
i = 0
lista = []

# Luodaan random lista.
while i < random.randint(3, 10):
    listanumero = random.randint(1, 9)
    lista.append(listanumero)
    i = i + 1

# Järjestetään lista, ja tulostetaan se.
lista.sort()
print("Alkuperäinen Lista:", lista)

# Luodaan listasta joukko, sillä se poistaa kaikki duplikaatit. 
# Lopuksi muutetaan siitä taas lista.
lista = list(set(lista))

# Tulostetaan uusi versio listasta.
print("Lista ilman duplikaatteja:", lista)