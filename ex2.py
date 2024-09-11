# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = int(input("Quel est la quantité d'eau a assainir ? "))
print("Voici les matériaux requis pour l'assainissement de ", water_quantity, "L d'eau :")
print(f"- {water_quantity/5} filtre(s)")
print(f"- {water_quantity*3/5} lampes UV")
print(f"- {water_quantity*0.5/5} kg de chlore")