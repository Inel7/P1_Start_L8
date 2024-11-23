from sterren_module import *
import random
kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

for i in range(1000):
    x = random.randint(-350, 350)
    y = random.randint(-300, 300)
    kleur = random.choice(kleuren)

    teken_ster(x,y,kleur)
