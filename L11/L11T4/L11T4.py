######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:25.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L11T4

import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    #####################################################
    # Lisää tarvittava koodi tämän kommentin alapuolelle.
    try:
        tiedosto = open(Nimi,"r",encoding="utf-8")
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    rivi = int(tiedosto.readline())
    pienin = rivi
    suurin = rivi

    while True:
        rivistr = tiedosto.readline()
        if rivistr == "":
            break
        rivi = int(rivistr)
        if rivi > suurin:
            suurin = rivi
            if (pienin*3) < suurin:
                Luvut.Suurempi = suurin
                Luvut.Pienempi = pienin
                break
        elif rivi < pienin:
            pienin = rivi
            if (pienin*3) < suurin:
                Luvut.Suurempi = suurin
                Luvut.Pienempi = pienin
                break
        else:
            continue

    # Lisää tarvittava koodi tämän kommentin yläpuolelle.
    #####################################################
    return Luvut

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
###########################################################################
# eof
