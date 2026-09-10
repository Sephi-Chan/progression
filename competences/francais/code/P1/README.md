# Fiches élèves de code — CE1 — P1

Les supports élèves suivent la [charte validée](../reference-fiches-eleves/CHARTE_FICHES_ELEVES.md) : Markdown simple, mots à lire en 16 pt, grilles à trois colonnes, prénom et date en en-tête CSS. Les corpus existants et leur ordre sont conservés. Les parcours, corrections et références restent dans les documents enseignants. Un bloc de métadonnées invisible à l’impression fournit maintenant les codes discrets en pied de page.

## Documents prêts à utiliser

Le [recueil élèves complet](PDF/P1_RECUEIL_ELEVES.pdf) contient **41 pages**, avec une pagination continue.

| Support | Markdown | PDF | Pages dans le recueil |
| --- | --- | --- | --- |
| Diagnostic de rentrée | [Source](DIAGNOSTIC_S01.md) | [PDF](PDF/DIAGNOSTIC_S01.pdf) | 1–3 |
| Semaine 1 | [Source](S01_FICHES_ELEVES.md) | [PDF](PDF/S01_FICHES_ELEVES.pdf) | 4–8 |
| Semaine 2 | [Source](S02_FICHES_ELEVES.md) | [PDF](PDF/S02_FICHES_ELEVES.pdf) | 9–13 |
| Semaine 3 | [Source](S03_FICHES_ELEVES.md) | [PDF](PDF/S03_FICHES_ELEVES.pdf) | 14–18 |
| Semaine 4 | [Source](S04_FICHES_ELEVES.md) | [PDF](PDF/S04_FICHES_ELEVES.pdf) | 19–23 |
| Semaine 5 | [Source](S05_FICHES_ELEVES.md) | [PDF](PDF/S05_FICHES_ELEVES.pdf) | 24–28 |
| Semaine 6 | [Source](S06_FICHES_ELEVES.md) | [PDF](PDF/S06_FICHES_ELEVES.pdf) | 29–33 |
| Semaine 7 | [Source](S07_FICHES_ELEVES.md) | [PDF](PDF/S07_FICHES_ELEVES.pdf) | 34–38 |
| Bilan de fin de période | [Source](BILAN_S07.md) | [PDF](PDF/BILAN_S07.pdf) | 39–41 |

Chaque semaine comporte quatre pages de rituel et une page de récit. Les fichiers séparés ont leur propre pagination. Imprimer en A4 à **100 % / taille réelle**. Les diagnostics et bilans sont réservés à la passation individuelle, sans entraînement préalable sur ces supports.

Lire le [guide enseignant synthétique](GUIDE_ENSEIGNANT.md), également disponible en [PDF — 6 pages](PDF/GUIDE_ENSEIGNANT.pdf), pour les parcours, les aides, les dictées et les corrections. Le [guide détaillé](GUIDE_ENSEIGNANT_DETAILLE.md) conserve les inventaires, les grilles et les protocoles complets. Les [notes de présentation](NOTES_ENSEIGNANT_MISE_EN_PAGE.md) conservent les indications de passation retirées des fiches. Les identifiants d’items restent dans le guide. Seul le code de la fiche apparaît, en gris clair, en bas à gauche.

## Modifier et régénérer

Modifier les fichiers Markdown pour le contenu, [style.css](style.css) pour les fiches élèves et [style_enseignant.css](style_enseignant.css) pour le guide synthétique. Les [exports HTML](HTML/P1_RECUEIL_ELEVES.html) servent à consulter la conversion ; le PDF fait foi pour les pages et les en-têtes automatiques.

Depuis ce dossier :

```sh
python3 generer_pdf.py
```

Le [générateur](generer_pdf.py) utilise `markdown-it-py`, WeasyPrint et PyYAML ; les versions sont indiquées dans [requirements.txt](requirements.txt). Il régénère les neuf supports élèves, le recueil de 41 pages et le guide enseignant synthétique séparé dans `HTML/` et `PDF/`. Il n’ajoute ni classes ni identifiants au contenu. Le guide détaillé est conservé en Markdown et n’est pas réexporté automatiquement.

Le CSS local reprend la référence avec une adaptation générique des bordures aux dernières rangées incomplètes : certaines grilles ont 8 ou 16 items. Un espace de 4 mm entre les colonnes distingue les groupes de mots les plus longs. Les mots, groupes de mots et exercices à trous sont des listes Markdown. Les récits sont des blocs `>`, les phrases et les lignes d’écriture des listes numérotées.

Le script compose et valide tout le lot avant de remplacer les exports. Il contrôle les en-têtes, les codes et les débordements hors page. Pour les élèves, il exige un titre `#` et un code par page afin d’éviter un décalage des pieds de page. Si une fiche déborde, il demande de répartir le contenu explicitement et d’ajouter le code correspondant. Le nombre total de fiches peut changer. Après modification, vérifier le rendu et mettre à jour le tableau ci-dessus si nécessaire.

Pour les dictées, masquer la grille de lecture et la ligne d’aide. Un cache de papier suffit. Les trous n/m ne demandent que le choix de cette lettre ; les autres graphies sont fournies.

## Codes de fiches : métadonnées invisibles à l’impression

Chaque fichier élève commence par un bloc YAML, retiré avant conversion :

```yaml
---
codes_fiches:
- P1 S1 J1
- P1 S1 J2
- P1 S1 J3
- P1 S1 J4
- P1 S1 TEXTE
---
```

Les codes suivent **exactement l’ordre des titres `#`**. Si tu ajoutes, supprimes ou déplaces une fiche, ajuste cette liste en même temps. Le générateur vérifie le nombre de titres, de codes et de pages, mais ne peut pas deviner le sens d’un titre ni détecter un code sémantiquement incorrect que tu aurais saisi.

J1 = lundi, J2 = mardi, J3 = jeudi, J4 = vendredi. Le diagnostic utilise `P1 S1 DIAG CODE`, `P1 S1 DIAG MOTS`, `P1 S1 DIAG TEXTE` ; le bilan suit le même principe avec `P1 S7 BILAN`.

Les codes sont conservés dans le recueil indépendamment de sa pagination continue. Ils sont dessinés par les boîtes CSS `@bottom-left`, en 8 pt et `#aaa`. Modifier ces deux valeurs dans `style.css` pour ajuster leur discrétion à l’imprimante. Le Python ne génère que les règles `@page :nth(...)` qui associent chaque page à son code.

Cette métadonnée est une extension demandée après la validation de la charte : elle ne réintroduit aucun HTML dans le Markdown. Le guide enseignant n’a pas besoin de ce bloc.

## Provenance et sources

Les textes hebdomadaires et les textes de passation sont créés pour l’exercice. Leur provenance, les choix pédagogiques et les références institutionnelles sont documentés dans le [guide enseignant](GUIDE_ENSEIGNANT.md#sources). La présente reprise porte sur la présentation et les consignes des supports existants ; elle ne constitue pas une nouvelle vérification institutionnelle ou une modification de la progression.
