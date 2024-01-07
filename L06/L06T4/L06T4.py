#aliohjelmat

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet\n2) Analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTied(kehote,tiedostonNimi):
    print(f"{kehote} tiedoston nimi on '{tiedostonNimi}'.")
    luku1 =input("Anna uusi nimi, enter säilyttää nykyisen: ")
    return luku1

def PieninLuku(tiedostonNimi):
    tiedosto=open(tiedostonNimi,"r")
    luku=tiedosto.readline()
    pieninluku=int((luku)[:-1])
    while True:
        riviraw=tiedosto.readline()
        if riviraw=="":
            break
        n=(riviraw)[:-1]
        rivi=int(n)
        if rivi<pieninluku:
            pieninluku=rivi

    return pieninluku

def suurinLuku(tiedostonNimi):
    tiedosto=open(tiedostonNimi,"r")
    luku=tiedosto.readline()
    suurinluku=int((luku)[:-1])
    while True:
        riviraw=tiedosto.readline()
        if riviraw=="":
            break
        n=(riviraw)[:-1]
        rivi=int(n)
        if rivi>suurinluku:
            suurinluku=rivi

    return suurinluku

def kirjoitus(tiedostonNimi,pieninLuku,suurinLuku):
    tiedosto=open(tiedostonNimi,"w",encoding="utf-8")
    tiedosto.write(f"Analyysin tulokset ovat seuraavat:\n"
                   f"Datan pienin arvo on {pieninLuku}.\n"
                   f"Datan suurin arvo on {suurinLuku}.")
    return None

#paaohjelma

def paaohjelma():
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

            luettavatiedosto=b
            kirjoitettavatiedosto=c
            print()
        elif valinta == 2:
            pieninluku=PieninLuku(luettavatiedosto)
            suurinluku=suurinLuku(luettavatiedosto)
            print("Suoritetaan analyysi\n")
        elif valinta == 3:
            kirjoitus(kirjoitettavatiedosto,pieninluku,suurinluku)
            print("Kirjoitetaan tulokset tiedostoon\n")
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