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

#aliohjelmat
import sys


def lukeminen(lista,nimi):

    try:
        tiedosto = open(nimi,"r",encoding="utf-8")
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)
    while True:
        rivi = tiedosto.readline()
        if rivi == "":
            break
        lista.append(rivi[:-1])
    return lista

def analyysi(lista,sanakirja):

    for auto in lista:
        try:
            sanakirja[auto] += 1
        except Exception:
            sanakirja[auto] = 1

    return sanakirja

def tulostus(sanakirja, lista, nimi):
    td = open(nimi, "w", encoding="utf-8")
    print("Tunnistettiin {0} automerkkiä ja {1} autoa:".format(len(sanakirja),len(lista)))
    td.write("Tunnistettiin {0} automerkkiä ja {1} autoa:\n".format(len(sanakirja),len(lista)))
    for i in sanakirja:
        if sanakirja[i]>1:
            print("{0}: {1} autoa".format(i,sanakirja[i]))
            td.write("{0}: {1} autoa\n".format(i,sanakirja[i]))
        else:
            print("{0}: {1} auto".format(i,sanakirja[i]))
            td.write("{0}: {1} auto\n".format(i, sanakirja[i]))
    td.close()
    return None

def paaohjelma():
    lista = []
    sanakirja = {}
    luNImi = input("Anna luettavan tiedoston nimi: ")
    kirNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    lista = lukeminen(lista,luNImi)
    if lista == []:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        sanakirja = analyysi(lista,sanakirja)
        tulostus(sanakirja,lista,kirNimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()