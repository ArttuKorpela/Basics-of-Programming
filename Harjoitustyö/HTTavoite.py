######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:04.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla: https://www.pythoncentral.io, Numpy array:n käyttö (esim. summat ja pyöristykset)
# https://lutpub.lut.fi/handle/10024/162088
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# HTTavoite.py

import  HTTavoiteKirjasto

#aliohjelmat

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto\n"
          "2) Analysoi\n"
          "3) Kirjoita tiedosto\n"
          "4) Analysoi viikonpäivittäiset keskiarvot\n"
          "5) Lue sähkönkulutusdata\n"
          "6) Analysoi viikoittaiset tuntilaskut\n"
          "0) Lopeta")
    try:
        valinta = int(input("Anna valintasi: "))
        return valinta
    except Exception:
        print("Tuntematon valinta, yritä uudestaan")



#paaohjelma

def paaohjelma():

    tilasto_olio = None


    lueTiedNimi = ""

    kirTiedNimi1 = ""

    kirTiedNimi2 = ""

    kulutusTiedNimi = ""

    laskuNimi = ""

    olioLista = []

    keskiarvitulokset = []

    viikonpaivaLista = []

    tulostusLista1 = []

    tulostusVknpvt = []

    yhdistetyt_tulokset = []

    sanakirja = {}

    while True:
        valinta = valikko()

        if valinta == 1:
            lueTiedNimi = HTTavoiteKirjasto.kysyNimi("luettavan")

            olioLista = HTTavoiteKirjasto.lueTiedosto(lueTiedNimi,olioLista)

        elif valinta == 2:
            if olioLista == []:
                HTTavoiteKirjasto.eiTietoja()
            else:
                tilasto_olio = HTTavoiteKirjasto.analysoiTilastot(olioLista)
                keskiarvitulokset = HTTavoiteKirjasto.keskiarvot(olioLista,keskiarvitulokset)


        elif valinta == 3:
            if tilasto_olio == None or keskiarvitulokset == []:
                HTTavoiteKirjasto.eiKirjTietoja()
            else:
                kirTiedNimi1 = HTTavoiteKirjasto.kysyNimi("kirjoitettavan")
                tulostusLista1 = HTTavoiteKirjasto.muotoilu(tilasto_olio, keskiarvitulokset,tulostusLista1)
                HTTavoiteKirjasto.kirjoitus(kirTiedNimi1,tulostusLista1)

        elif valinta == 4:
            if olioLista == []:
                HTTavoiteKirjasto.eiTietoja()
            else:
                kirTiedNimi2 = HTTavoiteKirjasto.kysyNimi("kirjoitettavan")
                viikonpaivaLista = HTTavoiteKirjasto.analysoiviikonpaivat(olioLista,viikonpaivaLista)
                tulostusVknpvt = HTTavoiteKirjasto.muotoiluVknpvt(tulostusVknpvt,viikonpaivaLista)
                HTTavoiteKirjasto.kirjoitus(kirTiedNimi2,tulostusVknpvt)

        elif valinta == 5:
            kulutusTiedNimi = HTTavoiteKirjasto.kysyNimi("luettavan")
            sanakirja = HTTavoiteKirjasto.luetiedosto(kulutusTiedNimi,sanakirja)
            HTTavoiteKirjasto.tietoyhdistys(olioLista, sanakirja)
        elif valinta == 6:
            if olioLista == []:
                HTTavoiteKirjasto.eiTietoja()
            else:
                yhdistetyt_tulokset = HTTavoiteKirjasto.matriisinmuodostus(olioLista,yhdistetyt_tulokset)
                laskuNimi = HTTavoiteKirjasto.kysyNimi("kirjoitettavan")
                HTTavoiteKirjasto.kirjoitus(laskuNimi,yhdistetyt_tulokset)

        elif valinta == 0:
            HTTavoiteKirjasto.lopetus()
            olioLista.clear()
            keskiarvitulokset.clear()
            viikonpaivaLista.clear()
            tulostusLista1.clear()
            tulostusVknpvt.clear()
            yhdistetyt_tulokset.clear()
            sanakirja.clear()
            tilasto_olio = None
            break
        else:
            HTTavoiteKirjasto.tuntematon()

    return None


paaohjelma()

#EOF