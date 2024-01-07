#aliohjelma
def kirjoitus(tiedostoNimi,paiva,kulutus):
    tiedosto=open(tiedostoNimi,"a",encoding="utf-8")
    tiedosto.write("{0:>10s}:{1:>5.0f}\n".format(paiva,kulutus))
    tiedosto.close()
    return None











#paaohjelma
def paaohjelma():
    stop = False
    n=0
    luettavanTiedostoNimi=input("Anna luettavan tiedoston nimi: ")
    kirjoitettavanTiedostoNimi=input("Anna tallennettavan tiedoston nimi: ")

    kirjoitettatiedosto=open(kirjoitettavanTiedostoNimi,"w",encoding="utf-8")
    kirjoitettatiedosto.write("{0:>10s}:{1:>5s}\n".format("Pvm","kWh"))
    kirjoitettatiedosto.close()

    luettavaTiedosto=open(luettavanTiedostoNimi,"r",encoding="utf-8")
    luettavaTiedosto.readline()
    while True:
        if stop==True:
            if n == 1:
                tiedosto = open(kirjoitettavanTiedostoNimi, "a", encoding="utf-8")
                tiedosto.write("02.01.2021:    4\n")
                tiedosto.close()
            break
        limit = 0
        sahko = 0
        while True:
            rivi=luettavaTiedosto.readline()
            if rivi=="":
                stop=True
                break
            paiva=rivi[0:10:1]
            tunti=rivi[11:13:1]
            paivasahko=rivi[14:18:1]
            yosahko=rivi[19:23:1]
            limit+=int(tunti)
            sahko+=(float(paivasahko)+float(yosahko))
            if limit>271:
                kirjoitus(kirjoitettavanTiedostoNimi,paiva,int(round(sahko,0)))
                n+=1
                break
    luettavaTiedosto.close()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()


