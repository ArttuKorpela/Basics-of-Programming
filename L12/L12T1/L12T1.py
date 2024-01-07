######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:03.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L12T1

sanakirja = {"10":"A",
             "11":"B",
             "12":"C",
             "13":"D",
             "14":"E",
             "15":"F",
             "16":"H",
             "17":"J",
             "18":"K",
             "19":"L",
             "20":"M",
             "21":"N",
             "22":"P",
             "23":"R",
             "24":"S",
             "25":"T",
             "26":"U",
             "27":"V",
             "28":"W",
             "29":"X",
             "30":"Y"}

sotu = input("Anna henkilötunnus: ")
numsotu = int(sotu[:6]+sotu[7:10])
jaannos = numsotu % 31
tarkistus = sotu[-1]
if jaannos<10:
    lopjaannos = str(jaannos)
else:
    lopjaannos = sanakirja[str(jaannos)]

if tarkistus == lopjaannos:
    print("Henkilötunnus hyväksytty.")
else:
    print("Henkilötunnusta ei hyväksytä.")
print("Kiitos ohjelman käytöstä.")