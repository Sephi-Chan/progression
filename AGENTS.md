# AGENTS.md — Génération de dossiers de compétences CE1

## Mission

Ce dépôt sert à produire des dossiers pédagogiques structurés pour des compétences de CE1.

Quand l'utilisateur demande de travailler une ou plusieurs compétences (par exemple `COMP1`, `NUM1`, `CONJ1`), générer **un fichier Markdown autonome par compétence**, rangé dans une arborescence déterminée à partir de `progression.xlsx`.

Le livrable doit être directement exploitable par un enseignant de CE1 : didactiquement justifié, explicite, progressif, objectivable, facilement déclinable et suffisamment standardisé pour que les différentes compétences aient une structure comparable.

Le travail porte sur une compétence précise. Ne pas transformer le document en séquence longue, en fiche de préparation exhaustive ou en chapitre de manuel.

---

## 1. Sources obligatoires

### 1.1. Hiérarchie des sources didactiques

Utiliser uniquement des sources institutionnelles ou de recherche reconnues, dans cet ordre de priorité :

1. **Programmes officiels français actuellement en vigueur**, en particulier le Bulletin officiel et les textes du ministère.
2. **Éduscol** et guides ministériels.
3. **Ressources institutionnelles des académies, DSDEN et circonscriptions**.
4. **Organismes de recherche reconnus en didactique ou en sciences de l'éducation**, par exemple le Centre Alain-Savary / IFÉ, seulement lorsque les trois niveaux précédents ne suffisent pas ou lorsqu'un éclairage de recherche est utile.

À la date de rédaction de ce fichier, le programme de référence pour le français et les mathématiques au cycle 2 est celui publié au BO n° 41 du 31 octobre 2024, applicable depuis la rentrée 2025. **Toujours vérifier qu'il n'a pas été remplacé ou modifié avant de l'utiliser.**

Ne jamais utiliser comme autorité didactique :
- blogs enseignants ;
- sites commerciaux ;
- fiches de méthodes éditoriales ;
- sites de soutien scolaire ;
- forums ;
- contenus générés par IA ;
- Wikipédia ou autres encyclopédies collaboratives ;
- ressources dont l'origine institutionnelle n'est pas identifiable.

Si une source secondaire contredit une source de niveau supérieur, retenir la source de niveau supérieur et signaler brièvement le conflit seulement s'il affecte réellement la conception du dossier.

### 1.2. Recherche en ligne

Pour chaque compétence :
- vérifier le programme en vigueur ;
- rechercher les ressources Éduscol directement pertinentes ;
- compléter si nécessaire par une ressource académique/circonscription ;
- ne mobiliser une source de recherche que si elle apporte une justification utile.

Ne jamais fonder le positionnement dans les programmes sur la mémoire du modèle si les sources officielles peuvent être consultées.

Si l'accès aux sources officielles en ligne est impossible et qu'aucune copie locale suffisante n'est disponible, **ne pas inventer le cadrage institutionnel**. Signaler clairement le blocage au lieu de produire de fausses références.

### 1.3. Citations dans les fichiers produits

Chaque fichier de compétence doit terminer par une section `## Sources`.

Pour chaque source réellement utilisée, donner :
- niveau de source : `Programme`, `Éduscol`, `Académie/Circonscription`, `Recherche`, ou `Source du texte littéraire` ;
- titre exact ;
- organisme ;
- date si disponible ;
- URL exacte ;
- partie ou page pertinente lorsque c'est possible.

Les affirmations importantes concernant les attendus, la progressivité ou les démarches recommandées doivent être rattachables à une source listée.

Ne pas multiplier les références décoratives : conserver les sources qui ont réellement influencé la conception.

---

## 2. Cas particulier des textes de lecture-compréhension

Pour les compétences de compréhension, et plus largement lorsqu'un texte sert de support, **préférer un extrait d'une œuvre réelle de littérature de jeunesse à un texte inventé**, à condition que l'extrait soit adapté au CE1 et juridiquement réutilisable.

