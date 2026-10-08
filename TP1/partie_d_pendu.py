"""
R3.08 - TP1 - Partie D : Jeu du Pendu (+ Bonus : Hall of fame)
7 erreurs maximum. Affiche le masque et les lettres déjà proposées.
"""
from partie_c_mots import charger_mots, choisir_mot, masque
from bonus_hall_of_fame import enregistrer_score, afficher_hall_of_fame

ERREURS_MAX = 7


def demander_lettre(lettres_proposees):
    """Demande une lettre unique, non encore proposée."""
    while True:
        lettre = input("Proposez une lettre : ").strip().upper()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Entrez UNE seule lettre.")
        elif lettre in lettres_proposees:
            print(f"Vous avez déjà proposé '{lettre}'.")
        else:
            return lettre


def jouer(mot):
    """Lance une partie du pendu. Retourne le nombre d'erreurs si gagné, None sinon."""
    lettres_proposees = set()
    lettres_trouvees = set()
    erreurs = 0

    while erreurs < ERREURS_MAX:
        print(f"\nMot : {masque(mot, lettres_trouvees)}")
        print(f"Lettres proposées : {' '.join(sorted(lettres_proposees)) or '-'}")
        print(f"Erreurs : {erreurs}/{ERREURS_MAX}")

        lettre = demander_lettre(lettres_proposees)
        lettres_proposees.add(lettre)

        if lettre in mot:
            lettres_trouvees.add(lettre)
            print("Bien joué !")
            if set(mot) <= lettres_trouvees:
                print(f"\nGagné ! Le mot était {mot} ({erreurs} erreur(s)).")
                return erreurs
        else:
            erreurs += 1
            print("Raté !")

    print(f"\nPendu ! Le mot était {mot}.")
    return None


def main():
    mots = charger_mots()
    pseudo = input("Votre pseudo : ").strip() or "Anonyme"
    while True:
        mot = choisir_mot(mots)
        erreurs = jouer(mot)
        if erreurs is not None:
            # Score : plus le mot est long et moins on fait d'erreurs, mieux c'est
            score = len(mot) * 10 - erreurs * 5
            enregistrer_score(pseudo, score)
            print(f"Score : {score} points.")
        afficher_hall_of_fame()
        if input("\nRejouer ? (o/n) : ").strip().lower() != "o":
            break


if __name__ == "__main__":
    main()
