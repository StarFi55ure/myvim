
if has("unix")
    if has("gui_running")
        set guifont=Inconsolata\ Bold\ 14
        set antialias
        
        autocmd GUIEnter * set vb t_vb=
    else
        set guifont=Inconsolata\ Medium\ 12
    endif
endif

set noerrorbells
set vb t_vb=

""""""""""""""""""""""""""""""""""""""""""""""
" setup the gui options
""""""""""""""""""""""""""""""""""""""""""""""

set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar
set guioptions-=L  "remove left-hand scroll bar

"if has("gui_running")
"    set lines=999 columns=999
"endif

