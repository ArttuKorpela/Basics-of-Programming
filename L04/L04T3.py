print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")
maara=int(input("Kuinka monta merkkijonoa kysytään: "))
minpituus=int(input("Mikä on merkkijonon minimipituus: "))
kiellettymerkki=input("Mitä merkkiä merkkijonossa ei saa olla: ")
pisin=""
merkkimaara=0
while merkkimaara<=maara:
    merkkijono=input("Anna merkkijono: ")
    merkkimaara+=1
    if merkkimaara==maara:
        print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")
        print(f"Annoit {merkkimaara} merkkijonoa.")
        print(f"Pisin merkkijono oli '{pisin}', jossa oli {len(pisin)} merkkiä.")
        break
    elif len(merkkijono)<minpituus:
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        print(f"Annoit {merkkimaara} merkkijonoa.")
        print(f"Pisin merkkijono oli '{pisin}', jossa oli {len(pisin)} merkkiä.")
        break
    elif len(pisin)<len(merkkijono):
        pisin=merkkijono
        if pisin.find(kiellettymerkki)>-1:
            print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
            print(f"Annoit {merkkimaara} merkkijonoa.")
            print(f"Pisin merkkijono oli '{pisin}', jossa oli {len(pisin)} merkkiä.")
            break
    elif merkkijono.find(kiellettymerkki)>-1:
        print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
        print(f"Annoit {merkkimaara} merkkijonoa.")
        print(f"Pisin merkkijono oli '{pisin}', jossa oli {len(pisin)} merkkiä.")
        break
    elif len(pisin)>len(merkkijono) or len(pisin)==len(merkkijono):
        continue
    else:
        print("Ohjelma päättyi tuntemattomaan syyhyn.")
        print(f"Annoit {merkkimaara} merkkijonoa.")
        print(f"Pisin merkkijono oli '{pisin}', jossa oli {len(pisin)} merkkiä.")
        break
print("Kiitos ohjelman käytöstä.")

