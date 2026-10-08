"""
R3.08 - TP1 - Bonus : Hall of fame
Les scores sont stockés dans scores.txt sous la forme 'pseudo;score'.
"""
from pathlib import Path

FICHIER_SCORES = Path(__file__).parent / "scores.txt"
TOP = 5


def charger_scores(chemin=FICHIER_SCORES):
    """Retourne la liste des (pseudo, score) triée par score décroissant."""
    scores = []
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ";" in ligne:
                    pseudo, score = ligne.rsplit(";", 1)
                    scores.append((pseudo, int(score)))
    except FileNotFoundError:
        pass
    return sorted(scores, key=lambda s: s[1], reverse=True)


def enregistrer_score(pseudo, score, chemin=FICHIER_SCORES):
    """Ajoute un score à la fin du fichier."""
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(f"{pseudo};{score}\n")


def afficher_hall_of_fame(chemin=FICHIER_SCORES, top=TOP):
    scores = charger_scores(chemin)
    print("\n=== HALL OF FAME ===")
    if not scores:
        print("Aucun score pour le moment.")
        return
    for rang, (pseudo, score) in enumerate(scores[:top], start=1):
        print(f"{rang}. {pseudo:<15} {score:>4} pts")


if __name__ == "__main__":
    afficher_hall_of_fame()
