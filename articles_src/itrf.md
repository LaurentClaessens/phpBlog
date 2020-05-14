
## Le problème

Pour participer aux concours ITRF, il faut remplir plusieurs dossiers, dont l'administration fournit des fichiers  `docx`.

* Chaque fichier contient une dizaine de pages : «diplômes», «expériences», «réalisations», etc.
* Tous ne contiennent pas exactement les mêmes choses.
* Les pages «identiques» d'un dossier à l'autre ne sont pas identiques : elles diffèrent de l'en-tête qui donne le nom du corps auquel le dossirt postule et d'une case dans laquelle est donné le numéro du concours.

Remplir fichier par fichier dans OpenOffice créerait une énorme duplication de code parce que le texte «diplômes» devrait être écrit autant de fois qu'il y a des dossiers à remplir. 

## Première chose à faire

Râler parce que si ils avaient fournit les squelettes de dossiers sous forme de document `tex`, ce serait facile.

## Début de solution

### Mise en place

* Conversion de tous les `docx`  en `odt`.
* Créer un répertoire par fichier.
* Diviser le `odt` en un fichier par page
* Créer un document maître qui les inclut tous. Donc un document maître par poste ITRF que l'on convoite.

### Manipulation de base

Il est facile de changer un mot dans un fichier `odt` 

* Décompresser avec
```bash
unzip mon_fichier.odt 
```
* Modifier le mot dans le fichier `content.xml`
* Recompresser avec
```bash
zip -r mon_fichier.odt *
```

Ceci peut être automatisé en python.

### Production des dossiers

* Dans un répertoire à part, créer un fichier `total.odt` qui contient toutes les pages à modifier du dossier. C'est à dire pas les deux pages de garde ni la page de présentation.
* Remplir ce fichiers avec OpenOffice.
* Remplacer les champs par des tags : `PYNOM`, `PYPRENOM`, `PYNUMERO` (pour le numéro du concours) et `PYCONCOURS` pour le nom du concours (ce qui arrive dans le haut de page).
* Les pages doivent être numérotées de force de façon à ce que la chaîne `style:page-number="624"` apparaisse dans le fichier `content.xml`. Cela servira à modifier le numéro des pages. Parce que évidemment d'un dossier à l'autre, le numéro de la page où «Services publics» arrive n'est pas la même.

Et là, on écrit un script en python qui, pour chaque dossier à remplir, fait une copie du fichier `total.odt`, le modifie en remplaçant les tags `PYmachin` par les valeurs correctes.

## Ce que j'ai appris

* On peut changer les numéros de pages dans LibreOffice en cliquant entre deux pages.
* On peut convertir un document `odt` en `pdf` en ligne de commande. Mais il semblerait que ce ne soit pas possible avec un document maître. Voici la commande :
```bash
office --convert-to pdf total.odt --headless
```
Attention : il faut fermer toutes les instances de LibreOffice, sinon cette commande ne fait rien.

## Conclusion

* Après des semaines de C++ intensif, ça fait du bien de taper un peu de Python. C'est un langage qui ne vous emm pas.
* OpenOffice c'est vraiment de la m. Une force de LaTeX contre OOo, c'est que le code LaTeX est du texte brut facilement modifiable via un script en python. Le couple LaTeX-Python est vraiment fort pour la génération automatique de documents.
* J'ai écrit dans la vie des scripts en python pour générer du code python, html, php, C++, latex et odt. 
