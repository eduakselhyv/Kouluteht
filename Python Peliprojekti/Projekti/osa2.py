# Importataan pygame ja random, jotta niitä voidaan käyttää
import pygame
import random

# Asetetaan ruudun koko ja sen nimi.
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")
# Kaksi muuttujaa, x ja y (tiedän, että voisin laittaa ne 
# suoraan funktioon piirraKuva, mutta yhdessä tehtävän osassa käskettiin
# käyttämään kuvan nimeä, x ja y koordinaattia funktiossa)
x = 0
y = 0

# Arvotaan sijainti joka kerralla kun funktiota haetaan
def piirraKuva(kuva, xkoord, ykoord): 
    xkoord = random.randint(0, 640)
    ykoord = random.randint(0, 400)
    kuva = pygame.image.load(kuva).convert()
    naytto.blit(kuva, (xkoord, ykoord))

# Peli
def main():
    # Jos pygame suljetaan, lopeta While loop
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        # Luo X ruudulle tehtävänannon mukaisesti
        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 255, 0), (0, 400), (640, 0))
        pygame.draw.line(naytto, (0, 0, 255), (0, 0), (640, 400))

        # Käytetään aikaisemmin luotua funktiota piirraKuva
        piirraKuva("pelihahmo.png", x, y)

        # Tulosta tapahtumat näytölle
        pygame.display.flip()

main()