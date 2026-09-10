# Charte de génération des fiches élèves de lecture

Cette charte formalise les choix de contenu et de présentation validés sur les fiches S01. Elle s’adresse à un futur générateur, même si les sons, les activités, le nombre de mots ou le nombre de pages changent.

Le résultat attendu est une fiche sobre, claire et confortable pour de jeunes lecteurs. La hiérarchie repose sur les titres, les espacements et quelques lignes de guidage. Elle ne repose pas sur une multiplication des tailles, des cadres ou des décorations.

## Livrables et références

Produire un Markdown éditable, un HTML issu de sa conversion directe et un PDF imprimable. La mise en forme appartient à une feuille CSS séparée.

Références validées, avec chemins relatifs à cette charte :

- [Markdown S01](exemple.md).
- [Feuille de style de référence](style.css).
- [PDF de référence](exemple.pdf).
- [Convertisseur autonome](generer.py).

Pour transmettre ce travail à un autre générateur, fournir cette charte et `style.css`. Ajouter le Markdown S01 comme exemple, sans en faire un contenu à reproduire obligatoirement. La feuille CSS est la source de vérité des valeurs de présentation ; les valeurs ci-dessous en décrivent la version validée.

## 1. Séparer contenu, présentation et conversion

Le Markdown contient uniquement le contenu destiné à l’élève et sa structure. Ne pas y ajouter de HTML, de bloc `<style>`, de classes CSS, d’identifiants ou de marqueurs techniques de pagination.

Le Python convertit le Markdown en HTML et applique le CSS. Il ne doit pas :

- reconnaître des phrases ou des titres pour leur attribuer un style ;
- ajouter des classes telles que `small`, `path`, `vocabulary`, `reading` ou `sheet` ;
- fabriquer des enveloppes HTML pour des activités particulières ;
- découper les titres ou reconstruire les listes pour leur présentation ;
- appliquer des exceptions en fonction du jour, du numéro de page ou du contenu d’un mot.

Les liens peuvent être adaptés au dossier de sortie. Le document HTML peut recevoir les éléments standards nécessaires : langue, encodage, titre et feuille de style. Les éléments du contenu restent ceux produits normalement par le parseur Markdown.

## 2. Contrat Markdown

| Syntaxe | Usage | Rendu attendu |
| --- | --- | --- |
| `# Titre` | Début d’une fiche | Titre principal ; commence une nouvelle page à l’impression |
| `## Rubrique` | Activité ou partie de la fiche | Intertitre sobre, en gras, séparé par de l’espace |
| Paragraphe | Rappel, consigne indispensable, mots aidés, question | Texte courant de même taille que les mots à lire |
| `- mot` | Liste de mots ou groupes de mots | Grille de trois colonnes, sans puces visibles |
| `1. Phrase` | Phrases à lire ou réponses numérotées | Liste verticale avec numéros de même taille que le texte |
| `> Texte` | Passage suivi à lire | Bloc de lecture aéré, sans guillemets ni bordure latérale ajoutés |
| `---` | Séparation utile dans une fiche | Filet horizontal ; ce n’est pas un saut de page |

Toutes les listes à puces deviennent des grilles. Ne pas utiliser cette syntaxe pour une liste de consignes, de matériel ou de notes. Les listes imbriquées ne font pas partie du format retenu.

Ne pas utiliser un tableau Markdown pour la grille de mots. Écrire un item par ligne, dans l’ordre de lecture : les trois premiers items occupent la première rangée, les trois suivants la deuxième, etc.

Le bloc `>` distingue le passage à lire des instructions qui suivent. Séparer les paragraphes du récit par une ligne contenant uniquement `>`. Cette convention de mise en page n’attribue pas le texte à un auteur.

Pour une ligne de réponse, une forme simple suffit : `1. \____________________________`. L’antislash empêche l’interprétation du soulignement comme une mise en forme Markdown.

## 3. Contenu visible par l’élève

Conserver des titres courts et informatifs : le son, les graphies, une notion ou le titre du récit. Le jour est facultatif. Les rubriques peuvent changer selon l’activité : ne pas imposer systématiquement les rubriques de S01.

Supprimer les éléments suivants de la fiche élève :