Ordre de préférence pour le corpus :
1. texte ou extrait reproduit dans une ressource institutionnelle ;
2. œuvre du domaine public accessible par une institution patrimoniale, notamment la BnF/Gallica ;
3. texte fourni directement par l'utilisateur ;
4. texte créé pour l'exercice, uniquement si aucune solution précédente n'est satisfaisante.

La source du texte littéraire n'est pas une source didactique : la distinguer explicitement des références servant à justifier l'enseignement.

Pour chaque extrait réel, indiquer immédiatement :
- auteur ;
- titre ;
- éventuellement chapitre/conte/édition ;
- source de consultation.

Ne pas reproduire de longs passages d'une œuvre contemporaine protégée. Dans ce cas, préférer une œuvre du domaine public, un texte fourni par l'utilisateur ou un texte créé et clairement étiqueté `Texte créé pour l'exercice`.

Ne jamais présenter comme citation exacte un texte adapté, modernisé, abrégé ou reformulé. Employer alors une mention explicite telle que `Adapté de ...`.

---

## 3. Source de vérité pour la progression

Le fichier `progression.xlsx` est la source de vérité pour :
- le code de compétence ;
- l'intitulé exact ;
- la discipline ;
- le sous-domaine ;
- la position relative de la compétence dans son sous-domaine.

### 3.1. Lecture de la progression

Avant de produire un dossier :
1. localiser `progression.xlsx` ;
2. lire l'onglet contenant les compétences ;
3. retrouver la ligne exacte correspondant au code demandé ;
4. conserver **mot pour mot** l'intitulé du fichier ;
5. identifier les compétences immédiatement précédentes et suivantes **dans le même sous-domaine**.

Ne jamais déduire un calendrier annuel précis à partir du simple numéro de ligne du tableur.

La progression étant organisée par domaines, la ligne globale du tableur ne signifie pas qu'une compétence de français est enseignée avant ou après une compétence de mathématiques.

En revanche, l'ordre des compétences d'un même sous-domaine sert à comprendre la logique locale de progression, sauf indication contraire dans une autre source fournie par l'utilisateur.

### 3.2. Positionnement dans la progression

Le dossier doit expliquer en quelques phrases :
- ce que cette compétence installe ;
- ce que l'élève est supposé déjà pouvoir mobiliser ;
- quelles compétences ultérieures du même sous-domaine elle prépare ;
- surtout, ce qu'il **ne faut pas anticiper** pour ne pas brouiller l'évaluation.

Exemple de principe : si une compétence demande de trouver l'infinitif d'un verbe et qu'une autre compétence ultérieure porte sur le repérage du verbe conjugué, le verbe peut être signalé dans les premiers exercices afin de ne pas évaluer les deux compétences à la fois.

### 3.3. Atomicité

Concevoir les tâches pour qu'elles évaluent principalement la compétence demandée.

Éviter qu'une difficulté secondaire non ciblée devienne le véritable obstacle :
- lecture lexicale inutilement difficile ;
- écriture longue lorsque la compétence n'est pas l'écriture ;
- calcul annexe ;
- consigne complexe ;
- vocabulaire rare ;
- représentation graphique non enseignée ;
- connaissance correspondant à une compétence ultérieure.

Quand une compétence secondaire est nécessaire, la neutraliser autant que possible.

---

## 4. Arborescence et noms de fichiers

Créer les fichiers sous :

```text
competences/
  <discipline-slug>/
    <sous-domaine-slug>/
      <CODE>.md
```

Utiliser des slugs ASCII en minuscules, avec des tirets pour les espaces.

Exemples :

```text
competences/francais/comprehension/COMP1.md
competences/francais/conjugaison/CONJ1.md
competences/francais/ecriture/ECR1.md
competences/francais/grammaire/GRAM1.md
competences/maths/geometrie/GEOM1.md
competences/maths/grandeurs-et-mesures/GM1.md
competences/maths/numeration/NUM1.md
```

Le code du fichier reste en majuscules.

Ne pas créer une arborescence parallèle codée en dur : la discipline et le sous-domaine doivent être lus dans `progression.xlsx`, puis transformés en slugs.

