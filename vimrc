call pathogen#infect()
call pathogen#helptags()

syntax on
filetype plugin indent on

set shiftwidth=4
set tabstop=4
set expandtab
set softtabstop=4

set ignorecase
set hlsearch
set incsearch
set number

set textwidth=80

autocmd FileType text setlocal textwidth=80

autocmd BufRead,BufNewFile *.tal set filetype=html

inoremap jj <Esc>

set t_Co=256

colorscheme babelide

"========================================
" My mappings
"========================================
map <C-C> :
map <F2> :NERDTreeToggle<CR>
map <F3> :NERDTreeFind<CR>

set encoding=utf-8

map k <M-k>
map j <M-j>

noremap <M-k> <Esc><Esc><Esc><Esc><C-W>k<C-W>_
noremap <M-j> <Esc><Esc><Esc><Esc><C-W>j<C-W>_

"========================================
" CtrlP settings
"========================================

let g:ctrlp_match_window = 'bottom:order:btt,max:25'
let g:ctrlp_working_path_mode = 'a'
let g:ctrlp_custom_ignore = {
\ 'dir':  '\v([\/]\.(git|hg|svn)|vendor)$',
\ 'file': '\v\.(exe|so|dll)$',
\ }
let g:ctrlp_extensions = ['ideactions']

nnoremap <leader>ia :CtrlPActions<CR>

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

autocmd VimEnter * wincmd p

