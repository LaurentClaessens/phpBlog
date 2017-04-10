
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

* Dans un répertoire à part, créer autant de fichiers `odt` qu'il y a de pages à remplir. Un seul fichier par «type» de page.
* Remplir ces fichiers avec OpenOffice.
* Remplacer les noms des concours par un tag facilement reconnaissable. Par exemple «FOOBARR-110142».
* Ces fichiers sont des fichiers «génériques».

Et là, on écrit un script en python qui, pour chaque dossier à remplir, fait une copie du fichier générique, le modifie en remplaçant «FOOBAR-110142» par le numéro du concours, et copie le résultat dans le répertoire du concours.

À ce moment, il suffit de recharger le fichier maître pour que tout soit en ordre. Lui, ne se rend pas compte qu'on a modifié ses fichiers inclus derrière le dos. D'ailleurs il est fait pour cela.


## Conclusion

J'avais déjà écrit des scripts en python pour générer du code python, html, php, c++ et latex. À partir d'aujourd'hui j'ajoute odt à la liste des types de fichiers pour lesquels j'ai écrit des morceaux en python.
