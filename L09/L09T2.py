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

#aliohjelmat

def indeksi():
    lista = [11,22,33,44,55]
    indeksi = int(input("Anna indeksi 0-4: "))
    try:
        print("Listan arvo on {0} indeksillä {1}.\n".format(lista[indeksi],indeksi))
    except IndexError:
        print("Tuli IndexError, indeksi {0}.\n".format(indeksi))
    return None


def nollajako():
    jakaja = int(input("Anna jakaja: "))
    try:
        print("4/{1} on {0:.2f}.\n".format(round(4/jakaja,2),jakaja))
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja {0}.\n".format(jakaja))
    return None
def kirjoitusVirhe():
    numero = input("Anna numero: ")
    try:
        print(numero*numero)
    except TypeError:
        print("Tuli TypeError, {0}*{0} merkkijonoilla ei onnistunut.\n".format(numero))
    return None

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError\n"
          "2) Testaa IndexError\n"
          "3) Testaa ZeroDivisionError\n"
          "4) Testaa TypeError\n"
          "0) Lopeta")
    while True:
        try:
            valinta = int(input("Valintasi: "))
            break
        except ValueError:
            print("Anna Valinta kokonaislukuna.")
    return valinta

def paaohjelma():


    while True:
        valinta = valikko()

        if valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.\n")


        elif valinta == 2:
            indeksi()

        elif valinta == 3:
            nollajako()

        elif valinta == 4:
            kirjoitusVirhe()

        elif valinta == 0:
            print("Lopetetaan\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")


    print("Kiitos ohjelman käytöstä.")

    return None

paaohjelma()

#EOF