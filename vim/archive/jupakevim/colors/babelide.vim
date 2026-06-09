"
" BabelIDE Vim Color Scheme
" =======================
"
" author: Julian Kennedy
"
set background=dark

hi clear
if exists("syntax_on")
    syntax reset
endif

let colors_name = "babelide"

" Default Colors
hi Normal       guifg=#eeeeec guibg=#000000
hi NonText      guifg=#555753 guibg=#000000 gui=none
hi NonText      ctermfg=darkgray
hi Cursor       guibg=#d3d7cf
hi lCursor      guibg=#d3d7cf

" Search
hi Search       guifg=#eeeeec guibg=#c4a000
hi Search       cterm=none ctermfg=grey ctermbg=blue
hi IncSearch    guibg=#eeeeec guifg=#729fcf
hi IncSearch    cterm=none ctermfg=yellow ctermbg=green

" Window Elements
hi StatusLine   guifg=#eeeeec guibg=#4e9a06 
hi StatusLine   ctermfg=white ctermbg=green 
hi StatusLineNC guifg=#d3d7df guibg=#4e9a06
hi StatusLineNC ctermfg=lightgray ctermbg=darkgreen
hi VertSplit    guifg=#eeeeec guibg=#eeeeec
hi Folded       guifg=#eeeeec guibg=#75507b
hi Folded       ctermfg=white ctermbg=magenta
hi Visual       guifg=#d3d7cf guibg=#4e9a06
hi Visual       ctermbg=white ctermfg=lightgreen cterm=reverse

" Specials
hi Todo         guifg=#8ae234 guibg=#4e9a06 
hi Todo         ctermfg=white ctermbg=green
hi Title        guifg=#eeeeec 
hi Title        ctermfg=white 

" Syntax
hi Comment      ctermfg=cyan cterm=none
hi Comment      guifg=#00D75F
hi CommentMultiLine     guifg=#D7D700
hi CommentSingleLine    guifg=#D7D700
hi Constant     ctermfg=darkyellow
hi Constant     guifg=#c4a000
hi Error        ctermfg=white ctermbg=red
hi Error        guifg=#eeeeec guibg=#ef2929
hi Identifier   ctermfg=darkgreen
hi Identifier   guifg=#8ae234
hi Keyword      ctermfg=39 guifg=#00AFFF
hi Number       ctermfg=darkblue
hi Number       guifg=#729fcf
hi Operator     guifg=#D1D100 gui=none
hi PreProc      ctermfg=darkred
hi PreProc      guifg=#cc0000
hi Special      ctermfg=magenta cterm=none
hi Special      guifg=#75507b
hi Statement    ctermfg=green
hi Statement    guifg=#4e9a06 
hi Type         ctermfg=gray 
hi Type         guifg=#d3d7cf 
hi FunctionName         ctermfg=46 guifg=#FF3838
hi FunctionKeyword      ctermfg=46 guifg=#00FF00

" Diff
hi DiffAdd      guifg=fg guibg=#3465a4 gui=none
hi DiffAdd      ctermfg=gray ctermbg=blue cterm=none
hi DiffChange   guifg=fg guibg=#555753 gui=none
hi DiffChange   ctermfg=gray ctermbg=darkgray cterm=none
hi DiffDelete   guibg=bg
hi DiffDelete   ctermfg=gray ctermbg=none cterm=none
hi DiffText     guifg=fg guibg=#c4a000 gui=none
hi DiffText     ctermfg=gray ctermbg=yellow cterm=none