Si le fichier existe déjà et que l'utilisateur demande explicitement de retravailler cette compétence, le mettre à jour en conservant le même chemin.

---

## 5. Format obligatoire d'un fichier de compétence

Chaque fichier doit respecter cette structure générale.

### 5.1. Métadonnées

Commencer par un front matter YAML :

```yaml
---
code: COMP1
niveau: CE1
discipline: Français
sous_domaine: Compréhension
intitule: "Trouver une information écrite clairement dans un texte"
---
```

Reprendre les valeurs exactes de `progression.xlsx`.

### 5.2. Titre

```markdown
# COMP1 – Trouver une information écrite clairement dans un texte
```

### 5.3. Cadrage de la compétence

Section :

```markdown
## Cadrage
```

En quelques paragraphes courts :
- reformuler précisément ce que l'élève doit apprendre à faire ;
- situer la compétence dans le programme officiel ;
- préciser son positionnement dans la progression fournie ;
- indiquer les limites choisies à ce stade ;
- mentionner brièvement les prérequis utiles ;
- signaler les compétences voisines qu'il faut éviter d'évaluer prématurément.

Le cadrage doit rester opérationnel : environ 150 à 300 mots sauf nécessité particulière.

### 5.4. Objectif et critères de réussite

Section :

```markdown
## Objectif et critères de réussite
```

Donner :
- `Objectif élève` : formulation courte et compréhensible ;
- `Critères de réussite` : 2 à 4 critères observables.

Les critères doivent permettre de corriger ou d'évaluer sans interprétation vague.

Ne pas inventer de seuil global de maîtrise (`4/5 = acquis`, etc.) sauf demande explicite de l'utilisateur.

### 5.5. Leçon explicite courte

Section :

```markdown
## Leçon explicite — 10 à 15 min
```

Donner un déroulé réaliste de **10 à 15 minutes maximum**, avec temps indicatifs.

Structure recommandée :
1. annonce de l'objectif et activation très courte ;
2. explication explicite de la procédure ou du concept ;
3. modelage ;
4. pratique guidée très brève ;
5. verbalisation finale de ce qu'il faut retenir.

La somme des temps annoncés ne doit jamais dépasser 15 minutes.

Inclure :
- matériel nécessaire ;
- vocabulaire à employer ;
- gestes professionnels ou formulations utiles ;
- erreurs typiques à anticiper.

Ne pas transformer cette section en fiche de préparation administrative.

### 5.6. Mémo élève

Section :

```markdown
### À retenir
```

Produire une trace orale/écrite très courte, de 2 à 5 lignes maximum, qui peut servir de formulation de référence.

Elle doit être compréhensible par un élève de CE1 et cohérente avec la procédure réellement enseignée.

### 5.7. Exercice type

Section :

```markdown
## Exercice type
```

Décrire **un seul format d'exercice principal**, destiné à être décliné de nombreuses fois.

Préciser :
- consigne stable ;
- support ;
- type de réponse attendu ;
- nombre d'items conseillé ;
- variables que l'on peut modifier ;
- variables qui doivent rester fixes au début ;
- difficultés parasites à éviter.

Ajouter une sous-section :

```markdown
### Pourquoi cet exercice est pertinent
```

Justifier brièvement :
- son alignement avec la compétence ;
- son objectivabilité ;
- sa facilité de déclinaison ;
- la manière dont il isole la compétence ciblée ;
- sa compatibilité avec le modelage, l'entraînement, le devoir et l'évaluation.

---

## 6. Modelage et pratique immédiate

### 6.1. Modelage explicite : 3 items

Section :

```markdown
## Modelage explicite — 3 items
```

Créer exactement **3 items** du même exercice type.

Le modelage doit montrer le raisonnement à enseigner, et non simplement donner les réponses.

Pour chaque item, fournir :
- l'énoncé ;
- ce que l'enseignant attire d'abord dans l'attention ;
- une verbalisation possible du raisonnement ;
- la réponse ;
- le contrôle final.

