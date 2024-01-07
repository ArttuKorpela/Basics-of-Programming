print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:")
print("1) Tulosta merkkijono etuperin\n2) Tulosta merkkijono takaperin\n3) Tulosta merkkijonon pituus\n0) Lopeta")
valinta=input("Anna valintasi: ")
if valinta == "0":
    print("Lopetetaan")
else:
    merkkijono = input("Anna merkkijono: ")
    if valinta=="1":
        print(f"Merkkijono on etuperin '{merkkijono}'.")
    elif valinta=="2":
        print(f"Merkkijono on takaperin '{merkkijono[::-1]}'.")
    elif valinta == "3":
        print(f"Merkkijonon pituus on {len(merkkijono)}.")
    else:
        print("Tuntematon valinta")
print("Kiitos ohjelman käytöstä.")
