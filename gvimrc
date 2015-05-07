
if has("unix")
    if has("gui_macvim")
        set guifont=Terminus\ (TTF)\ Bold:h16
        set noantialias
    else
        set guifont=Source\ Code\ Pro\ for\ Powerline\ Medium\ 10
    endif
endif

""""""""""""""""""""""""""""""""""""""""""""""
" setup the gui options
""""""""""""""""""""""""""""""""""""""""""""""

set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar
set guioptions-=L  "remove left-hand scroll bar

if has("gui_running")
    set lines=999 columns=999
endif

