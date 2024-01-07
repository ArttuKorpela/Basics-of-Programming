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
#paaohjelma

def paaohjelma():
    tiedNimi=input("Anna tiedoston nimi: ")
    tiedosto=open(tiedNimi,"r",encoding="utf-8")
    rivi=tiedosto.readline()

    print("Kalastuskilpailun tulokset ovat seuraavat:")
    while True:
        rivi=(tiedosto.readline()[:-1]).split(";")
        if rivi[0]=="":
            break

        print("Joukkue '{0}' sai kalan {1}, joka oli {2} cm.".format(rivi[0],rivi[1],rivi[2]))

    print("Kiitos ohjelman käytöstä.")

    return None
#L07T3
#EOF
paaohjelma()
