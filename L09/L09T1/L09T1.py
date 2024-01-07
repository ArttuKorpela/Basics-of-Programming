######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:11.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################



#Aliohjelmat
import sys


def lukeminen(lista):
    lista.clear()
    nimi = input("Anna luettavan tiedoston nimi: ")
    try:
        tiedosto = open(nimi,"r",encoding="utf-8")
        while  True:
            rivi = tiedosto.readline()
            if rivi == "":
                tiedosto.close()
                break
            else:
                lista.append(int(rivi))
        print("Tiedoston '{0}' lukeminen onnistui, {1} riviä.".format(nimi,len(lista)))
        return lista
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(nimi))

        sys.exit(0)

def kirjoittaminen(lista):

    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(nimi, "w", encoding="utf-8")
        for i in lista:
            tiedosto.write("{0}\n".format(i))

        tiedosto.close()
        print("Tiedoston '{0}' kirjoittaminen onnistui.".format(nimi))
        return None

    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(nimi))

    sys.exit(0)

#paaohjelma

def paaohjelma():

    numeroilista = []

    numeroilista=lukeminen(numeroilista)
    kirjoittaminen(numeroilista)
    print("Kiitos ohjelman käytöstä.")

    numeroilista.clear()
    return None

paaohjelma()

#L09T1
#EOF