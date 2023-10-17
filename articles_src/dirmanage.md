## le problème d'import


J'ai un projet dans `/home/laurent/project`. Il contient les fichiers suivants:

```
/home/laurent/project/main.py
/home/laurent/project/src/utilities.py
/home/laurent/project/tools/other.py
```

- `main.py` est exécutable.
- `tools.py` est exécutable.
- `utilities.py` doit pouvoir être importé de n'importe où.

Le problème est de donner le chemin d'import dans `tools.py`.

## Ce que je veux

Je me donne deux contraines:

- Je veux toujours importer `utilities.py` avec
```
from src.utilities import ...
```

- Je veux que mon "working directory" soit toujours `/home/laurent/project`, c'est à dire le répertoire de base de mon projet.

La seconde contrainte est pour lire des données dans des fichiers situés par exemple dans `project/configs/foo.json`. Et je ne veux pas me demander en permanance quel est le chemin relatif de `project/configs` par rapport à l'exécutable que j'ai lancé.

Et ce, où que soit mon exécutable. Y compris si il est dans `src` ou un de ses sous-répertoires.


## Ma solution

J'ajoute dans `project/tools` le fichier `dirmanage.py` contenant
```
"""Manage the subdirectory issue."""

import os
import sys
from pathlib import Path

init_dir = Path(os.getcwd()).resolve() 
base_dir = (init_dir / "..").resolve()
os.chdir(str(base_dir))
sys.path.append(os.getcwd())
```

Ensuite dans `tools/other.py`, j'ai les lignes suivantes:

```
import dirmanage
import src.utilities
```

- Si je veux accéder au répertoire d'où le script est lancé : `dirmanage.init_dir`. Pour le répertoire de base du project : `dirmanage.base_dir`.
- Le répertoire de travail est le répertoire de base parce que `os.chdir`
- Les imports fonctionnent parce que `sys.path.append`.

	
## Un dans chaque répertoire

J'ai un tel fichier `dirmanage.py` dans chaque répertoire dans lequel j'ai un exécutable. La seule ligne à adapter est le `base_dir`.
	
## Faire plaisir au linter

Le linter se plain que `dirmanage` n'est pas utilisé. Je lui fait plaisir:
```
import dirmanage
import src.utilities
_ = dirmanage
```
