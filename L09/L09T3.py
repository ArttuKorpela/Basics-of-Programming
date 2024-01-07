######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä 14.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
import sys


def nimi(kehote):
    return input("Anna {} tiedoston nimi: ".format(kehote))

def lue(nimi,lista):
    lista.clear()
    n=0
    auto = None
    vanha_auto= None
    try:
        tiedosto = open(nimi,"r",encoding="utf-8")
        while True:
            auto = (tiedosto.readline())[:-1]
            if auto == "":
                break
            if auto != vanha_auto:
                vanha_auto = auto
                lista.append(vanha_auto)
        if lista == []:
            print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
            print("Kiitos ohjelman käytöstä.")
            sys.exit(0)

        return lista
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)


def analyysi(lista):

    print("Tiedostossa oli {} eri automerkkiä.".format(len(lista)))
    return None

def kirjoitus(lista,nimi):

    tiedosto = open(nimi,"w",encoding="utf-8")
    for auto in lista:
        print(auto)
        tiedosto.write(f"{auto}\n")
    tiedosto.close()
    print("Kiitos ohjelman käytöstä.")

def paaohjelma():

    autolista = []

    lnimi = nimi("luettavan")
    knimi = nimi("kirjoitettavan")
    autolista = lue(lnimi,autolista)
    analyysi(autolista)
    kirjoitus(autolista,knimi)

paaohjelma()

#eof