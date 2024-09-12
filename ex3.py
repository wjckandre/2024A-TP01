# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
from math import *

speed = float(input("Quel est la vitesse de lancer ? "))
angle = float(input("Quel est l'angle de lancement ? "))*pi/180
d = (pow(speed,2)*sin(2*angle))/9.81
print(f"La distance maximale en x est de {d}")
