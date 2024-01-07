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
import datetime
#aliohjelmat
def valinta():
    print(
          "Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit\n"
          "2) Laske ikä päivinä\n"
          "3) Tulosta viikonpäivät\n"
          "4) Tulosta kuukaudet\n"
          "0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def tunnistus():
    merkkijono=input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    paivamaara=datetime.datetime.strptime(merkkijono,"%d.%m.%Y %H:%M")
    kuukausi=int(paivamaara.strftime("%m"))
    paiva = int(paivamaara.strftime("%d"))
    print(paivamaara.strftime("Annoit vuoden %Y\n"
                        f"Annoit kuukauden {kuukausi}\n"
                        f"Annoit päivän {paiva}\n"
                        "Annoit tunnin %H\n"
                        "Annoit minuutin %M\n"))
    return None

def syntymapaiva():
    paiva=datetime.datetime(2000,1,1)
    merkkijono = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ")
    paivamaara = datetime.datetime.strptime(merkkijono, "%d.%m.%Y")
    aika=paiva-paivamaara
    print("1.1.2000 henkilö oli {0} päivää vanha.\n".format(aika.days))
    return None

def paivat():
    ma=datetime.datetime(2022,10,31)
    n=0
    for i in range(7):
        paiva=ma + datetime.timedelta(days=n)
        print(paiva.strftime("%A"))
        n+=1
    print()
    return None

def kuukaudet():
    tam=datetime.datetime(2022,1,1)
    n=0
    for i in range(12):
        kuukausi=tam + datetime.timedelta(days=+31*n)
        print(kuukausi.strftime("%b"))
        n+=1
    print()
    return None

def lopetus():
    print("Lopetetaan.\n")
    print("Kiitos ohjelman käytöstä.")
    return None


# paaohjelma

def paaohjelma():
    arvo=0
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        n = valinta()

        if n == 1:
            tunnistus()
        elif n == 2:
            syntymapaiva()
        elif n == 3:
            paivat()
        elif n == 4:
            kuukaudet()
        elif n == 0:
            lopetus()
            break
    return None

paaohjelma()






#L08T3
#EOF