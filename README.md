# HCR-Simple-Memory-Modifier


## 💡 Projet Éducatif : Manipulation de Mémoire de Jeu Solo

Ce projet est une application d'apprentissage conçue pour illustrer les principes fondamentaux de l'interaction avec la mémoire d'un processus de jeu **solo (hors ligne)** sur PC. Il permet de modifier les valeurs de ressources (pièces et diamants) dans le jeu **Hill Climb Racing (v1.41.1.0)**.

**L'objectif principal est l'éducation :** comprendre comment les données sont stockées dans la mémoire d'un programme et comment les modifier à l'aide d'outils de programmation comme `pymem` et `tkinter`.

### 🛠️ Technologies Utilisées

* **Python** : Langage de programmation principal.
* **`pymem`** : Bibliothèque Python essentielle pour lire et écrire dans la mémoire des processus Windows.
* **`tkinter`** : Utilisé pour créer l'interface graphique utilisateur (GUI) de l'outil.
* **Concepts de Hacking Éthique** : Adresses statiques (basiques) et manipulation de processus.

### 📚 Ce que j'ai appris avec ce projet

Ce projet a été une excellente pratique pour maîtriser :

1.  **L'attachement à un Processus (`Pymem`)** : Comment localiser et se connecter à la mémoire d'une application cible (`HillClimbRacing.exe`).
2.  **L'adressage Mémoire** : Comment identifier et utiliser des **adresses statiques** (`address_money`, `address_diams`) pour cibler des variables spécifiques du jeu.
3.  **Le Développement GUI** : Création d'une interface utilisateur fonctionnelle avec `tkinter` pour interagir avec mon script Python.
4.  **La Sécurité des Jeux** : Comprendre le rôle des valeurs côté client (faciles à modifier) par opposition aux valeurs côté serveur (sécurisées en multijoueur).

### ⚙️ Guide d'Installation (Pour ceux qui veulent apprendre)

1.  **Prérequis** : Assurez-vous d'avoir Python installé sur votre machine.
2.  **Installation des Dépendances** :
    ```bash
    pip install pymem
    ```
3.  **Exécution** :
    ```bash
    python votre_script_principal.py
    ```

**🚨 Avertissement :** Ce script ne doit être utilisé que sur des jeux solo ou des environnements de test personnels. Toute tentative d'utiliser cette méthode sur des jeux multijoueurs ou des systèmes tiers est illégale et contraire à l'éthique. Ce projet est strictement à des fins éducatives.
