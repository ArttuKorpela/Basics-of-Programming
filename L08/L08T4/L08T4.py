######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:03.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import L08T4Kirjasto

#paaohjelma

def paaohjelma():
    class TULOS:
        pieninarvo = ""
        suurinarvo = ""
        summa = ""
        keskiarvo = ""

    tulos=TULOS()

    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    valinta = 0
    b = ""
    c = ""
    luettavatiedosto=""
    while True:
        valinta = L08T4Kirjasto.valikko()
        if valinta == 1:
            
            a = "Luettavan"
            Lukutiedosto = L08T4Kirjasto.kysyTied(a, b)
            if Lukutiedosto != "":
                b = Lukutiedosto

            luettavatiedosto = b

            lista = L08T4Kirjasto.lueTiedosto(luettavatiedosto)
            print("Tiedosto '{0}' luettu.\n".format(luettavatiedosto))

        elif valinta == 2:
            tulos = L08T4Kirjasto.analyysi(tulos,lista)
            print("Analyysi suoritettu.\n")

        elif valinta == 3:

            a = "Kirjoitettavan"
            KirjoitettavaTiedosto = L08T4Kirjasto.kysyTied(a, c)
            if KirjoitettavaTiedosto != "":
                c = KirjoitettavaTiedosto
            kirjoitettavatiedosto = c

            L08T4Kirjasto.kirjoitus(kirjoitettavatiedosto,tulos)

            print("Tulokset kirjoitettu tiedostoon.\n")

        elif valinta == 0:

            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
    print()
    print("Kiitos ohjelman käytöstä.")

    return None

paaohjelma()

#L08T4.py
#EOF