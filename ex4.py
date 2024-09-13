# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))
distance = 0
if battery_level == 0:
    print("La batterie est vide")
else:
    for i in range(int(battery_level*2), 0, -1):
        if i >= 50*2 and i <= 100*2:
            distance += 1
        elif i >= 25*2:
            distance += 0.25
        elif i >= 10*2:
            distance += 0.5
        elif i >= 5*2:
            distance += 1.25
        elif i >= 0*2:
            distance += 3
    print(f"{float(distance)} km")
