# Ohjelma toistuu jatkuvasti, jotta käyttäjä voi kysyä monta kertaa.
while True:
    
    # Luodaan muuttuja kala
    kala = True

    # Niin kauan kun kala on tosi, pyydä lukua.
    while kala:
        
        # Pyydä lukua
        luku = input("Anna luku: ")
    
        # Jos syöte sisältää kirjaimia, pyydä käyttäjää antamaan kelpoinen luku. En valitettavasti osaa ohjelmoida ohjelmaa tarkistamaan, jos syöte sisältää erikoismerkkejä, joten niitä syöttäessä tulee errori.
        if luku.isupper() or luku.islower():
            print("Syöte ei ole luku!")
            
        # Jos syöte ei sisällä kirjaimia, päästä käyttäjä jatkamaan muuttamalla muuttuja kala epätodeksi.
        else:
            luku = int(luku)
            onko = True
            kala = False

    # Laske, onko syöte alkuluku.
    for i in range(2, luku, 1):
        if luku % i == 0 or luku == 1:
            onko = False
            break

    # Jos syöte on alkuluku, eli jos muuttuja onko on totta.
    if onko:
        print("Luku on alkuluku.")
        
    # Jos onko on epätosi, niin luku ei ole alkuluku
    else:
        print("Luku ei ollut alkuluku.")