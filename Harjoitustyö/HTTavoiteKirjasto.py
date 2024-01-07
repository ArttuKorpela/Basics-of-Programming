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
# HTTavoiteKirjasto.py

import datetime
import sys
import numpy

class SAHKOAlKIO:
        aika = None
        hinta = None
        kulutus = None

class TILASTOTULOS:
    keskiarvo = None
    pieninarvo = None
    suurinarvo = None
    suurinarvoaika = None
    pieninarvoaika = None
    maara = None

class KESKIARVOT:
    paivamaara = None
    keskiarvo = None


#aliohjelmat

def kysyNimi(kehotus):
    tiednimi = input("Anna {0} tiedoston nimi: ".format(kehotus))
    return tiednimi

def lueTiedosto(nimi,lista):

    try:
        tiedot = []
        lista.clear()

        lt = open(nimi, "r", encoding="utf-8")
        lt.readline()
        while True:
            rivi = ((lt.readline())[:-1])
            if rivi == "":
                break
            tiedot = rivi.split(";")

            pm=tiedot[0]
            tuote = SAHKOAlKIO()
            paiva_ja_aika = datetime.datetime.strptime(pm[1:-1],"%Y-%m-%d %H:%M:%S")
            tuote.aika = paiva_ja_aika
            tuote.hinta = float(tiedot[1])
            lista.append(tuote)
        print("Tiedosto '{0}' luettu.\n".format(nimi))

        tiedot.clear()
        lt.close()
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)

    return lista



def analysoiTilastot(lista):
    hintalista = []
    hintalista.clear()

    tilastotulos = TILASTOTULOS()

    for i in lista:
        hintalista.append(float(i.hinta))


    tilastotulos.keskiarvo = sum(hintalista)/len(hintalista)
    tilastotulos.pieninarvo = min(hintalista)
    tilastotulos.suurinarvo = max(hintalista)
    tilastotulos.maara = len(hintalista)
    tilastotulos.pieninarvoaika=lista[hintalista.index(min(hintalista))].aika
    tilastotulos.suurinarvoaika=lista[hintalista.index(max(hintalista))].aika

    print("Tilastotietojen analyysi suoritettu {0} alkiolle.".format(tilastotulos.maara))

    return tilastotulos










def keskiarvot(oliolista, tuloslista):
    n=0
    vanhapaiva = (oliolista[0].aika).date()
    hintalista = []
    tuloslista.clear()

    for i in oliolista:
        n+=1
        keskiarvoOlio = KESKIARVOT()
        paiva = (i.aika).date()



        if vanhapaiva == paiva:
                hintalista.append(float(i.hinta))

                if n == (len(oliolista)):
                    keskiarvoOlio.keskiarvo = (sum(hintalista) / len(hintalista))
                    hintalista.clear()
                    keskiarvoOlio.paivamaara = vanhapaiva
                    tuloslista.append(keskiarvoOlio)

        elif vanhapaiva != paiva:
            keskiarvoOlio.keskiarvo = (sum(hintalista)/len(hintalista))
            hintalista.clear()
            keskiarvoOlio.paivamaara = vanhapaiva
            vanhapaiva=paiva
            tuloslista.append(keskiarvoOlio)
            hintalista.append(float(i.hinta))



    print("Päivittäiset keskiarvot laskettu {0} päivälle.\n".format(len(tuloslista)))
    hintalista.clear()
    return tuloslista

