import random

kleuren = ["rood", "blauw", "groen", "geel", "paars", "oranje"]
willekeurige_kleur = random.choice(kleuren)
print("Willekeurig gekozen kleur:", willekeurige_kleur)

def genereer_gebruikersnaam():
    besschrijving = ["Super","Mega","Ultra","Toffe","Magische"]
    rol = ["Coder","Ninja","Expert","Gamer"]

    for i in range(10):
        wilk_beschrijving = random.choice(besschrijving)
        wilk_rol = random.choice(rol)
        print(wilk_beschrijving, wilk_rol)
genereer_gebruikersnaam()

willekeurig_geheel_getal = random.randint(1,10)
print("willekeurig getal :",willekeurig_geheel_getal)