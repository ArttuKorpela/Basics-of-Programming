aloitusarvo= int(input("Anna aloitusarvo: "))
lopetusarvo= int(input("Anna lopetusarvo: "))
print()
print("Toteutus for-lauseella:")
n=""
for numerot in range(aloitusarvo,lopetusarvo+1):
    n+=str(numerot)+" "
print(n)
print()
print("Toteutus while-lauseella:")
luku=aloitusarvo
lukujono=""
while luku!=lopetusarvo:
    luku+=1
    lukujono+=str(luku)+" "
print(aloitusarvo,lukujono)
print()
print("Kiitos ohjelman käytöstä.")