def muotoilu(olio,oliolista,lista):

    lista.clear()

    lista.append("Analyysin tulokset {0} tunnilta ovat seuraavat:\n".format(olio.maara))
    lista.append("Sähkön keskihinta oli {0} snt/kWh.\n".format(round(olio.keskiarvo,1)))
    lista.append("Halvimmillaan sähkö oli {0} snt/kWh, {1}.\n".format(olio.pieninarvo, (olio.pieninarvoaika).strftime("%d.%m.%Y %H:%M")))
    lista.append("Kalleimmillaan sähkö oli {0} snt/kWh, {1}.\n".format(olio.suurinarvo, (olio.suurinarvoaika).strftime("%d.%m.%Y %H:%M")))
    lista.append("\n")
    lista.append("Päivittäiset keskiarvot (Pvm;snt/kWh):\n")
    for i in oliolista:
        lista.append("{1};{0}\n".format(round(i.keskiarvo,1), (i.paivamaara).strftime("%d.%m.%Y")))

    return lista






def kirjoitus(tiedoston_nimi, lista):
    try:
        tiedosto = open(tiedoston_nimi,"w",encoding="utf-8")
        for alkio in lista:
            tiedosto.write(alkio)
        tiedosto.close()
        print("Tiedosto '{0}' kirjoitettu.\n".format(tiedoston_nimi))
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(tiedoston_nimi))
        sys.exit(0)

    return None

def analysoiviikonpaivat(oliolista, lista):
    lista = []
    maarat = [0,0,0,0,0,0,0]
    for olio in oliolista:
        paiva = int((olio.aika).strftime("%w"))    
        summat[paiva] += olio.hinta       
        maarat[paiva] += 1
    for i in range(7):
            if maarat[i] == 0:
                    lista.append(0.0)
            lista.append(summat[i]/maarat[i])
    return lista


def muotoiluVknpvt(tulostelista, arvolista):
    tulostelista.clear()
    tulostelista.append("Viikonpäivä;Keskimääräinen hinta snt/kWh\n")
    tulostelista.append("Maanantai;{0:.2}\n".format(float(round(arvolista[1],2))))
    tulostelista.append("Tiistai;{0:.2}\n".format(float(round(arvolista[2], 2))))
    tulostelista.append("Keskiviikko;{0:.2}\n".format(float(round(arvolista[3], 2))))
    tulostelista.append("Torstai;{0:.2}\n".format(float(round(arvolista[4], 2))))
    tulostelista.append("Perjantai;{0:.2}\n".format(float(round(arvolista[5], 2))))
    tulostelista.append("Lauantai;{0:.2}\n".format(float(round(arvolista[6], 2))))
    tulostelista.append("Sunnuntai;{0:.2}\n".format(float(round(arvolista[0], 2))))
    return tulostelista

#aliohjelmat
def luetiedosto(tiedoston_nimi, sanakirja):
    try:
        sanakirja = {}

        lista = []

        edellinenpaiva = None

        kulutus = None

        paivamaara = None

        kulutusData = open(tiedoston_nimi,"r",encoding="utf-8")

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
        print("Tiedosto '{0}' luettu.".format(tiedoston_nimi))
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(tiedoston_nimi))
        sys.exit(0)
    return sanakirja


def tietoyhdistys(oliolista,sanakirja):

    kokonaishinta = []

    for olio in oliolista:
        if olio.aika == datetime.datetime(2021, 3, 28, 3, 0):
            olio.kulutus = 0
        else:
            olio.kulutus = (sanakirja[olio.aika])
            kokonaishinta.append(olio.kulutus*olio.hinta)

    print("Hinta- ja kulutustiedot yhdistetty. Lasku on yhteensä {0:.2f} euroa.\n".format(round(sum(kokonaishinta)/100,2)))
    sanakirja.clear()
    kokonaishinta.clear()
    return None

def matriisinmuodostus(oliolista,tulostuslista):

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

    print("Tuntikohtaiset hinnat analysoitu.")
    return tulostuslista

def tuntematon():
    print("Tuntematon valinta, yritä uudestaan.\n")
    return None

def eiTietoja():
    print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
    return None

def eiKirjTietoja():
    print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.\n")
    return None

def lopetus():
    print("Lopetetaan.\n"
          "\n"
          "Kiitos ohjelman käytöstä.")
    return None

#EOF
