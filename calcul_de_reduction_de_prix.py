#mini_reduction.py

def calculer_reduction(prix_initial, statut_etudiant, annees_fidelite, code_promo):
    reduction = 0.0

    
    if annees_fidelite >= 5:
        print ("vous bénéficiez d'une réduction de fidélité de 15%")
        reduction += prix_initial * 0.15  # 15 %
    elif statut_etudiant =="o":
        print ("vous bénéficiez d'une réduction étudiante de 10%")
        reduction += prix_initial * 0.10  # 10 %
    elif code_promo == "PROMO2025":
        print ("vous bénéficiez d'une réduction de code promo de 6%")
        reduction += prix_initial * 0.06  # 6% de réduction supplémentaire
    elif prix_initial > 100:
        print (f"vous bénéficiez d'une réduction de 5 {devise}")
        reduction += 5.0  # réduction fixe supplémentaire
    else :
        print ("vous bénéficiez d'une réduction de 2%")
        reduction += prix_initial * 0.02  # 2% de réduction supplémentaire
    return reduction
print("choisissez vote devise :")
print("1:Euro (€)")
print("2:Dollar ($)")
print("3:Livre (£)")
choix =input("entrez votre choix(1/2/3) ")

if choix == "1":
    devise = "€"
elif choix == "2":
    devise = "$"
elif choix == "3":
    devise = "£"
else:
    print("Choix invalide, la devise par défaut sera €.")
    devise = "€"
reponse="o"
    
while reponse=="o":
    try:
        prix_initial = float(input("Prix du produit : "))
        if prix_initial < 0:
            print("Le prix ne peut pas être négatif.")
            continue 
    except ValueError:
        print("Saisie invalide pour le prix.")
        exit(1)

    statut = input("Êtes-vous étudiant ? (o/n) ").strip().lower()
    fidelite = input("Fidélité (en années) : ").strip()

    try:
        fidelite = int(fidelite)
    except ValueError:
        print("Saisie invalide pour la fidélité.")
        exit(1)
    CPromo=input("Avez-vous un code promo ? (o/n) ").strip().lower()
    code_promo=""
    if CPromo=="o":
        code_promo=input("Entrez le code promo : ").strip() 
    reduction = calculer_reduction(prix_initial, statut, fidelite, code_promo)
    prix_final = prix_initial - reduction
    if prix_final < 0:
        prix_final = 0.0  # garde-fou

    print(f"Réduction totale : {reduction:.2f} {devise}")
    print(f"Prix final : {prix_final:.2f}{devise}")
    reponse=input("voulez-vous refaire un calcul de réduction ? (o/n) ")
    
print("\n Merci pour votre achat !")
