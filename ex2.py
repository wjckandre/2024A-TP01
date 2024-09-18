# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
print(f"""Voici les éléments requis pour assainir {(water_quantity)}L d'eau:
\t- Filtre(s) : {int(water_quantity/5)}
\t- Lampe(s) UV : {int(water_quantity*3/5)}
\t- Chlore : {water_quantity*0.5/5}kg""")