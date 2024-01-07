
#aliohjelmat
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot\n2) Laske\n3) Tulosta tulokset\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta
def kysyLuku(kehote):
    luku1 = int(input(kehote))
    return luku1
def summa(x,y):
    summa = int(x + y)
    return summa
def erotus(x,y):
    erotus=int(x-y)
    return erotus
def tulostaTulokset(summa,erotus,luku1,luku2):
    print(f"Tulosta tulokset\nLuvut ovat {luku1} ja {luku2}.\nLukujen summa on {summa} ja erotus on {erotus}.")
    return None

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    valinta=0
    n=0
    while True:
        valinta = valikko()
        if valinta == 1:
            print("Syötä tiedot")
            luku1 = kysyLuku("Anna kokonaisluku 1: ")
            luku2 = kysyLuku("Anna kokonaisluku 2: ")
            n += 1
            print()
        elif valinta == 2 and n > 0:
            summat = summa(luku1, luku2)
            erotukset = erotus(luku1, luku2)
            print("Laske")
            print()
        elif valinta == 3:
            tulostaTulokset(summat, erotukset, luku1, luku2)
            print()
        elif valinta == 0:
            print("Lopetetaan.")
            break
            print()
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
    print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()



