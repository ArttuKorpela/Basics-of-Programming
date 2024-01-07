######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:20.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L10T2
import sys


def lue(sanakirja, tdnimi):
    try:
        tiedosto = open(tdnimi,"r",encoding="utf-8")
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(tdnimi))
        sys.exit(0)
    tiedosto.readline()
    while True:
        rivi = (tiedosto.readline()).split(";")

        if rivi == [""]:
            break
        vuosi = int((rivi[1])[0:4])
        try:
            sanakirja[vuosi] += 1
        except Exception:
            sanakirja[vuosi] = 1
    return sanakirja

def tulostus(sanakirja):
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")

    summa = 0
    for i in sorted(sanakirja,reverse=True):
        print("{0}: {1}".format(i,sanakirja[i]))
        summa += sanakirja[i]
    print("Yhteensä {0} autoa.".format(summa))
    return None
def paaohjelma():
    sanakirja = {}

    tdnimi = input("Anna luettavan tiedoston nimi: ")
    sanakirja = lue(sanakirja,tdnimi)
    tulostus(sanakirja)
    print("Kiitos ohjelman käytöstä.")
paaohjelma()