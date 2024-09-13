#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

Gold = 0
Silver = 0
Bronze = 0
flag = False

for i in code_medals:
    if i == "G":
        Gold += 1
    elif i == "S":
        Silver += 1
    elif i == "B":
        Bronze += 1
    else:
        flag = True
if flag:
    print("Veuillez entrer une chaîne valide.")
else:
    print(f"{country}:\n- {Gold} OR\n- {Silver} Argent\n- {Bronze} Bronze")
