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

import L08T2Kirjasto

# aliohjelmat

def valinta():
    print(
          "Minkä muunnoksen haluat tehdä?")
    print("1) Anna muunnettava tilavuus\n"
          "2) Muunna litra gallon'ksi\n"
          "3) Muunna litra pint'ksi\n"
          "4) Muunna litra cup'ksi\n"
          "5) Muunna litra fluid ounce'ksi\n"
          "6) Muunna gallon litroiksi\n"
          "7) Muunna pint litroiksi\n"
          "8) Muunna cup litroiksi\n"
          "9) Muunna fluid ounce litroiksi\n"
          "0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta
def tilavuus():
    n=float(input("Anna muunnettava tilavuus desimaalilukuna: "))
    print()
    return n

def litraGal(arvo):
    print("Litrat muutettuina gallon'ksi: {0}\n".format(round(L08T2Kirjasto.litraGallonaksi(arvo),2)))
    return None

def litraPint(arvo):
    print("Litrat muutettuina pint'ksi: {0}\n".format(round(L08T2Kirjasto.litraPintiksi(arvo),2)))
    return None

def litraCup(arvo):
    print("Litrat muutettuina cup'ksi: {0}\n".format(round(L08T2Kirjasto.litraCup(arvo),2)))
    return None

def litraFluid(arvo):
    print("Litrat muutettuina fluid ounce'ksi: {0}\n".format(round(L08T2Kirjasto.litraOunceksi(arvo),2)))
    return None

def gallonLitra(arvo):
    print("Gallon't muutettuina litroiksi: {0}\n".format(round(L08T2Kirjasto.GallonaLitraksi(arvo),2)))
    return None

def pintLitra(arvo):
    print("Pint't muutettuina litroiksi: {0}\n".format(round(L08T2Kirjasto.PintLitraksi(arvo),2)))
    return None

def cupLitra(arvo):
    print("Cup't muutettuina litroiksi: {0}\n".format(round(L08T2Kirjasto.CupLitraksi(arvo),2)))
    return None

def fluidLitra(arvo):
    print("Fluid ounce't muutettuina litroiksi: {0}\n".format(round(L08T2Kirjasto.OunceLitraksi(arvo),2)))
    return None
def lopetus():
    print("Lopetetaan\n")
    print("Kiitos ohjelman käytöstä.")
    return None


# paaohjelma

def paaohjelma():
    arvo=0
    print("Käytetään kirjaston versiota 1.0")
    while True:
        n = valinta()

        if n == 1:
            arvo=tilavuus()
        elif n == 2:
            litraGal(arvo)
        elif n == 3:
            litraPint(arvo)
        elif n == 4:
            litraCup(arvo)
        elif n == 5:
            litraFluid(arvo)
        elif n == 6:
            gallonLitra(arvo)
        elif n == 7:
            pintLitra(arvo)
        elif n==8:
            cupLitra(arvo)
        elif n==9:
            fluidLitra(arvo)
        elif arvo==0:
            print("Anna jokin tilavuus.")
        elif n == 0:
            lopetus()
            break


paaohjelma()

# L08T2.py
# EOF