Faire décroître progressivement l'aide :
- **Item 1 : modelage complet** par l'enseignant ;
- **Item 2 : modelage interactif**, avec questions aux élèves ;
- **Item 3 : guidage allégé**, en laissant davantage de décisions aux élèves.

Employer une verbalisation simple, répétable et compatible avec le langage d'un CE1.

### 6.2. Pratique immédiate : 7 items

Section :

```markdown
## À toi de jouer — 7 items
```

Créer exactement **7 items supplémentaires** à donner juste après la leçon.

Ils utilisent le même format et restent accessibles. Ils ne doivent introduire aucune nouvelle difficulté majeure.

Ne pas placer les réponses sous les items.

La correction correspondante est placée dans la section générale `Corrections`.

---

## 7. Séries d'entraînement

Section :

```markdown
## Entraînements
```

Créer exactement **10 séries**, nommées :

```text
ENT01
ENT02
...
ENT10
```

### 7.1. Nombre d'items

Chaque série contient **5 à 10 items**, en fonction du temps réel nécessaire pour réaliser un item.

Règle pratique :
- réponse très courte, repérage, choix, calcul ou transformation simple : 8 à 10 items ;
- production courte ou traitement intermédiaire : 6 à 8 items ;
- lecture substantielle, phrase complète, manipulation, mesure, tracé ou tâche visuelle plus lente : 5 à 6 items.

Ne jamais augmenter artificiellement le nombre d'items pour atteindre 10.

### 7.2. Progressivité

Les 10 séries doivent constituer une progression **à l'intérieur de la même compétence** :

- `ENT01` à `ENT03` : accessibles ;
- `ENT04` à `ENT07` : niveau standard ;
- `ENT08` à `ENT10` : plus résistants.

La difficulté peut augmenter par des **variables didactiques pertinentes** :
- nombres plus grands ;
- distracteurs plus proches ;
- ordre moins canonique ;
- distance accrue entre les éléments à relier ;
- support légèrement moins guidé ;
- formulation moins transparente ;
- davantage d'informations inutiles ;
- changement de position dans la phrase ;
- etc.

Mais ne jamais transformer la difficulté en compétence nouvelle.

Exemple de mauvaise progressivité : passer d'un repérage explicite dans un texte à une inférence alors que l'inférence correspond à une compétence distincte de la progression.

### 7.3. Stabilité de la consigne

La consigne et le format doivent varier le moins possible.

L'objectif est que l'élève puisse consacrer ses ressources cognitives au savoir-faire travaillé plutôt qu'à la compréhension d'une nouvelle tâche.

---

## 8. Séries d'évaluation

Section :

```markdown
## Évaluations
```

Créer exactement **10 formes d'évaluation**, nommées :

```text
EVAL01
EVAL02
...
EVAL10
```

Chaque évaluation contient exactement **5 items**.

### 8.1. Évaluations parallèles

Les dix évaluations doivent avoir une difficulté globale comparable.

Elles ne constituent **pas** une progression de facile à difficile.

Chaque forme doit échantillonner des difficultés représentatives de la compétence et rester comparable aux autres formes.

Ne pas introduire en évaluation une difficulté qui n'a pas été travaillée.

### 8.2. Réutilisation des entraînements

Chaque évaluation doit contenir :
- **au moins 3 items sur 5 directement repris ou très légèrement transposés des entraînements** ;
- **au moins 1 item nouveau mais strictement isomorphe** aux exercices entraînés ;
- au maximum 4 items sur 5 reproduits à l'identique.

Le but est de conserver une forte familiarité avec la tâche tout en vérifiant que l'élève ne réussit pas uniquement par reconnaissance d'un item mémorisé.

Un item `très légèrement transposé` conserve exactement la même structure cognitive et ne change qu'une donnée superficielle.

### 8.3. Correction

Pour les questions fermées, donner la réponse exacte.

Pour les productions ouvertes, donner :
- un exemple de réponse attendue ;
- les critères permettant d'accepter d'autres formulations correctes.

---

## 9. Séries de devoirs

Section :

```markdown
## Devoirs
```

