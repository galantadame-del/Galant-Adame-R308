# Galant-Adame-R308

Travaux pratiques de la ressource **R3.08 – Programmation Orientée Objet en Python**.

**Auteur :** Adame GALANT

## Arborescence

```
Galant-Adame-R308/
├── README.md
├── .gitignore
├── TP1/
│   ├── partie_a_etudiants.py      # Partie A : dictionnaire d'étudiants
│   ├── partie_b_devine_nombre.py  # Partie B : devine le nombre
│   ├── partie_c_mots.py           # Partie C : manipulation des mots
│   ├── partie_d_pendu.py          # Partie D : jeu du pendu
│   ├── bonus_hall_of_fame.py      # Bonus : hall of fame (scores.txt)
│   ├── donnees.txt                # Notes des étudiants
│   └── mots.txt                   # Liste de mots pour le pendu
├── TP2/
└── TP3/
```

## TP1

| Partie | Fichier | Contenu |
|---|---|---|
| A | `partie_a_etudiants.py` | `ajouter_etudiant`, `moyenne_classe`, `meilleur_etudiant`, sauvegarde/chargement dans `donnees.txt` |
| B | `partie_b_devine_nombre.py` | Nombre aléatoire entre 1 et 100, 10 essais max, indications plus/moins |
| C | `partie_c_mots.py` | `charger_mots`, `choisir_mot` (en MAJUSCULES), `masque` |
| D | `partie_d_pendu.py` | Pendu, 7 erreurs max, affichage du masque et des lettres proposées |
| Bonus | `bonus_hall_of_fame.py` | Scores enregistrés dans `scores.txt`, affichage du top 5 |

## Exécution

Python 3.8+ requis, aucune dépendance externe.

```bash
cd TP1
python partie_a_etudiants.py
python partie_b_devine_nombre.py
python partie_c_mots.py
python partie_d_pendu.py
```
