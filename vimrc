
syntax on
filetype plugin indent on

set noerrorbells
set belloff=all

if has('win32') || has('win64')
    set runtimepath-=~/vimfiles
    set runtimepath^=~/.vim
    set runtimepath-=~/vimfiles/after
    set runtimepath+=~/.vim/after

    set backup
    set dir=$TMP
    set backupdir=$TMP
    set directory=$TMP
    set noundofile

    set backspace=2
    set backspace=indent,eol,start
endif

" ========================================
" Install Plugins
" ========================================

call plug#begin('~/.vim/bundle')

Plug 'vim-airline/vim-airline'
Plug 'kien/ctrlp.vim'
Plug 'tpope/vim-fugitive'
Plug 'scrooloose/nerdtree'
Plug 'tpope/vim-surround'
Plug 'flazz/vim-colorschemes'
Plug '~/.vim/bundle/jupakevim'
Plug 'nelsonjchen/vim-carto'
Plug 'vimwiki/vimwiki'
Plug 'sirtaj/vim-openscad'

call plug#end()

" ========================================
" Setup main settings
" ========================================

set shiftwidth=4
set tabstop=4
set expandtab
set softtabstop=4

set ignorecase
set hlsearch
set incsearch
set number

autocmd FileType text setlocal textwidth=80
autocmd FileType python setlocal textwidth=80

autocmd BufRead,BufNewFile *.tal set filetype=html

inoremap jj <Esc>

set t_Co=256

colorscheme babelide
set encoding=utf-8

"========================================
" My mappings
"========================================

map <C-C> :
map <F2> :NERDTreeToggle<CR>
map <F3> :NERDTreeFind<CR>

map k <M-k>
map j <M-j>

noremap <M-k> <Esc><Esc><Esc><Esc><C-W>k<C-W>_
noremap <M-j> <Esc><Esc><Esc><Esc><C-W>j<C-W>_

"========================================
"force myself to use vim properly
"========================================
map <Up> <nop>
map <Down> <nop>
map <Left> <nop>
map <Right> <nop>

imap <Up> <nop>
imap <Down> <nop>
imap <Left> <nop>
imap <Right> <nop>
"========================================
" CtrlP settings
"========================================

map <C-p> :CtrlP

let g:ctrlp_match_window = 'bottom:order:btt,max:25'
let g:ctrlp_working_path_mode = 'a'
let g:ctrlp_custom_ignore = {
\ 'dir':  '\v([\/]\.(git|hg|svn)|vendor)$',
\ 'file': '\v\.(exe|so|dll)$',
\ }
let g:ctrlp_extensions = ['ideactions']

nnoremap <leader>ia :CtrlPActions<CR>

autocmd VimEnter * wincmd p

"=========================================
" Vimwiki Settings
"=========================================

let g:vimwiki_list = [{'path': '~/Dropbox/vimwiki/', 'syntax': 'markdown', 'ext': 'md'}]


"=========================================
" Setup powerline
"=========================================
"set rtp+=~/.myvim/bundle/powerline/powerline/bindings/vim


