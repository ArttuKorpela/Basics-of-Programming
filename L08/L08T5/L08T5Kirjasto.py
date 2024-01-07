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
versio=1.0
#Luokat
class TUOTE:
    tunnus = None
    maara = None
    hinta = None



#aliohjelmat
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto\n"
          "2) Analysoi tiedot\n"
          "3) Tallenna tulokset\n"
          "0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def kysyTied(kehote,tiedostonNimi):
    print("Anna {0} tiedoston nimi, nykyinen on '{1}'.".format(kehote,tiedostonNimi))
    uusinimi =input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if uusinimi == "":
        return tiedostonNimi
    else:
        return uusinimi


def lueTiedosto(luettavanTiedostonNimi, lista):
    lt = open(luettavanTiedostonNimi, "r", encoding="utf-8")
    lista.clear()
    while True:
        rivi = ((lt.readline())[:-1])
        if rivi == "":
            break
        tiedot = rivi.split(";")
        tuote = TUOTE()
        tuote.tunnus = tiedot[0]
        tuote.maara = float(tiedot[1])
        tuote.hinta = float(tiedot[2])

        lista.append(tuote)
    print("Tiedosto '{0}' luettu, {1} riviä.\n".format(luettavanTiedostonNimi, len(lista)))
    lt.close()
    return lista



def analyysi(lista):
    arvo = 0
    hintalista = []
    for tuote in lista:
        arvo = tuote.maara*tuote.hinta
        hintalista.append(arvo)
    print("Tiedot analysoitu, varaston arvo on {0:.2f} EUR.\n".format(round(sum(hintalista),2)))
    return hintalista

def kirjoitus(tiedosto,lista):
    print("Tulokset tallennettu tiedostoon '{0}'.\n".format(tiedosto))
    tiedosto = open(tiedosto, "w", encoding="utf-8")
    for arvo in lista:
        tiedosto.write("{0:.2f}\n".format(arvo))
    tiedosto.close()
    return None

def lopetus():
    print("Lopetetaan.\n")
    print("Kiitos ohjelman käytöstä.")
    return None

#L08T5.py
#EOF