Créer exactement **10 séries**, nommées :

```text
DEV01
DEV02
...
DEV10
```

Chaque devoir contient exactement **5 items**.

Les devoirs doivent être **accessibles** et reposer uniquement sur des formats déjà rencontrés en classe.

Règles :
- aucune nouvelle procédure ;
- aucune nouvelle représentation ;
- aucune difficulté plus élevée que les premiers entraînements ;
- vocabulaire simple ;
- consigne connue ;
- possibilité de réaliser la tâche sans aide spécialisée d'un adulte ;
- pas de matériel particulier à domicile, sauf si ce matériel est explicitement fourni avec le devoir.

Privilégier des items repris ou très proches de `ENT01` à `ENT04`.

Le devoir sert à consolider, pas à découvrir ni à piéger.

---

## 10. Corrections séparées

Après toutes les séries destinées aux élèves, créer :

```markdown
## Corrections
```

Puis les sous-sections :
- `### Correction — À toi de jouer`
- `### Corrections des entraînements`
- `### Corrections des évaluations`
- `### Corrections des devoirs`

Les corrections des séries doivent reprendre les identifiants des séries et les numéros d'items.

Exemple :

```markdown
#### ENT03
1. ...
2. ...
```

Ne jamais insérer la correction directement sous une série élève, sauf dans la section de modelage où la verbalisation de la réponse fait partie de l'enseignement.

---

## 11. Traçabilité des items

Terminer la partie pédagogique par :

```markdown
## Traçabilité des évaluations et devoirs
```

Créer deux tableaux réservés à l'enseignant.

### 11.1. Évaluations

Pour chaque item de chaque évaluation, indiquer son origine :

```text
EVAL01-1 -> ENT02-4
EVAL01-2 -> ENT05-2, transposé
EVAL01-3 -> nouveau isomorphe de ENT04
...
```

Cette table permet de vérifier que la règle de réutilisation est réellement respectée.

### 11.2. Devoirs

Indiquer de la même manière l'origine de chaque item de devoir.

Cette traçabilité est importante : ne pas se contenter d'affirmer que des items ont été repris.

---

## 12. Identifiants des items

Utiliser systématiquement des identifiants uniques dans le document :

- `MOD01`, `MOD02`, `MOD03`
- `IMM01` à `IMM07`
- `ENT01-01`, `ENT01-02`, etc.
- `EVAL01-01`, etc.
- `DEV01-01`, etc.

Les identifiants servent à la traçabilité et à la réutilisation.

Ils peuvent être placés discrètement au début de l'item.

---

## 13. Supports visuels et matériel

Certaines compétences ne peuvent pas être correctement exercées avec du texte seul : plans, longueurs, figures, tableaux, collections, horloges, monnaie, etc.

Dans ce cas :
- le support doit être suffisamment décrit pour être réellement exploitable ;
- toutes les données nécessaires doivent être présentes ;
- ne pas écrire des consignes du type `regarde le plan ci-dessous` sans fournir le plan.

Par défaut, lorsque le support peut être représenté simplement :
- utiliser un tableau Markdown, un bloc monospace ou un **SVG embarqué directement dans le Markdown** ;
- éviter les images externes fragiles ;
- ne créer des fichiers d'assets séparés que si l'utilisateur le demande.

Pour un SVG ou une figure :
- conserver des dimensions lisibles ;
- ne pas dépendre d'une couleur seule pour distinguer des éléments ;
- ajouter des lettres, symboles ou motifs si nécessaire ;
- vérifier que la réponse ne dépend pas d'un défaut de rendu.

Pour les grandeurs et mesures, respecter le niveau de la compétence : si l'objectif est de comparer sans mesurer, ne pas fournir involontairement une graduation ou une donnée numérique qui transforme la tâche en mesure.

---

## 14. Qualité des items

Chaque item doit être :
- grammaticalement correct ;
- adapté au niveau CE1 ;
- non ambigu ;
- résoluble avec les informations données ;
- centré sur une seule difficulté principale ;
- corrigible de manière stable.

