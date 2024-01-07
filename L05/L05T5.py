#aliohjelmat
PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'

def tulostaohjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.")
    print()
    return None
def tarkistaMerkkijono(merkkijono):
    vaatimukset=0
    pituus=len(merkkijono)
    if merkkijono.find(EROTIN)>-1:
        vaatimukset=3
    elif len(merkkijono)<PITUUS_MIN:
        vaatimukset=1
    elif len(merkkijono)>PITUUS_MAX:
        vaatimukset=2
    return vaatimukset
def tulostaHyvaksytyt(merkkijonot):
    if merkkijonot=="":
        print("Et antanut yhtään hyväksyttävää merkkijonoa.")
    else:
        print("Annoit seuraavat hyväksytyt merkkijonot:")
        tuloste=merkkijonot.replace(";","\n")
        print(tuloste)
    return None
def kysyMerkkijono(sana):
    merrkkijono=input(f"Anna {sana}merkkijono 5-15 merkkiä (enter lopettaa): ")
    return merrkkijono
#paaohjelma
def paaohjelma():
    tulostaohjeet()
    kerrat=0
    kysymyssana=""
    Merkkijono=""
    uusin_merkkijono=""
    while True:
        uusin_merkkijono = kysyMerkkijono(kysymyssana)
        if uusin_merkkijono=="" and kerrat==0:
            print("Et antanut yhtään hyväksyttävää merkkijonoa.")
            break
        elif uusin_merkkijono=="":
            Lopullinen=Merkkijono[:len(uusin_merkkijono)-1:]
            print()
            tulostaHyvaksytyt(Lopullinen)
            break
        elif tarkistaMerkkijono(uusin_merkkijono)==1:
            kysymyssana="uusi "
            print(f"Liian lyhyt, {len(uusin_merkkijono)} merkkiä.")
        elif tarkistaMerkkijono(uusin_merkkijono)==2:
            kysymyssana="uusi "
            print(f"Liian pitkä, {len(uusin_merkkijono)} merkkiä.")
        elif tarkistaMerkkijono(uusin_merkkijono)==3:
            kysymyssana = "uusi "
            print(f"Merkkijonossa on kielletty merkki '{EROTIN}'.")
        elif tarkistaMerkkijono(uusin_merkkijono)==0:
            Merkkijono+=uusin_merkkijono+";"
            kerrat+=1
            kysymyssana="seuraava "
    print("Kiitos ohjelman käytöstä.")



paaohjelma()



