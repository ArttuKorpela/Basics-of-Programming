######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:22.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

#aliohjelmat

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet\n2) Lue tiedosto\n3) Analysoi\n4) Kirjoita tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTied(kehote,tiedostonNimi):
    print(f"{kehote} tiedoston nimi on '{tiedostonNimi}'.")
    luku1 =input("Anna uusi nimi, enter säilyttää nykyisen: ")
    return luku1

def lueTiedosto(luettavanTiedostonNimi):
    lista=[]
    lt=open(luettavanTiedostonNimi,"r",encoding="utf-8")
    while True:
        rivi=((lt.readline())[:-1])
        if rivi=="":
            break
        lista.append(int(rivi))
    lt.close()
    return lista

def analyysi(olio,lista):
    olio.pieninarvo=min(lista)
    olio.suurinarvo=max(lista)
    olio.summa=sum(lista)
    olio.keskiarvo=round(sum(lista)/len(lista),0)
    return olio


def kirjoitus(tiedostonNimi,olio):
    tiedosto=open(tiedostonNimi,"w",encoding="utf-8")
    tiedosto.write("Analyysin tulokset ovat seuraavat:\n"
                   "Datan pienin arvo on {0}.\n"
                   "Datan suurin arvo on {1}.\n"
                   "Datan summa on {2}.\n"
                   "Datan keskiarvo on {3:.1f}.".format(olio.pieninarvo,olio.suurinarvo,olio.summa,olio.keskiarvo))
    tiedosto.close()
    return None

#paaohjelma

def paaohjelma():
    class TULOS:
        pieninarvo = ""
        suurinarvo = ""
        summa = ""
        keskiarvo = ""

    tulos=TULOS()

    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    valinta = 0
    b = ""
    c= ""
    while True:
        valinta = valikko()
        if valinta == 1:
            print("Anna tiedostonimet")
            a = "Luettavan"
            Lukutiedosto = kysyTied(a, b)
            if Lukutiedosto != "":
                b = Lukutiedosto

            a = "Kirjoitettavan"
            KirjoitettavaTiedosto = kysyTied(a, c)
            if KirjoitettavaTiedosto != "":
                c = KirjoitettavaTiedosto

            luettavatiedosto = b
            kirjoitettavatiedosto = c
            print()
        elif valinta == 2:
            lista = lueTiedosto(luettavatiedosto)
            print("Tiedosto '{0}' luettu.\n".format(luettavatiedosto))
        elif valinta == 3:
            tulos = analyysi(tulos,lista)
            print("Analyysi suoritettu.\n")
        elif valinta == 4:
            kirjoitus(kirjoitettavatiedosto,tulos)
            print("Tulokset kirjoitettu tiedostoon.\n")
        elif valinta == 0:

            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
    print()
    print("Kiitos ohjelman käytöstä.")

    return None

paaohjelma()

#L07T4.py
#EOF