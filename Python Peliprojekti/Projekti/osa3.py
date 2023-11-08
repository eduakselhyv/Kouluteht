import pygame
import random

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset):
    päähahmo = hahmot[0]

    for vihollinen in viholliset:
        if päähahmo[1] == vihollinen[1] and päähahmo[2] == vihollinen[2]:
            del hahmot[0]

    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT and päähahmo[1] < 640:
            päähahmo[1] += 20

            for vihollinen in viholliset:
                if vihollinen[1] > päähahmo[1]:
                    vihollinen[1] -= 10
                else: 
                    vihollinen[1] += 10

                if vihollinen[2] > päähahmo[2]:
                    vihollinen[2] -= 10
                else: 
                    vihollinen[2] += 10
        
        elif tapahtuma.key == pygame.K_LEFT and päähahmo[1] > 0:
            päähahmo[1] -= 20

            for vihollinen in viholliset:
                if vihollinen[1] > päähahmo[1]:
                    vihollinen[1] -= 10
                else: 
                    vihollinen[1] += 10

                if vihollinen[2] > päähahmo[2]:
                    vihollinen[2] -= 10
                else: 
                    vihollinen[2] += 10

        elif tapahtuma.key == pygame.K_UP and päähahmo[2] > 0:
            päähahmo[2] -= 20

            for vihollinen in viholliset:
                if vihollinen[1] > päähahmo[1]:
                    vihollinen[1] -= 10
                else: 
                    vihollinen[1] += 10

                if vihollinen[2] > päähahmo[2]:
                    vihollinen[2] -= 10
                else: 
                    vihollinen[2] += 10

        elif tapahtuma.key == pygame.K_DOWN and päähahmo[2] < 400:
            päähahmo[2] += 20

            for vihollinen in viholliset:
                if vihollinen[1] > päähahmo[1]:
                    vihollinen[1] -= 10
                else: 
                    vihollinen[1] += 10

                if vihollinen[2] > päähahmo[2]:
                    vihollinen[2] -= 10
                else: 
                    vihollinen[2] += 10

def main():
    kissahahmo = ["pelihahmo.png", 100, 100, False]
    hahmot = [kissahahmo]
    rumilus = ["pahahahmo.png", random.randint(0, 640), random.randint(0, 400), False]
    rumilus1 = ["pahahahmo.png", random.randint(0, 640), random.randint(0, 400), False]
    rumilus2 = ["pahahahmo.png", random.randint(0, 640), random.randint(0, 400), False]
    viholliset = [rumilus, rumilus1, rumilus2]

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)


main()