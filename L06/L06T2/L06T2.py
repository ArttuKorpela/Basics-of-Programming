#paaohjelma

def paaohjelma():
    kirjaimet=0
    merkit=0
    nimet=0

    tiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(tiedostoNimi,"r",encoding="utf-8")
    while True:
        rivi = tiedosto.readline()
        if rivi[:-1]=="":
            tiedosto.close()
            break
        elif rivi.find("-")==-1:
            merkit+=len(rivi)
            nimet+=1
            kirjaimet+=len(rivi)-1
        else:
            merkit+=len(rivi)
            nimet+=1
            kirjaimet+=len(rivi)
    print(f"Tiedostossa oli {nimet} nimeä ja {merkit} merkkiä.")
    keskiarvo=int(round(kirjaimet/nimet,0))
    print(f"Keskimäärin nimen pituus oli {keskiarvo} merkkiä.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()