import random
import math


proizvodi = ["Macbook M2", "iPhone 14 Pro", "iPad 11", "Apple Watch", "AirPods 2gen", "AppleTV", "Canon G7X", "Playstation 5"]

cene = {
    "Macbook M2": 1500,
    "iPhone 14 Pro": 1200,
    "iPad 11": 500,
    "Apple Watch": 400,
    "AirPods 2gen": 200.588,
    "AppleTV": 200.53,
    "Canon G7X": 800,
    "Playstation 5": 600
}

for proizvod in proizvodi:
    print(proizvod,"-", cene[proizvod], "€")

budzet = int(input("Unesite svoj budzet:"))
print("Proizvodi koje mozete kupiti sa budzetom od", budzet, "€ su:")

for proizvod in proizvodi:
    if(cene[proizvod]<=budzet):
        print(proizvod,"-", cene[proizvod], "€")

def najskuplji_proizvod():
    najskuplji_proizvod=max(cene, key=cene.get)
    return najskuplji_proizvod

print("Najskuplji proizvod je:", najskuplji_proizvod(), "-", cene[najskuplji_proizvod()], "€")

random_proizvod = random.choice(proizvodi)
print("Nasumicno odabrani proizvod je:", random_proizvod)

zbir = sum(cene.values())
prosek = zbir / len(proizvodi);
print("Prosek je ",prosek)
print("Prosecna cena proizvoda je ", math.ceil(prosek * 100) / 100)

prodati_komadi = [5, 20, 10, 3, 7, 4, 25, 12]

ukupan_prihod =0

for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]


print("Ukupan prihod od prodaje svih proizvoda je:", ukupan_prihod, "€")

novi_proizvod = input("Unesite naziv novog proizvoda:")
nova_cena = float(input("Unesite cenu novog proizvoda:"))

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("Azurirana lista proizvoda:")
for proizvod in proizvodi:
        print(proizvod,"-", cene[proizvod], "€")



sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("Proizvodi sortirani po ceni:")
for proizvod, cena in sortirani_proizvodi:
    print(proizvod, "-", cena, "€")