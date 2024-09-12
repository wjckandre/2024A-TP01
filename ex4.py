# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Pourcentage de batterie : "))
distance = 0
for i in range(battery_level, 0, -1):
    if i > 50 and i <= 100:
        distance += 2
    elif i > 25:
        distance += 0.5
    elif i > 10:
        distance += 1
    elif i > 5:
        distance += 2.5
    elif i > 0:
        distance += 6
print(f"La distance possible est de {int(distance)} km")
