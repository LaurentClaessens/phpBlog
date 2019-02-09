## Copier le frido de ma machine vers OVH

Mon site personnel sur lequel est hébergé entre autres [le frido](https://laurent.claessens-donadello.eu/pdf/lefrido.pdf) est hébergé chez OVH.

### Question

Comment copier automatiquement le pdf du Frido de ma machine vers OVH ?

### Activer sftp chez OVH

- Dans l'espace personnel chez OVH, aller dans "Hébergements" et ensuite dans l'onglet "FTP-SSH".
- Activer SFTP

### Mettre la clef publique

En utilisant un `pftp` non interactif créer le répertoire `.ssh` et y mettre `authorized_keys`

### Le script local

Créer en local un fichier `batchfile` contenant

```
cd laurent/pdf
put lefrido.pdf
```

Maintenant il ne reste qu'à lancer la commande
```
sftp -b batchfile claessenvs@ftp.cluster003.ovh.net
```
