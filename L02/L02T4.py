sana = input("Anna sana: ")
print(f"Antamasi sanan kolme ensimmäistä kirjainta ovat {sana[0:3]}")
print(f"Sanan neljä viimeistä kirjainta ovat {sana[-4::]}")
print(f"Kirjaimet 3, 4, 5 ja 6 ovat {sana[2:6]}\n")

print(f"Sanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta: {sana[::3]}\n")

print(f"Antamasi sana '{sana}' on takaperin '{sana[::-1]}'.\n")

a = input("Anna aloituspaikka: ")
b = input("Anna lopetuspaikka: ")
c = input("Anna siirtymä: ")
print(f"Antamillasi asetuksilla sana {sana} tulostuu näin: {sana[int(a):int(b):int(c)]}\n")

print(f"Antamasi sanan pituus oli {len(sana)} merkkiä.")
print("Kiitos ohjelman käytöstä.")
