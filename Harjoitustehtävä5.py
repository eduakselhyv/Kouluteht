{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1035{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang11 # Luodaan operaattori, joka py\'f6ritt\'e4\'e4 bin\'e4\'e4rilukua vasemmalle\par
def vasenSuunta(luku, askel):\par
    # Toistetaan askelten m\'e4\'e4r\'e4n verran\par
    for i in range(0, askel, 1):\par
        # Otetaan binn\'e4riluvun ensimm\'e4inen numero (00100, a = 0)\par
        a = luku[0]\par
        # Heitet\'e4\'e4n numero luvun loppuun (001000)\par
        b = luku + a\par
        # Poistetaan ensimm\'e4inen numero, sill\'e4 se on nyt luvun lopussa (01000)\par
        c = b[1:len(luku) + 1]\par
        # Muutetaan luku 00100 luvuksi 01000, jotta seuraavalla toistolla \par
        # se siirt\'e4\'e4 uuden luvun vanhan sijaan.\par
        luku = c\par
        \par
        # Jos t\'e4m\'e4 on viimeinen toisto, tulosta vastaus.\par
        if i + 1 == askel:\par
            print(c)\par
\par
# Luodaan operaattori, joka py\'f6ritt\'e4\'e4 bin\'e4\'e4rilukua vasemmalle\par
def oikeaSuunta(luku, askel):\par
    # Toistetaan askelten m\'e4\'e4r\'e4n verran\par
    for i in range(0, askel, 1):\par
        # Otetaan bin\'e4\'e4riluvun kaikki paitsi viimeinen numero (00100, a = 0010)\par
        a = luku[0:len(luku) - 1]\par
        # Heitet\'e4\'e4n kaikki paitsi viimeinen numero luvun loppuun (001000010)\par
        b = luku + a    \par
        # Poistetaan heitetyt numerot (001000010 > 00010)\par
        c = b[len(luku) - 1:]\par
        # Muutetaan luku 00100 luvuksi 00010, jotta seuraavalla toistolla\par
        # se siirt\'e4\'e4 uuden luvun vanhan sijaan.\par
        luku = c\par
\par
        # Jos t\'e4m\'e4 on viimeinen toisto, tulosta vastaus.\par
        if i + 1 == askel:\par
            print(c)\par
\par
# Pyydet\'e4\'e4n lukua\par
luku = input("Anna luku: ")\par
\par
a = True\par
\par
# Pyydet\'e4\'e4n askelten m\'e4\'e4ri\'e4 (tein huvikseen siten, ett\'e4 sen t\'e4ytyy olla numero)\par
while a:\par
    askel = input("Anna askelten m\'e4\'e4r\'e4: ")\par
    try:\par
        askel = int(askel)\par
        a = False\par
    except:\par
        continue\par
\par
b = True\par
\par
# Pyydet\'e4\'e4n py\'f6rimissuuntaa (Jos vastaus ei ole oikea tai vasen, pyyd\'e4 uudestaan)\par
while b:\par
    suunta = input("Anna py\'f6rimissuunta (Vasen/Oikea): ")\par
    if suunta == "Vasen" or suunta == "vasen" or suunta == "Oikea" or suunta == "oikea":\par
        b = False\par
\par
# Suorita vasenSuunta operaattori, jos suunnaksi annettin vasen\par
if suunta == "Vasen" or suunta == "vasen": \par
    vasenSuunta(luku, askel)\par
\par
# Suorita oikeaSuunta operaattori, jos suunnaksi annettin oikea\par
if suunta == "Oikea" or suunta == "oikea":\par
    oikeaSuunta(luku, askel)\par
}
 