- codes internes comme `P1-S01-J2`, identifiants d’items et informations de suivi technique ;
- prénom et date saisis dans le Markdown : ils sont ajoutés par CSS ;
- mentions de fabrication comme « Texte créé pour l’exercice » ;
- explications destinées au professeur sur les parcours, l’évaluation ou le relevé de code ;
- consignes qui répètent simplement le titre, par exemple « Lis les mots » après « Je lis les mots » ;
- rappels répétés après chaque exercice, sans nécessité propre à la tâche.

Garder une consigne lorsqu’elle apporte une action que le titre ne précise pas : « Entoure les lettres du son qui glisse » ou « Cache les mots et écris le mot dicté ». Une question de compréhension et les mots à préparer avec l’adulte restent utiles.

Les mentions de provenance d’un texte créé et les précisions pédagogiques vont dans le document enseignant associé. Pour une œuvre réelle, conserver l’attribution et respecter les conditions de réutilisation ; cette charte ne permet pas de supprimer une attribution nécessaire ni de présenter un texte inventé comme une œuvre publiée.

Ne pas modifier la difficulté ou supprimer une aide nécessaire uniquement pour gagner de la place.

## 4. Typographie et espacements

Utiliser la famille générique `sans-serif`. Aucune police nommée, téléchargée, embarquée volontairement par le générateur ou déclarée avec `@font-face`. L’incorporation automatique de la police de substitution dans le PDF par WeasyPrint est normale.

| Élément | Valeurs validées |
| --- | --- |
| Texte courant et tous les éléments à lire | 16 pt ; interligne 1,5 ; couleur `#181818` |
| Titre principal | 23 pt ; interligne 1,2 ; marge inférieure 5 mm |
| Intertitre | 13 pt ; gras ; interligne 1,4 ; marge supérieure 7 mm, inférieure 3 mm ; espacement intérieur supérieur 4 mm |
| Paragraphes | Marges verticales 3 mm |
| Passage suivi | Même taille de 16 pt ; interligne 1,65 ; marges verticales du bloc 7 mm ; espace après chaque paragraphe 5 mm |
| Liste numérotée | Retrait gauche 8 mm ; aucun retrait intérieur supplémentaire des items ; espace après chaque item 3 mm |
| Numéros de liste | `font-size: 1em` ; même taille et même ligne de base que le texte |
| En-tête prénom/date | 13 pt |
| Numéro de page | 9 pt ; couleur `#555` |

Tous les mots à lire ont la même taille : rappels, grilles, expressions à lire avec l’adulte, phrases, récit et questions. Ne pas réintroduire de petits caractères pour les mots aidés ou de réduction ponctuelle pour faire tenir un mot long.

Ne pas ajouter de bordure au-dessus de chaque intertitre. Le CSS validé utilise l’espace pour séparer les rubriques. Après le récit, conserver une distinction nette entre le passage et les activités suivantes grâce à la fin du bloc de lecture, à l’espace et à l’intertitre. Un filet `---` peut être utilisé si une séparation supplémentaire est utile, sans le systématiser.

## 5. Grille de mots et lignes de guidage

La grille utilise CSS Grid sur `ul`, sans classe et sans transformation Python :

```css
ul {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  list-style: none;
  padding: 0;
  margin: 3mm 0 4mm;
  break-inside: avoid;
}
ul > li {
  margin: 0;
  padding: 3mm 2mm 3mm 0;
  border-bottom: .2mm solid #ddd;
}
ul > li:nth-last-child(-n+3) {
  border-bottom: 0;
}
```

Les lignes sous les rangées guident l’œil de gauche à droite. Garder ces séparations, mais aucune ligne sous la dernière rangée. Ne pas ajouter de traits verticaux, de cadres de cellules ou d’alternance de fonds.

La référence contient 12 items : trois colonnes et quatre rangées. Le nombre 12 n’est pas une obligation pédagogique. La règle `nth-last-child(-n+3)` fonctionne pour une grille complète dont l’effectif est un multiple de trois, par exemple 6, 9, 12 ou 15.

