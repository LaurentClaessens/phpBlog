## neovim

Installation pas à pas de neovim pour Ubuntu. J'utilise [fish](https://fishshell.com/). Si vous utiliser encore bash, vous devrez faire quelque adaptations.

## install

Le néovim fournit par `apt` est trop vieux pour faire tourner l'extension `vim-tree.lua` que je veux. Donc on passe par snap:
```
sudo snap install nvim --classic
```

## nvm (node)

L'extension `vim-tree.lua` nécessite sous le capot d'avoir node 16. Nous l'installons avec [nvm](https://github.com/nvm-sh/nvm).

```
set nvm_version 0.39.3   
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v$nvm_version/install.sh | bash

bash 
nvm install 16
exit
```

## installer vim-plug

J'utilise le mécanisme [vim-plug](https://github.com/junegunn/vim-plug).

```
curl -fLo "$HOME/.local/share/nvim/site/autoload/plug.vim" --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

## init.vim

Voici la partie non triviale de mon fichier `init.vim` qui doit être dans `~/.config/nvim/init.vim`:
```
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')
Plug 'nvim-tree/nvim-web-devicons'
Plug 'nvim-tree/nvim-tree.lua'
Plug 'sheerun/vim-polyglot'
Plug 'sbdchd/neoformat'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

lua << EOF
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
vim.opt.termguicolors = true
require("nvim-tree").setup()
EOF


let g:coc_node_path = '~/.nvm/versions/node/v16.19.1/bin/node'
```
Vous devez adapter la ligne `coc_node_path` pour mettre le chemin dans lequel se trouve réellement votre node installé par nvm.


## premier lancement de neovim

```
nvim test.txt
```
Il donne pas mal d'erreurs au lancement. Pas de problèmes.

Pour instaler tout ce qui manque, il suffit de lancer (à l'intérieur de nvim) la commande
```
:PlugInstall
```

Quittez neovim et relancez. On est bon.

## coc-pyright

```
sudo apt install yarn yarnpkg
bash
nvm use 16
nvim test.py
```

Puis dans nvim:
```
:CocInstall coc-pyright
```
Si ça ne marche pas: 


```
cd ~/.local/share/nvim/plugged/coc.nvim
bash
nvm use 16
npm install coc.nvim
```

## Orthographe

Ouvre un autre néovim avec

```
nvim -u none
:set spelllang=fr
:spell
```
