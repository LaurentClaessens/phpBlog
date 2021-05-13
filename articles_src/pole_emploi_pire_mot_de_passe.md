## Contraintes idiotes sur les mots de passe

J'ai récemment créé un compte employeur sur Pôle-emploi. Les contraintes sur le mot de passe sont les pires que j'aie vues.


### Longueur

Le mot de passe est limité en longueur : entre 8 et 12 caractères.

### Pas de copier-coller

Il est impossible de copier-coller un mot de passe. Donc il faut le taper à la main. Cela interdit de facto les mots de passe réellement aléatoires.

### Caractères spéciaux

Obligation d'utiliser au moins :

- une majuscule
- un chiffre
- un caractère spéciaux parmi une liste d'une dizaines de caractères.

Cette contraire affaiblit le mot de passe. 

Certes, choisir 12 caractères totalement aléatoire dans un alphabet de 26+26+10+10=72 caractères est (un peu) plus fort que 12 caractères totalement aléatoires parmi les 26 lettres de l'alphabet.

Mais personne ne va réellement mélanger tous ces éléments. En effet, ce que tout le monde va faire, c'est 10 lettres suivies de un caractère spécial et un chiffre (presque certainement 1).

Vous en voulez une preuve ? Voici le dernier affront de Pôle-Emploi contre la sécurité informatique ...

### L'exemple

Pôle-Emploi donne comme exemple ceci : "iNterEt?1". Oui : "internet" avec une substitution complètement triviale de majuscules, suivie de 1 caractère spécial et un chiffre (le 1 évidemment).

Bref, le mot proposés par Pôle-Emploi est en gros le pire mot de passe possible. Il combine deux inconvénients grave :

- il est facile à craquer en force brute par un ordinateur.
- il est compliqué à retenir par un humain.

### Un peu d'arithmétique

Suivant l'exemple de Pôle-Emploi, on procède comme suit :

- on choisit un mot
- on substitue deux majuscules
- on ajoute un chiffre
- on ajoute un caractère spécial

Voyons le nombre de possibilités :

- choisir un mot : disons 1000 possibilités
- choisir deux lettres dans le mot, pour un mot de 8 lettres, il y a `8*7=56` possibilités.
- ajouter un chiffre : 10 possibilités
- ajouter un caractère spécial : 10 possibilités
- mettre le chiffre avant ou après le caractère spécial : 2 possibilités.

Bref, en gros : `1000*56*10*10*2=11000000`. Onze millions de possibilités.

Disons qu'en suivant les conseils de Pôle-Emploi, un gars normal devrait se faire très rapidement craquer.

Et vous savez quoi ? Onze millions de possibilités, c'est un peu moins que le nombre de mots de passe de ... 5 lettres.

Prenez un mot de passe de seulement 5 lettres minuscules (vraiment mélangées), et vous avez déjà mieux que ce que Pôle-Emploi propose.

### J'accuse les caractères spéciaux

Je dit que clairement, ce sont les contraintes «il faut mettre tels et tels caractères» qui poussent à trouver des stratégies de contournement. Forcément, on en arrive à faire quelque substitutions simples à partir d'un mot dans un dictionnaire.

### Un peu d'ironie

Pôle-Emploi passe son temps à rappeler qu'ils ne demandent jamais de mot de passe par mail; qu'il faut faire attention aux scams etc. Un peu comme si ils étaient préoccupés par la sécurité informatique.

