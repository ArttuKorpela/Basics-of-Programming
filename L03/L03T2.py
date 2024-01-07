print("Selvitetään sanojen aakkosjärjestys.")
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

if sana1 == sana2:
    print(f"Sanat ovat samoja, '{sana1}'.")
elif sana1 < sana2:
    print(f"'{sana1}' on aakkosissa aiemmin kuin '{sana2}'.")
else:
    print(f"'{sana2}' on aakkosissa aiemmin kuin '{sana1}'.")
print()
print("Selvitetään merkin sisältyminen merkkijonoon.")
merkkijono = input("Anna merkkijono: ")
merkki = input("Anna etsittävä merkki: ")
arvo=merkkijono.find(merkki)
if arvo>=0:
    print(f"Merkki '{merkki}' sisältyy merkkijonoon '{merkkijono}'.")
else:
    print(f"Merkki '{merkki}' ei sisälly merkkijonoon '{merkkijono}'.")
print()
print("Selvitetään, onko sana palindromi.")
palindromi1=input("Anna testattava sana: ")
palindromi=palindromi1.lower()
kaannettyna= palindromi[::-1]
if palindromi==kaannettyna:
    print(f"Sana '{palindromi}' on palindromi.")
else:
    print(f"Sana ei ole palindromi.")
    print(f"Sana on etuperin '{palindromi}' ja takaperin '{kaannettyna}'.")
print("Kiitos ohjelman käytöstä.")
