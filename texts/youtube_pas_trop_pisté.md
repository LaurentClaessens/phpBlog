## Je suis un parasite de youtube

Je profite des vidéos, je ne paye rien [mais je rends la pareille](https://laurent.claessens-donadello.eu/frido.html) aux créateurs qui mettent de la connaissance en ligne, j'ai un bloqueur de pub, et je télécharge les vidéos plutpôt que les regarder en ligne pour ne pas être pisté et ne pas subir les recommandations.

Bref, si tout le monde faisait comme moi, on diviserait pas 10 le nombre de vidéos de qualité et par 1000 le nombre de vidéos de mauvaise qualité. Je précise que je n'ai rien contre les scientifiques qui font des vidéos sur leur sujet et dont j'ai du mal à croire qu'une partie n'est pas faite sur leur temps de travail. Pour moi une personne payée par une université a parfaitement le droit de faire des vidéos de vulgarisation sur son temps de travail (je pense à [dr Becky](https://www.youtube.com/@DrBecky) et probablement un certain nombre de vidéos de [numberphile](https://www.youtube.com/@numberphile)).


## Sans s'abonner

Pour ne manquer aucune vidéo d'une chaîne, le mieux est de s'abonner à son flux RSS. L'url du rss est :
```
https://www.youtube.com/feeds/videos.xml?channel_id=<id de la chaine>
```
Pour trouver l'identifiant de la chaine:

- Aller sur la page de la chaine : `https://www.youtube.com/@ChatSceptique`
- Cliquer sur la description : `On fait quoi quand on est un chat mignon et qu'on a ...`
- Dans le panneau qui arrive, cliquer en bas sur "Partager la chaine".
- Demander de "Copier l'ID de la chaine".

Au final, l'adresse du flux est :

``` 
https://www.youtube.com/feeds/videos.xml?channel_id=UCOuIgj0CYCXCvjWywjDbauw
```
## Télécharger une vidéo


Maintenant c'est chaud. On va tenter de regarder la vidéo `https://www.youtube.com/watch?v=gKgH60hFoRU` en étant le moins pisté possible par Google.

### La base

Installer [yt-dlp](https://github.com/yt-dlp/yt-dlp) et télécharger. Avec ça on n'a pas les pubs et je ne vois pas très bien comment Google pourrait sa faire un dossier sur moi.


### La difficulté

Depuis quelque jours, il est impossible de télécharger une vidéo sans être connecté. Le script `yt-dlp` a besoin d'avoir un cookie de connexion.

Évidemment, on peut se créer un compte google, se connecter dans Firefox et faire ceci :
```
 ./yt-dlp  --cookies-from-browser firefox   "https://www.youtube.com/watch?v=8g28saKDM-E"
```
Ça marche, mais 

- ça donne à Google l'information comme quoi je regarde telle ou telle vidéo.
- ça me demande d'être connecté et donc potentiellement pisté.


### Ma solution

Ma solution est surement loin d'être parfaite, mais si vous avez une meilleur idée, n'hésitez pas.


1. Je me suis souvenu que j'ai un compte gmail jamais utilisé, créé du temps où on ne devait pas donner de numéro de téléphone pour créer un compte. 
2. Sinon, je crois qu'on peut créer un compte youtube à partir d'une addresse mail non google.
3. Bref, ayez un compte youtube qui servira juste à ça. Et qui n'est pas lié à votre personne.
4. Créer une session Firefox à laquelle vous vous connecterez une seule fois, juste pour vous connecter à votre compte youtube.
5. Notez le répertoire principal de ce nouveau compte. Firefox vous le donne. Chez moi c'est de la forme `/home/mon_utilisateur/snap/firefox/common/.mozilla/firefox/foobar.yt-dlp` parce que mon compte s'appelle `yt-dlp`.
5. Maintenant vous avez le cookie qu'il faut.
6. En terminal pour pouvez utiliser ceci:

```
./yt-dlp  --cookies-from-browser firefox:/home/mon_utilisateur/snap/firefox/common/.mozilla/firefox/foobar.yt-dlp  "https://www.youtube.com/watch?v=8g28saKDM-E"
```
