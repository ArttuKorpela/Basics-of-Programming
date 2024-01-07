import math


class AUTO:
    km = None
    kulutus = None
    Polttoaine = None
    ika = None
    vakuutus = None
    bonus = None
    vero = None


#aliohjelmat

def kysytiedot():
    tiedot = AUTO()
    tiedot.km = int(input("Anna vuotuiset kilometrit: "))
    tiedot.kulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    tiedot.polttoaine = float(input("Anna polttoaineen hinta (€/l): "))
    tiedot.ika = int(input("Anna auton ikä vuosissa: "))
    tiedot.vakuutus = int(input("Anna vakuutusten määrä (euroissa): "))
    tiedot.bonus = int(input("Anna bonusprosentti kokonaislukuna: "))
    tiedot.vero = int(input("Anna verojen määrä: "))
    return tiedot

def laskut(t,lista):
    lista = [0,0,0,0,0]

    for i in range(5):
        summa = (t.km/100) * t.kulutus * t.polttoaine + (t.vakuutus - (t.bonus*(t.vakuutus)/100)) + t.vero + 200 * math.sqrt(t.ika+i)
        lista[i] = int(round(summa,0))
    return lista

def tulostus(lista):
    for i in range(5):
        vuosi = i+1
        print("{0}. vuosi: {1}".format(vuosi,lista[i]))
    print("Viiden vuoden aikana autoon käytettiin rahaa {0} euroa.".format(sum(lista)))
    print("Kiitos ohjelman käytöstä.")
    return None

def paaohjelma():
    lista = []
    tiedot = kysytiedot()
    lista = laskut(tiedot,lista)
    tulostus(lista)
    return None

paaohjelma()
