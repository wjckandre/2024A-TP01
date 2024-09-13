# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
from math import *

speed = float(input("Vitesse initiale (m/s): "))
angle = int(input("Angle de lancer (en degrés): "))*pi/180
d = round((pow(speed,2)*sin(2*angle))/9.8,2)
print(f"Distance parcourue: {d}m")
