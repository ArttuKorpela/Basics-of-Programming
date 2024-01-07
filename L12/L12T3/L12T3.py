######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:03.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L12T3
import sys

import jsonpickle

#Luokat
class TIEDOT:
    Nimike = None
    Tekija = None
    ISBN = None
    Varauksia = None
    Niteita = None
    Lisakappaleita = None
    VarauksiaPerNide = None

#aliohjelmat

def tiedNimi(kehote):
    nimi = input("Anna {0} tiedoston nimi: ".format(kehote))
    return nimi

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto\n2) Lue JSON tiedosto\n3) Kirjoita CSV tiedosto\n4) Kirjoita JSON tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def lueCSVTiedosto(luettavanTiedostonNimi,lista):
    lista.clear
    try:
        lt=open(luettavanTiedostonNimi,"r",encoding="utf-8")
        lt.readline()
        while True:

            rivi=((lt.readline())[:-1]).split(";")
            if rivi==[""]:
                break
            olio = TIEDOT()
            olio.Nimike = rivi[0]
            olio.Tekija = rivi[1]
            olio.ISBN = rivi[2]
            olio.Varauksia = int(rivi[3])
            olio.Niteita = int(rivi[4])
            olio.Lisakappaleita = int(rivi[5])
            olio.VarauksiaPerNide = float(rivi[6])

            lista.append(olio)
        lt.close()
        print("Luettu {0} kirjan tiedot.\n".format(len(lista)))
    except Exception:
        print("Tiedoston {0} käsittelyssä virhe, lopetetaan.".format(luettavanTiedostonNimi))
        sys.exit(0)
    return lista

def lueJSONTiedosto(Nimi,lista):
    lista.clear
    try:
        tiedosto = open(Nimi,"r",encoding="utf-8")
        data = tiedosto.read()
        lista = jsonpickle.decode(data)
        tiedosto.close
        print("Luettu {0} kirjan tiedot.\n".format(len(lista)))
    except Exception:
        print("Tiedoston {0} käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    return lista

def kirjoitaCSV(nimi,lista):
    try:
        tiedosto = open(nimi,"w",encoding = "utf-8")
        tiedosto.write("Nimike;Tekijä;ISBN;Varauksia;Niteitä;Tilattuja lisäkappaleita;Varauksia / nide\n")
        for olio in lista:
            tiedosto.write(str(olio.Nimike)+";"+str(olio.Tekija)+";"+str(olio.ISBN)+";"+str(olio.Varauksia)+";"+str(olio.Niteita)+";"+str(olio.Lisakappaleita)+";"+str(olio.VarauksiaPerNide)+"\n")
        tiedosto.close()
        print("Tiedosto {0} kirjoitettu.\n".format(nimi))
    except Exception:
        print("Tiedoston {0} käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)
    return None
def kirjoitusJSON(nimi,lista):
    try:
        tiedosto = open(nimi,"w",encoding="utf-8")
        data = jsonpickle.encode(lista,indent=4)
        tiedosto.write(data)
        tiedosto.close()
        print("Tiedosto {0} kirjoitettu.\n".format(nimi))
    except Exception:
        print("Tiedoston {0} käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)
    return None

#paaohjelma

def paaohjelma():
    oliolista = []
    valinta = None
    nimi = None
    while True:
        valinta = valikko()
        if valinta == 1:
           nimi = tiedNimi("luettavan CSV")
           oliolista = lueCSVTiedosto(nimi,oliolista)
        elif valinta == 2:
            nimi = tiedNimi("luettavan JSON")
            oliolista = lueJSONTiedosto(nimi, oliolista)
        elif valinta == 3:
            nimi = tiedNimi("kirjoitettavan CSV")
            kirjoitaCSV(nimi, oliolista)
        elif valinta == 4:
            nimi = tiedNimi("kirjoitettavan JSON")
            kirjoitusJSON(nimi, oliolista)
        elif valinta == 0:
            print()
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta.")


paaohjelma()