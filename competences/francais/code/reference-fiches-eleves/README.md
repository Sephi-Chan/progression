# Référence autonome — Fiches élèves de lecture

Ce dossier rassemble tout ce qu’il faut transmettre à un futur générateur. Il peut être copié ou déplacé en entier : aucun fichier ne dépend de l’arborescence P1.

## Fichiers

- [CHARTE_FICHES_ELEVES.md](CHARTE_FICHES_ELEVES.md) : règles de contenu, de Markdown, de présentation et de validation ; instruction prête à transmettre.
- [style.css](style.css) : feuille de style validée, commune aux exemples et aux futures fiches.
- [exemple.md](exemple.md) : contenu S01 illustrant les conventions.
- [exemple.html](exemple.html) : conversion directe du Markdown, avec CSS intégré pour faciliter son partage.
- [exemple.pdf](exemple.pdf) : rendu imprimable de référence, cinq pages.
- [generer.py](generer.py) : convertisseur autonome, adaptable à d’autres contenus et nombres de pages.
- [requirements.txt](requirements.txt) : dépendances Python utilisées.

Le contenu S01 sert d’exemple, sans imposer ses rubriques ou ses quantités à un futur document. Le PDF fait foi pour la pagination et les en-têtes prénom/date ; l’affichage HTML à l’écran est continu.

## Utilisation

Depuis ce dossier, dans un environnement Python disposant des dépendances :

```sh
python3 generer.py --pages 5
```

Pour un autre Markdown :

```sh
python3 generer.py chemin/vers/fiche.md
```

Le script lit le CSS situé à côté de lui et écrit le HTML et le PDF à côté du Markdown. Il remplace ces deux sorties si elles existent. L’option `--pages` est facultative : cinq pages n’est pas une contrainte générale.

Les dépendances Python peuvent être installées dans un environnement virtuel avec `pip install -r requirements.txt`. WeasyPrint nécessite également ses bibliothèques système ; le dossier est autonome pour les documents, pas un environnement d’exécution embarqué.

## Statut de cette référence

Le Markdown et le CSS sont des copies de la version validée, destinées à rester disponibles même si les fichiers de travail P1 bougent. Ils ne sont pas synchronisés automatiquement avec P1. Faire évoluer ce dossier explicitement lorsqu’une nouvelle version de référence est validée, puis régénérer ses exemples.

Pour transmettre la documentation, copier le dossier entier. Pour une transmission minimale à un générateur, fournir la charte et le CSS ; ajouter l’exemple Markdown et le PDF pour montrer le résultat attendu.
