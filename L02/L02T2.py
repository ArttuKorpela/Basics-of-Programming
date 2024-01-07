merkki = input("Anna auton merkki: ")
malli = input("Anna auton malli: ")
merkki_ja_malli = merkki +" "+ malli
print(f'Auto on {merkki}, {merkki_ja_malli}.\n')

ensimmainen_sana = input("Anna ensimmäinen sana: ")
toinen_sana = input("Anna toinen sana: ")
yhdyssana = ensimmainen_sana.lower()+toinen_sana.lower()

print(f"Sanoista tulee yhdyssana '{yhdyssana}'.")
print("Kiitos ohjelman käytöstä.")