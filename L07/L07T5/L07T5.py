######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:23.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#luokat ja listat
class AUTO:
    merkki = ""
    hinta = ""



#aliohjelmat
def kysyTalTied():
    talTiedNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedosto = open(talTiedNimi, "w", encoding="utf-8")
    tiedosto.close()
    return talTiedNimi
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot\n2) Tulosta autojen tiedot\n3) Tallenna autojen tiedot tiedostoon\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def annaAutonTied(autolista):
    auto = AUTO()
    auto.merkki = input("Anna auton merkki: ")
    auto.hinta = input("Anna auton hinta: ")
    autolista.append(auto)
    print()
    return autolista
def tulostaAutonTied(autolista):
    print("Listalta löytyy seuraavat autot ja hinnat:")
    for autot in autolista:
        rivi = "{0} {1}".format(autot.merkki, autot.hinta)
        print(rivi)
    print()
    return None
def kirjoitus(tiedosto,lista):
    print("Tapahtumat kirjoitettu tiedostoon '{0}'.\n".format(tiedosto))
    tiedosto = open(tiedosto, "w", encoding="utf-8")
    tiedosto.write("Auton merkki;Auton hinta\n")
    for i in lista:
        merkki=i.merkki
        hinta=i.hinta
        tiedosto.write("{0};{1}\n".format(merkki,hinta))
    tiedosto.close()
    return None
#paaohjelma
def paaohjelma():
    n=0
    autolista=[]
    talTidNimi=kysyTalTied()
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")

    while True:
        valinta=valikko()

        if valinta == 1:
            n += 1
            autolista = annaAutonTied(autolista)

        elif valinta == 2:
            tulostaAutonTied(autolista)

        elif valinta == 3:
            kirjoitus(talTidNimi,autolista)
        elif valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")

    print("Kiitos ohjelman käytöstä.")

    return None

paaohjelma()

#L07T5.py
#EOF