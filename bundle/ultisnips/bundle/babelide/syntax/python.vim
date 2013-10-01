" Vim syntax file
" Language: Python
" Maintainer: Julian K
" Latest Revision: Mon Oct  8 15:08:44 SAST 2012

"if exists("b:current_syntax")
"    finish
"endif

syn match pythonClassName "class\s[a-zA-Z_][a-zA-Z_\d]*"lc=5
syn match pythonMethod "def\s[a-zA-Z_][a-zA-Z_0-9]*\s*"lc=3
syn match pythonDecorator "^@[a-zA-Z_][a-zA-Z_\d]*"

syn keyword pythonDefKeyword def 

syn keyword pythonKeyword and as assert break class continue
syn keyword pythonKeyword del elif else except exec finally
syn keyword pythonKeyword for from global if import in is
syn keyword pythonKeyword lambda not or pass print raise 
syn keyword pythonKeyword return try while with yield
syn keyword pythonKeyword False True
syn keyword pythonKeyword None

syn keyword pythonSelfKeyword self

syn region pythonStringSingleQuote start="'" end="'"
syn region pythonStringDoubleQuote start="\"" end="\""
syn region pythonStringTrippleQuote start='"""' end='"""' keepend
syn region pythonCommentSingle start="#" end="$" keepend


hi pythonClassName          ctermfg=135 guifg=#AF5FFF cterm=Bold gui=Bold
hi pythonDefKeyword         ctermfg=46 guifg=#55FF55
hi pythonKeyword            ctermfg=39 guifg=#00AFFF cterm=Bold
hi pythonMethod             ctermfg=124 guifg=#AF0000
hi pythonSelfKeyword        ctermfg=172 guifg=#D78700 cterm=Bold

hi pythonStringSingleQuote  ctermfg=41 guifg=#00D75F cterm=Bold
hi pythonStringDoubleQuote  ctermfg=41 guifg=#00D75F cterm=Bold
hi pythonStringTrippleQuote ctermfg=47 guifg=#00FF5F

hi pythonDecorator          ctermfg=33 guifg=#0087FF

hi pythonCommentSingle      ctermfg=184 guifg=#D7D700

let b:current_syntax = "python"

