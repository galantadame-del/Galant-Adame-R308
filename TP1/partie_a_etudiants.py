"""
R3.08 - TP1 - Partie A : Dictionnaire d'étudiants
Gestion des notes d'une classe avec un dictionnaire {nom: note}.
"""
from pathlib import Path

DOSSIER = Path(__file__).parent
FICHIER_DONNEES = DOSSIER / "donnees.txt"


def ajouter_etudiant(classe, nom, note):
    """Ajoute (ou met à jour) un étudiant et sa note dans le dictionnaire."""
    if not 0 <= note <= 20:
        raise ValueError("La note doit être comprise entre 0 et 20.")
    classe[nom] = float(note)


def moyenne_classe(classe):
    """Retourne la moyenne des notes de la classe (None si la classe est vide)."""
    if not classe:
        return None
    return sum(classe.values()) / len(classe)


def meilleur_etudiant(classe):
    """Retourne le tuple (nom, note) du meilleur étudiant (None si vide)."""
    if not classe:
        return None
    nom = max(classe, key=classe.get)
    return nom, classe[nom]


def sauvegarder(classe, chemin=FICHIER_DONNEES):
    """Sauvegarde le dictionnaire dans un fichier texte, une ligne 'nom note' par étudiant."""
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in classe.items():
            f.write(f"{nom} {note:g}\n")


def charger(chemin=FICHIER_DONNEES):
    """Charge un dictionnaire {nom: note} depuis un fichier texte."""
    classe = {}
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                nom, note = ligne.rsplit(maxsplit=1)
                classe[nom] = float(note)
    except FileNotFoundError:
        print(f"Fichier {chemin} introuvable, classe vide.")
    return classe


def afficher(classe):
    """Affiche la liste des étudiants et leurs notes."""
    if not classe:
        print("Aucun étudiant.")
        return
    for nom, note in classe.items():
        print(f"  - {nom:<15} {note:>5.2f}/20")


def menu():
    classe = charger()
    while True:
        print("\n=== Gestion des étudiants ===")
        print("1. Afficher les étudiants")
        print("2. Ajouter un étudiant")
        print("3. Moyenne de la classe")
        print("4. Meilleur étudiant")
        print("5. Sauvegarder")
        print("0. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher(classe)
        elif choix == "2":
            nom = input("Nom : ").strip()
            try:
                note = float(input("Note (/20) : ").replace(",", "."))
                ajouter_etudiant(classe, nom, note)
                print(f"{nom} ajouté(e).")
            except ValueError as e:
                print(f"Erreur : {e}")
        elif choix == "3":
            moy = moyenne_classe(classe)
            print("Classe vide." if moy is None else f"Moyenne : {moy:.2f}/20")
        elif choix == "4":
            best = meilleur_etudiant(classe)
            print("Classe vide." if best is None else f"Meilleur : {best[0]} ({best[1]:g}/20)")
        elif choix == "5":
            sauvegarder(classe)
            print(f"Sauvegardé dans {FICHIER_DONNEES.name}.")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
