# Mon blog en php

Comme vous pouvez le voir en [vous abonnant](http://laurent.claessens-donadello.eu/rss.xml), mon blog est extrêmement minimaliste. Entièrement fait à la main en html.

J'ai donc décidé de «moderniser» ça comme exercice de `php` ... travail en cours ...

## Installation

Pour mémoire ...

Pour avoir la liste des anciens articles, il faut lire le fichier `Trss.xml` (le nom va changer très bientôt). Pour ce faire j'utilise la fonction 
```php
 simplexml_load_file(  );
```
Je ne me souviens plus quel paquet il faut installer pour l'obtenir. Je crois un de ceux-ci :
```bash
apt install php-pear  libpcre3-dev
```

Ensuite redémarrer le server Apache :
```bash
sudo service apache2 restart
```
