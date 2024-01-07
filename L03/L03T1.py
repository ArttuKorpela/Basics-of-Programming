print("Anna kaksi kokonaislukua.")
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
print("Selvitetään, ovatko antamasi luvut parillisia.")
lista = [luku1,luku2]
for numero in lista:
    jakojaannos = int(numero)%2
    if int(jakojaannos) == 0:
        print(f"Luku {numero} on parillinen.")
    else:
        print(f"Luku {numero} on pariton.")
print("Selvitetään, kumpi antamistasi luvuista on pienempi.")
if luku1>luku2:
    print(f"Luku {luku2} on pienempi.")
elif luku2>luku1:
    print(f"Luku {luku1} on pienempi.")
else:
    print(f"Luvut {luku1} ja {luku2} ovat yhtäsuuria.")
print("Kiitos ohjelman käytöstä.")