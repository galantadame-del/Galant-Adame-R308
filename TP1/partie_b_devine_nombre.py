"""
R3.08 - TP1 - Partie B : Mini-jeu "Devine le nombre"
L'ordinateur choisit un nombre entre 1 et 100, le joueur a 10 essais.
"""
import random

MIN, MAX = 1, 100
ESSAIS_MAX = 10


def demander_nombre(essai):
    """Demande un entier valide entre MIN et MAX au joueur."""
    while True:
        saisie = input(f"Essai {essai}/{ESSAIS_MAX} - Votre proposition : ").strip()
        if saisie.isdigit() and MIN <= int(saisie) <= MAX:
            return int(saisie)
        print(f"Veuillez entrer un entier entre {MIN} et {MAX}.")


def jouer():
    secret = random.randint(MIN, MAX)
    print(f"\nJ'ai choisi un nombre entre {MIN} et {MAX}. Vous avez {ESSAIS_MAX} essais !")

    for essai in range(1, ESSAIS_MAX + 1):
        proposition = demander_nombre(essai)
        if proposition < secret:
            print("C'est plus !")
        elif proposition > secret:
            print("C'est moins !")
        else:
            print(f"Bravo ! Trouvé en {essai} essai(s).")
            return essai

    print(f"Perdu ! Le nombre était {secret}.")
    return None


if __name__ == "__main__":
    while True:
        jouer()
        if input("\nRejouer ? (o/n) : ").strip().lower() != "o":
            break
