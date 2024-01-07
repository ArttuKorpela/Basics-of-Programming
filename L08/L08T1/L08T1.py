######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:02.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import math
import random

#aliohjelmat

def valinta():
    print("Mitä haluat tehdä?")
    print("1) Laske absoluuttinen arvo\n2) Laske kertoma\n3) Laske potenssi\n4) Laske neliöjuuri\n5) Arvo satunnaisluku\n0) Lopeta")
    valinta=int(input("Anna valintasi: "))
    return valinta

def absoluuttinenArvo():
    arvo=float(input("Minkä luvun absoluuttinen arvo selvitetään: "))
    luku=math.fabs(arvo)
    print("Luvun absoluuttinen arvo on {0:.1f}\n".format(luku,))
    return None
    

def kertoma():
    arvo=int(input("Minkä luvun kertoma lasketaan: "))
    luku=math.factorial(arvo)
    print("Luvun kertoma on {0}\n".format(luku))
    return None

def potenssi():
    alakerta=float(input("Mikä luku korotetaan potenssiin: "))
    ylakerta=float(input("Mitä eksponenttia käytetään: "))
    tulos=math.pow(alakerta,ylakerta)
    print("Luku korotettuna eksponenttiin on {0:.1f}\n".format(tulos))
    return None

def neliojuuri():
    arvo=float(input("Mikä luvun neliöjuuri lasketaan: "))
    luku=math.sqrt(arvo)
    print("Luvun neliöjuuri on {0:.1f}\n".format(luku))
    return None

def satunnaisluku():
    print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
    minimi=int(input("Anna minimi (otetaan mukaan): "))
    maksimi=int(input("Anna maksimi (otetaan mukaan): "))
    luku=random.randint(minimi,maksimi)
    print("Arvottiin satunnaisluku {0}\n".format(luku))
    return None

def lopetus():
    print("Lopetetaan\n")
    print("Kiitos ohjelman käytöstä.")
    return None

#paaohjelma

def paaohjelma():
    random.seed(1)
    while True:
        n=valinta()

        if n==1:
            absoluuttinenArvo()
        elif n==2:
            kertoma()
        elif n==3:
            potenssi()
        elif n==4:
            neliojuuri()
        elif n==5:
            satunnaisluku()
        elif n==0:
            lopetus()
            break

paaohjelma()
            



#L08T1.py
#EOF