Pour un effectif non multiple de trois, ne pas ajouter de mots de remplissage et ne pas garder aveuglément cette règle : elle supprimerait aussi une partie du filet de l’avant-dernière rangée. Adapter la règle CSS à la dernière rangée réelle et vérifier le rendu. Une sélection générique possible est :

```css
/* Remplace la règle nth-last-child(-n+3), si les rangées incomplètes sont admises. */
ul > li:nth-child(3n+1):nth-last-child(-n+3),
ul > li:nth-child(3n+1):nth-last-child(-n+3) ~ li {
  border-bottom: 0;
}
```

Cette variante est une proposition pour de futurs contenus, pas une modification du CSS S01 validé. La tester avec les effectifs réellement utilisés. Si le nombre de colonnes change, adapter aussi la règle des bordures.

## 6. Pages et en-têtes automatiques

Format A4 portrait. Marges : 28 mm en haut, 18 mm à gauche et à droite, 16 mm en bas.

Le prénom et la date sont produits sur chaque page par les boîtes de marge CSS, respectivement `@top-left` et `@top-right`. Le numéro de page utilise `@bottom-right` et `counter(page)`. Ces informations ne doivent jamais être répétées dans le Markdown ni injectées dans son HTML par Python.

Chaque `h1` commence une nouvelle page, sauf le premier, afin d’éviter une page initiale vide. Un titre doit rester avec le contenu qui suit. Les listes de mots doivent rester ensemble tant qu’elles tiennent sur une page.

Ne pas figer le document à cinq pages : c’est seulement la longueur de S01. Adapter la validation au document produit. Si une fiche déborde, réduire le contenu non essentiel ou répartir les activités de manière explicite ; ne pas réduire arbitrairement la police.

Les en-têtes CSS de pages sont destinés au PDF et à l’impression. Leur absence dans l’affichage HTML continu à l’écran est normale. Le PDF fait foi pour la pagination.

## 7. Exemple de Markdown réutilisable

L’exemple suivant illustre la syntaxe, pas une progression pédagogique imposée :

```markdown
# Le son étudié

## Je retrouve

ma · mi · mo

## Je lis les mots

- moto
- tomate
- ami
- lama
- malade
- salade
- mari
- mardi
- samedi
- domino
- animal
- minute

Avec l’adulte : animal · minute.

## Je lis des phrases

1. Mon ami arrive samedi.
2. La moto roule.

# Le titre du récit

> Premier paragraphe du texte à lire.
>
> Deuxième paragraphe du texte à lire.

## Je raconte

Une question courte sur le texte.
```

## 8. Validation avant livraison

- Vérifier le Markdown : pas de HTML, d’identifiants, de prénom/date ni de consignes redondantes.
- Vérifier la conversion : aucun ajout de classes ou de styles selon le contenu ; aucun tableau pour les mots.
- Vérifier le PDF réel, et pas seulement l’aperçu HTML : la référence a été rendue avec WeasyPrint 69.0.
- Contrôler les en-têtes sur chaque page, l’absence de page vide et la présence de tous les items.
- Contrôler l’ordre de lecture et le nombre de colonnes de chaque grille.
- Contrôler les filets entre les rangées et leur absence sous la dernière.
- Contrôler la taille uniforme des mots, y compris hors grille, et l’alignement des numéros de liste.
- Examiner les pages les plus chargées et les mots ou groupes de mots les plus longs : aucun chevauchement ou débordement.
- Conserver les modifications CSS déjà validées par l’utilisateur ; ne pas rétablir des décorations ou conventions supprimées.

## Instruction courte à transmettre au générateur

> Produis des fiches élèves en Markdown simple et convertis-les directement en HTML/PDF avec la feuille CSS fournie. Respecte cette charte de présentation, sans copier obligatoirement le contenu S01. Utilise les listes à puces pour les grilles de mots, les listes numérotées pour les phrases et les blocs `>` pour les textes suivis. Garde tous les mots à lire en 16 pt, une police générique sans-serif, des consignes minimales et les en-têtes prénom/date générés par CSS. N’ajoute aucun HTML, ID ou classe au contenu, ni habillage spécifique dans Python. Conserve les lignes de guidage entre les rangées de mots, sans bordure sous la dernière. Adapte la longueur et les rubriques au contenu réel, puis vérifie visuellement le PDF.
