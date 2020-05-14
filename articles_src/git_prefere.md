
Mes commandes git préférées

Nathanael Charnier nous parlait des [commande qu'il utilise le plus](https://blog.nathanaelcherrier.com/2017/06/07/3-commandes-git-jutilise-le-plus/). J'ai voulu faire le même exercice.

## git status, git commit

Bien évidemment, les commandes git que j'utilise le plus sont `git status` et `git commit`. Je ne crois pas devoir expliquer pourquoi.

## git clone

J'aime utiliser des branches pour tout ce que je fais. Mais j'aime surtout avoir un `Vim` ouvert sur un bureau dans une branche et un autre Vim sur un autre bureau dans une autre branch.

Donc toute nouvelle branche se crée en deux étapes :

- cloner le projet dans un nouveau répertoire
- créer la branche dans le clone

J'ai bien entendu un script bash qui automatise cela; ça ne me coûte rien.

### Un moment d'égo : mon organisation

Au moment d'écrire ces lignes, le répertoire `mazhe` (contenant [mazhe](https://github.com/LaurentClaessens/mazhe)) contient 4 sous-répertoires

- `finite_mazhe` dans lequel je travaille sur les différences finies.
- `orga_mazhe` dans lequel je travaille sur l'introduction et l'organisation du projet.
- `gradient_mazhe` dans lequel je travaille les théorèmes sur la méthode du gradient conjugué.
- `master_mazhe` dans lequel je ne travaille pas. Je ne fais que des `pull` pour y inclure les modifications. C'est de ce répertoire que je fais les `push` pour publier après avoir lancé les tests unitaires (oui, j'ai des tests unitaires pour du code LaTeX).

Mon répertoire de [finitediff](https://github.com/LaurentClaessens/mazhe) contient également 4 sous-répertoires :

- `cppcheck_finitediff` où je cherche à résoudre tous les problèmes que [cppcheck](https://github.com/LaurentClaessens/mazhe) me signale.
- `docu_finitediff` dans lequel je travaille la documentation. Je converti les commentaires en doxygen et les relis.
- `gradient_finitediff` dans lequel je vais commencer à travailler à implémenter la méthode du gradient à pas optimal.
- `master_finitediff` dans lequel je fais des `git pull`.

### Un sale inconvénient

Cette organisation est très bien, mais pour les projets en python c'est compliqué. Lorsque je lance les tests unitaires dans un répertoire je veux évidemment tester la version *du répertoire courrant*. Donc lorsque le script de test fait un `import` c'est compliqué de lui faire comprendre d'où il doit importer.

Pour [phystricks](https://github.com/LaurentClaessens/mazhe), mon répertoire `phystricks` contient par exemple le sous-répertoire `foo_phystricks`, qui contient seulement un sous-sous-répertoire `physrticks` (donc `phystricks/foo_phystricks/phystrick`). Le script `testing.sh` ajoute essentiellement `pwd/..` à `$PYTHONPATH` avant de lancer `unit_tests.py` (c'est pire que ça parce que le répertoire de tests est encore un sous-répertoire et que ce n'est pas `$PYTHONPATH`, mais `$SAGE_PATH`, mais vous voyez l'idée).

## git stash

J'estime que les tests unitaires doivent également vérifier que tous les fichiers nécessaires à la compilation et au fonctionnement sont effectivement suivis par git. Donc je lance les tests unitaires dans un nouveau clone du répertoire à tester.

Mais je veux tester les dernière modifications, même celles pour lesquelles il n'y a pas encore de commit.

J'utilise donc `git stash` pour appliquer les modifications non commitées au clone dans lequel les tests vont être lancées.

J'avoue n'être pas très satisfait/convaincu du niveau de propreté [de ce système](https://github.com/LaurentClaessens/mazhe/blob/master/testing/testing.sh).

## Le perdant : git checkout

Je n'utilise pratiquement jamais `git checkout` parce que je change de branche soit avec un `cd` soit en changeant de bureau.

## Mais pas à la main

J'utilise donc énormément `stash` et `clone`, mais uniquement via des scripts. C'est assez rare que je tape moi-même ces commandes.
