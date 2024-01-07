######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:04.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#https://www.pythoncentral.io
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
import datetime
import sys
import numpy
#import HarjoitustyoKirjasto





#aliohjelmat
def luetiedosto(tiedoston_nimi,oliolista):
    sanakirja = {}

    lista = []

    kokonaishinta = []

    edellinenpaiva = None

    kulutus = None

    paivamaara = None
    try:
        kulutusData = open(tiedoston_nimi,"r",encoding="utf-8")
    except Exception:
        print("Tiedostonkäsittelyssä virhe, suljetaan.")
        sys.exit(0)

    kulutusData.readline()

    while True:
        rivi = (kulutusData.readline())[:-1]
        if rivi == "":
            kulutusData.close()
            lista.clear()
            break
        lista = rivi.split(";")

        paivamaara = datetime.datetime.strptime((lista[0]),"%d.%m.%Y %H:%M")
        if paivamaara == edellinenpaiva:
            sanakirja[paivamaara] = kulutus + (float(lista[1])+float(lista[2]))
            edellinenpaiva = paivamaara
        else:
            kulutus = float(lista[1])+float(lista[2])
            edellinenpaiva = paivamaara

            sanakirja[paivamaara] = kulutus

    for olio in oliolista:
        if olio.aika == datetime.datetime(2021, 3, 28, 3, 0):
            olio.kulutus = 0
        else:
            olio.kulutus = (sanakirja[olio.aika])
            kokonaishinta.append(olio.kulutus*olio.hinta)

    print("Hinta- ja kulutustiedot yhdistetty. Lasku on yhteensä {0:.2f} euroa.".format(round(sum(kokonaishinta)/100,2)))
    sanakirja.clear()
    kokonaishinta.clear()
    return None

def matriisinTulostus(oliolista,tulostuslista):
    viikot = 54
    tunnit = 24
    tulostuslista.clear()
    viimeisteltyRivi = ""


    matriisiB = numpy.zeros((viikot, tunnit), float)
    for olio in oliolista:
        viikko = int((olio.aika).strftime("%W"))


        tunti = int((olio.aika).strftime("%H"))


        matriisiB[viikko][tunti] += (olio.hinta)*(olio.kulutus)

    yht_viikot = (matriisiB.sum(1))
    m = numpy.insert(matriisiB,24,yht_viikot,axis=1)
    yht_tunnit = (m.sum(0))
    n = numpy.append(m,[yht_tunnit],axis=0)
    numpy.set_printoptions(precision=2, suppress=True)
    lopullinen = numpy.round(n,
             decimals=1)
    rivien_maara = numpy.shape(lopullinen)[0]
    sarakkeiden_maara = numpy.shape(lopullinen)[1]

    tulostuslista.append("Viikko\Tunti;0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;YHT\n")
    for rivi in range(rivien_maara):
        if rivi <= 53:
            for sarake in range(sarakkeiden_maara):
                viimeisteltyRivi += str(lopullinen[rivi][sarake])+";"
            tulostuslista.append(("Vko {0};{1}".format(rivi,viimeisteltyRivi))[:-1]+"\n")
            viimeisteltyRivi = ""
        else:
            for sarake in range(sarakkeiden_maara):
                viimeisteltyRivi += str(lopullinen[rivi][sarake])+";"
            tulostuslista.append(("YHT;{0}".format(viimeisteltyRivi))[:-1]+"\n")

    print("Tuntikohtaiset hinnat analysoitu")
    return tulostuslista





#lista = []
#lista = HarjoitustyoKirjasto.lueTiedosto("porssisahko2021.txt",lista)
#luetiedosto("kerrostalo2021.txt",lista)

#matriisinTulostus(lista)
