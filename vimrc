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

inoremap jj <Esc>

set t_Co=256

colorscheme tango

"========================================
" My custom mappings
"========================================
map <C-C> :
map <F2> :NERDTreeToggle<CR>

" Must figure out what this does
"autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p