Éviter :
- les pièges gratuits ;
- les formulations inutilement négatives ;
- les ambiguïtés lexicales ;
- les connaissances culturelles indispensables à la réussite ;
- les nombres ou textes inutilement longs ;
- les cas particuliers non enseignés ;
- les distracteurs absurdes qui rendent la réponse évidente sans mobiliser la compétence.

### 14.1. Pour les compétences de langue

Contrôler notamment :
- vocabulaire connu ou transparent ;
- syntaxe des phrases ;
- accord des formes utilisées ;
- absence de cas exceptionnels non enseignés ;
- distinction entre la compétence ciblée et les compétences de repérage grammatical voisines.

### 14.2. Pour la compréhension

Distinguer strictement :
- information explicitement écrite ;
- reprise pronominale ;
- inférence ;
- interprétation ;
- compréhension lexicale.

Ne pas faire glisser une série vers une compétence de compréhension ultérieure.

### 14.3. Pour les mathématiques

Respecter une progression du concret vers la représentation puis, lorsque pertinent, vers l'abstrait.

Le matériel ou le dessin doit soutenir la notion sans fournir directement la réponse.

Éviter de mobiliser une convention mathématique que l'élève n'est pas encore supposé connaître.

---

## 15. Variables didactiques

Dans le dossier, ajouter avant les entraînements une courte section :

```markdown
## Variables didactiques
```

Donner :
- 3 à 6 variables permettant de rendre l'exercice plus facile ;
- 3 à 6 variables permettant de le rendre plus résistant ;
- les variables interdites à ce stade parce qu'elles feraient basculer vers une autre compétence.

Cette section doit guider la construction des 10 séries et rendre explicite la logique de progressivité.

---

## 16. Style rédactionnel

Écrire en français.

Pour les parties destinées à l'enseignant :
- style précis, direct et professionnel ;
- phrases courtes ;
- vocabulaire didactique lorsqu'il apporte une vraie précision.

Pour les consignes élèves :
- formulation courte ;
- syntaxe simple ;
- même formulation autant que possible d'une série à l'autre.

Pour les verbalisations de modelage :
- utiliser des formulations que l'enseignant peut réellement dire à voix haute ;
- éviter le jargon théorique ;
- rendre visible la prise d'information, la décision, l'action et la vérification.

Ne pas surcharger les documents d'emojis, d'encadrés décoratifs ou de commentaires génériques.

---

## 17. Ce qu'il ne faut pas faire

Ne pas :
- créer plusieurs exercices-types concurrents sans nécessité ;
- modifier l'intitulé de la compétence provenant du tableur ;
- anticiper volontairement une compétence ultérieure pour « enrichir » l'exercice ;
- rendre les dernières évaluations plus difficiles que les premières ;
- fabriquer un texte littéraire en laissant croire qu'il provient d'un auteur ;
- inventer une citation institutionnelle ;
- citer une source qui n'a pas été consultée ;
- transformer les devoirs en nouvelles leçons ;
- mettre les réponses juste après les exercices élèves ;
- produire des séries dont les corrections ne correspondent pas exactement aux items ;
- laisser une consigne dépendre d'une image ou d'un matériel absent ;
- considérer qu'une réponse ouverte n'a qu'une formulation possible lorsqu'il en existe plusieurs.

---

## 18. Procédure de travail pour chaque compétence

Suivre cet ordre :

1. Lire `progression.xlsx`.
2. Identifier exactement la compétence demandée.
3. Examiner les compétences voisines du même sous-domaine.
4. Rechercher les sources institutionnelles actuelles.
5. Définir précisément le périmètre de la compétence.
6. Choisir un exercice type stable.
7. Définir ses variables didactiques.
8. Construire la leçon de 10 à 15 minutes.
9. Proposer une trace écrite qui n'excède pas 5 phrases.
10. Construire les 3 items de modelage. Explicite les pocédures.
11. Construire les 7 items de pratique immédiate.
12. Construire `ENT01` à `ENT10`.
13. Construire `EVAL01` à `EVAL10` en réutilisant réellement les entraînements.
14. Construire `DEV01` à `DEV10` à partir des formes les plus accessibles.
15. Construire toutes les corrections.
16. Construire les tableaux de traçabilité.
17. Ajouter les sources.
18. Exécuter la checklist de validation.
19. Écrire le fichier au chemin prévu.

