"""
R3.08 - TP1 - Partie C : Manipulation des mots
Chargement d'une liste de mots, choix aléatoire et calcul du masque.
"""
import random
from pathlib import Path

FICHIER_MOTS = Path(__file__).parent / "mots.txt"


def charger_mots(chemin=FICHIER_MOTS):
    """Charge la liste des mots (un par ligne) depuis un fichier texte."""
    with open(chemin, encoding="utf-8") as f:
        return [ligne.strip() for ligne in f if ligne.strip()]


def choisir_mot(mots):
    """Choisit un mot au hasard et le retourne en MAJUSCULES."""
    return random.choice(mots).upper()


def masque(mot, lettres_trouvees):
    """Retourne le mot masqué : lettres trouvées visibles, les autres remplacées par '_'.

    >>> masque("PYTHON", {"P", "O"})
    'P _ _ _ O _'
    """
    return " ".join(lettre if lettre in lettres_trouvees else "_" for lettre in mot)


if __name__ == "__main__":
    mots = charger_mots()
    print(f"{len(mots)} mots chargés : {mots}")
    mot = choisir_mot(mots)
    print(f"Mot choisi : {mot}")
    print(f"Masque vide      : {masque(mot, set())}")
    print(f"Masque avec voyelles : {masque(mot, set('AEIOUY'))}")
    print(f"Masque complet   : {masque(mot, set(mot))}")
