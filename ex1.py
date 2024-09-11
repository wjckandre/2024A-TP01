# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est le nom de l'athlète ? ")
date = input("Quel est la date du record ? ")
discipline = input("En quelle discipline ? ")
categorie = input("En quelle catégorie ? ")
record = input("Quel est le record ? ")
print("NOUVEAU RECORD")
print("-----------------------------")
print(date)
print(discipline, " - ", categorie)
print(athlete, country, " - ", record)