Lorsque plusieurs compétences sont demandées, effectuer cette procédure pour chacune d'elles et produire un fichier distinct.

---

## 19. Checklist de validation obligatoire

Avant de considérer un fichier terminé, vérifier silencieusement chacun des points suivants.

### Sources
- [ ] Le programme actuellement en vigueur a été vérifié.
- [ ] Les références didactiques respectent la hiérarchie imposée.
- [ ] Aucune source commerciale ou blog n'est utilisée.
- [ ] Toute œuvre littéraire reproduite est correctement identifiée.
- [ ] Aucun passage protégé substantiel n'est reproduit sans justification.

### Progression
- [ ] Code, discipline, sous-domaine et intitulé correspondent exactement à `progression.xlsx`.
- [ ] Le positionnement dans le sous-domaine est explicité.
- [ ] Les compétences ultérieures ne sont pas évaluées par accident.

### Leçon
- [ ] La durée totale annoncée est comprise entre 10 et 15 minutes.
- [ ] L'objectif est observable.
- [ ] Les critères de réussite sont explicites.
- [ ] Le mémo élève tient en 2 à 5 lignes.

### Exercice type
- [ ] Un seul format principal est retenu.
- [ ] Il cible réellement la compétence.
- [ ] Les variables didactiques sont explicites.
- [ ] Le support nécessaire est fourni.

### Quantités
- [ ] 3 items de modelage.
- [ ] 7 items de pratique immédiate.
- [ ] 10 séries d'entraînement.
- [ ] Chaque entraînement contient 5 à 10 items.
- [ ] 10 évaluations de 5 items exactement.
- [ ] 10 devoirs de 5 items exactement.

### Progressivité et évaluation
- [ ] Les entraînements vont de l'accessible au résistant sans changer de compétence.
- [ ] Les 10 évaluations sont de difficulté comparable.
- [ ] Chaque évaluation réutilise au moins 3 items entraînés.
- [ ] Chaque évaluation contient au moins 1 item nouveau isomorphe.
- [ ] Aucun item d'évaluation n'est plus difficile que ce qui a été entraîné.
- [ ] Les devoirs n'introduisent aucune nouveauté.

### Corrections
- [ ] Chaque item a une correction.
- [ ] Les corrections sont séparées des exercices élèves.
- [ ] Les réponses ouvertes ont des critères d'acceptation.
- [ ] Les numéros d'items correspondent exactement.
- [ ] Les tableaux de traçabilité sont complets et exacts.

### Fichier
- [ ] Le chemin respecte l'arborescence.
- [ ] Le front matter est valide.
- [ ] Le Markdown est lisible.
- [ ] Aucun lien ou support essentiel n'est cassé.

Si un point échoue, corriger le document avant de terminer.

---

## 20. Compte rendu à l'utilisateur

Après génération, répondre brièvement en donnant :
- la liste des compétences produites ;
- les chemins des fichiers créés ou modifiés ;
- les éventuels arbitrages didactiques importants ;
- toute limite de source rencontrée.

Ne pas recopier dans le message final l'intégralité des fichiers générés sauf demande explicite.

---

## 21. Priorité en cas de conflit

Ordre de priorité :
1. demande explicite de l'utilisateur pour la tâche en cours ;
2. programme officiel en vigueur ;
3. présent `AGENTS.md` ;
4. progression locale pour l'ordre et le découpage des compétences ;
5. ressources d'accompagnement.

Ne jamais modifier silencieusement la progression pour la rendre plus conforme à une préférence personnelle.

Si l'intitulé local et le programme officiel ne se superposent pas parfaitement, conserver l'intitulé local, expliquer le rapprochement dans le cadrage et concevoir les exercices dans le périmètre le plus cohérent avec les deux.
