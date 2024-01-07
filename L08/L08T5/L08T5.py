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
import L08T5Kirjasto
#paaohjelma

def paaohjelma():

    luetutrivit = []
    taltiedot = []

    kir_tied_nimi = ""
    lue_tied_nimi = ""

    while True:
        valinta = L08T5Kirjasto.valikko()

        if valinta == 1:
            lue_tied_nimi = L08T5Kirjasto.kysyTied("luettavan", lue_tied_nimi)
            luetutrivit = L08T5Kirjasto.lueTiedosto(lue_tied_nimi, luetutrivit)

        elif valinta == 2:
            taltiedot = L08T5Kirjasto.analyysi(luetutrivit)

        elif valinta == 3:
            kir_tied_nimi = L08T5Kirjasto.kysyTied("kirjoitettavan", kir_tied_nimi)
            L08T5Kirjasto.kirjoitus(kir_tied_nimi, taltiedot)

        elif valinta == 0:
            L08T5Kirjasto.lopetus()
            break
    return None


paaohjelma()
#L08T5.py
#EOF