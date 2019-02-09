## Conseils pour écrire un livre collaboratif

Je pose ici quelque conseils, issus de mon expérience d'écriture du Frido.

### Git de votre côté

Soyez sûr d'être capables d'utiliser
- `git commit`
- `git pull`
- `git push`
- `git clone`
- `git merge`
- `git diff`
Vous allez devoir faire des branches et être capables de lire correctement un diff.

Si vous aimez Vim, voici mon `.gitconfig` :
```
[user]
	name = Votre nom ici
	email = votre addresse
[push]
	default = simple
[core]
	editor = vim
    quotepath = false
[difftool]
	prompt = false
[diff]
    external = git_diff_wrapper.sh
[pager]
    diff =
```
où le script `git_diff_wrapper.sh` est
```
#!/bin/sh
vimdiff "$2" "$5"
```

### Git côté serveur

Publiez votre code LaTeX sur un site type "github" ... ou plus libre si le coeur vous en dit.

### La publicité

J'avais déjà eu quelque retours avec *aucune* publicité nulle part. Sans doute que le nombre de documents indexés par Google pour les mots-clefs «décomposition polaire opérateur» n'est pas très grand.

Ensuite, un article par an sur linuxfr est amplement suffisant.

### Licence

Mettez-en directement une qui permet l'utilisation commerciale. La raison est que :
- dès que vous aurez des patch de contributeurs tiers, il ne sera plus possible de changer la licence
- vous avez envie de vendre le livre sur un site d'impression à la demande comme [lulu](lulu.com) ou [thebookedition](https://thebookedition.com). Sinon le livre ne sera pas autorisé à l'agrégation.

Comme vous mettez une licence qui permet l'utilisation commerciale, mettez-en une qui a une clause héréditaire forte. Exemple : la FDL. 

### Informatique

- Nommez vos fichiers en préfixant par un nombre :
    * `001_espaces_vectoriels.tex`
    * `002_espaces_vectoriels.tex`
    * `003_analyse_reelle.tex`
    * `004_espacesDeBanach.tex`
- Organisez vos sources : un fichier principal dans le répertoire principal, et les fichiers `tex` dans un sous-répertoire.
- Utilisez `ack` ou `ag`, pas `grep`.
