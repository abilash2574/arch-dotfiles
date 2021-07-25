" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

" This is where you add all your plugins
call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'

    " File Explorer
    Plug 'preservim/nerdtree'
 
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'

    "Installing gruvbox
    Plug 'morhetz/gruvbox'

    " Dark color sheme
    Plug 'ghifarit53/tokyonight-vim'
        
    " Nord Plugin
    Plug 'arcticicestudio/nord-vim'

    " palenight a elegant dark theme
    Plug 'drewtempelmeyer/palenight.vim'


    "Installing git support to vim
    "Plug 'tpope/vim-fugitive'

    " This helps in adding comments much faster.
    Plug 'tpope/vim-commentary'
    
    " Plug 'preservim/nerdcommenter'
    
    "There are two plugins that works as file finder
    "ctrlpvim
    "Plug 'ctrlpvim/ctrlp.vim'
    
    "Then its fzf
    "Plug 'junegunn/fzf.vim'
    
    " If you find yourself in need of code completion you must use coc or ycm    

    " Start Screen for vim Startify
    Plug 'mhinz/vim-startify'

    " This plugin is for Airline Status line.
    Plug 'vim-airline/vim-airline'
    
    " which key is a plugin to use leader key mapping extensively
    Plug 'liuchengxu/vim-which-key'

    " Plug 'mhinz/vim-signify'      " Learn about all this in free time
    Plug 'tpope/vim-fugitive'

    Plug 'tpope/vim-rhubarb'
    " Plug 'junegunn/gv.vim' 
    
    Plug 'justinmk/vim-sneak'       " This is quite intresting see it
    
    Plug 'unblevable/quick-scope'
    
    Plug 'voldikss/vim-floaterm'
    
    Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
    
    "
    call plug#end()
