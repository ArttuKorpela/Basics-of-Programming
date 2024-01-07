#aliohjelmat
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono\n2) Määritä askel\n3) Tulosta merkkijono\n0) Lopeta")
    valinta=int(input("Anna valintasi: "))
    return valinta
def kysyMerkkijono():
    merkkijono=input("Anna merkkijono: ")
    print()
    return merkkijono
def kysyAskel():
    askel=int(input("Anna tulostuksessa käytettävä askel: "))
    print()
    return askel
def tulostaMerkkijono(a,b):
    c=0
    if b==0:
        for kirjain in range(len(a)+1):
            print(a[:len(a)-c:])
            c+=1
    else:
        print(a[::b])
    print()
    return None
def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    while True:
        Valinta=valikko()
        if Valinta==1:
            merkkijono=kysyMerkkijono()
        elif Valinta==2:
            askel=kysyAskel()
        elif Valinta==3:
            tulostaMerkkijono(merkkijono,askel)
        elif Valinta==0:
            print("Lopetetaan.")
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()

