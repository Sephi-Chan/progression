# Étude du code — CE1 — Période 2

Sept semaines, du lundi au vendredi sur quatre jours de classe. Chaque semaine propose quatre fiches pour le rituel et un récit préparé à lire pendant un autre temps de lecture. Les créneaux durent de 5 à 10 minutes et suivent la [programmation locale](../programmation_code_CE1_32_semaines.md#période-2--deuxième-passage-et-automatisation).

## À imprimer

- [Recueil élèves — 38 pages](PDF/P2_RECUEIL_ELEVES.pdf). Imprimer en A4 à taille réelle.
- [Guide enseignant — 15 pages](PDF/GUIDE_ENSEIGNANT.pdf). Il indique le modelage, les parcours, les aides et les corrections. Les dernières pages donnent le protocole, la grille de relevé et le texte de pointage du bilan.
- [Bilan élève — 3 pages](PDF/BILAN_S14.pdf). Réserver ces pages à la passation individuelle. La fiche du jeudi de semaine 14 permet aux autres élèves de relire un corpus connu pendant la passation.

| Semaine | Travail principal | Source éditable | PDF séparé | Pages du recueil |
| --- | --- | --- | --- | --- |
| 8 | Nasales et valeurs de s/ss | [Markdown](S08_FICHES_ELEVES.md) | [PDF](PDF/S08_FICHES_ELEVES.pdf) | 1–5 |
| 9 | oi/oin, y et ill | [Markdown](S09_FICHES_ELEVES.md) | [PDF](PDF/S09_FICHES_ELEVES.pdf) | 6–10 |
| 10 | ien/oin/ion et groupes consonantiques | [Markdown](S10_FICHES_ELEVES.md) | [PDF](PDF/S10_FICHES_ELEVES.pdf) | 11–15 |
| 11 | é/è et finales er/ez/et | [Markdown](S11_FICHES_ELEVES.md) | [PDF](PDF/S11_FICHES_ELEVES.pdf) | 16–20 |
| 12 | x/ph et valeurs de c/g/s/x | [Markdown](S12_FICHES_ELEVES.md) | [PDF](PDF/S12_FICHES_ELEVES.pdf) | 21–25 |
| 13 | e devant consonnes, consonnes doubles et mots longs | [Markdown](S13_FICHES_ELEVES.md) | [PDF](PDF/S13_FICHES_ELEVES.pdf) | 26–30 |
| 14 | Synthèse et reprise cumulative | [Markdown](S14_FICHES_ELEVES.md) | [PDF](PDF/S14_FICHES_ELEVES.pdf) | 31–35 |
| Bilan | Précision, encodage et lecture de texte selon le profil | [Markdown](BILAN_S14.md) | [PDF](PDF/BILAN_S14.pdf) | 36–38 |

## Utiliser le dossier

- Choisir avec le [guide enseignant modifiable](GUIDE_ENSEIGNANT.md) la quantité de mots, les aides et la reprise selon les erreurs observées.
- En dictée, cacher le corpus après sa lecture et annoncer les aides prévues. Vérifier séparément la graphie travaillée et l’orthographe complète.
- Prévoir le bilan sur plusieurs temps de lecture. Conserver séparément le relevé des listes et le résultat sur texte. Les résultats ou observations de P1, s’ils sont disponibles, aident à choisir les premières reprises.

## Modifier et régénérer

Les fiches reprennent la [charte élèves](../reference-fiches-eleves/CHARTE_FICHES_ELEVES.md). Le Markdown fournit le contenu et les feuilles CSS gèrent la présentation. Dans le front matter des sources élèves, conserver un repère en toutes lettres par titre de niveau 1, dans le même ordre. Il apparaît discrètement en pied de page.

Les versions des dépendances sont indiquées dans [requirements.txt](requirements.txt). Dans le dossier P2, régénérer les exports HTML et PDF avec :

```sh
python3 generer_pdf.py
```

Les dossiers [HTML](HTML/) et [PDF](PDF/) contiennent les exports. Le générateur vérifie la correspondance entre titres et pages, les en-têtes et la présence des repères. Après une modification du nombre de pages, vérifier le rendu et mettre à jour le tableau.
