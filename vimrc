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

colorscheme tango

"========================================
" My custom settings
"========================================
let g:ctrlp_open_new_file = 'h'
let g:ctrlp_arg_map = 1
let g:ctrlp_max_files = 40000
let g:ctrlp_max_height = 30
let g:ctrlp_max_depth = 15
let g:ctrlp_user_command = 'find %s -type f'

"========================================
" My custom mappings
"========================================
map <C-C> :
map <F2> :NERDTreeToggle<CR>

set encoding=utf-8

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

autocmd VimEnter * wincmd p

