import random

while True:    
    
    # Pyydetään lottoriviä ja arpojen määriä
        lottorivi = input("Anna Lottorivi:")
        arpamäärä = input("Anna arvottavien rivien määrä:")
    
    # Luodaan muuttujat, jotka pitävät kirjaa siitä montako kertaa
    # on saanut joko 4, 5, 6, tai 7 oikein.
    b = 0
    c = 0
    d = 0
    e = 0
    
    # Muutetaan merkkijono lottorivistä lista.
    lottorivi = list(lottorivi.split(","))
    
    # Arvotaan yhtä monta kertaa kun arpamääriä annettiin.
    for i in range(0, int(arpamäärä), 1):
        
        # Luodaan uusi joukko, joukko listan sijaan siksi, ettei tule duplikaatteja.
        lottonumerot = set()
        a = 0
        
        # Arvotaan oikeat loton numerot
        while len(lottonumerot) < 7:
            lottonumero = random.randint(1,39)
            lottonumerot.add(lottonumero)
        
        # Tarkastetaan montako numeroa käyttäjä sai oikein lotosta
        for g in range(0, 7, 1):
            if int(lottorivi[g]) in lottonumerot:
                # Jokaisesta oikeasta numerosta muuttuja a nousee yhdellä.
                # Tämä tarkistaa lopuksi montako numeroa sai oikein.
                a = a + 1
        
        # Jos lotosta sai 4, 5, 6 tai 7 numeroa oikein, lisää se lopullisiin tuloksiin
        if a == 4:
            b = b + 1
            
        if a == 5:
            c = c + 1
        
        if a == 6:
            d = d + 1
            
        if a == 7:
            e = e + 1
            
    # Kun kaikki arvat on käyty läpi, näytyä lopputulokset.
    print(b, "kertaa 4 oikein")
    print(c, "kertaa 5 oikein")
    print(d, "kertaa 6 oikein")
    print(e, "kertaa 7 oikein")