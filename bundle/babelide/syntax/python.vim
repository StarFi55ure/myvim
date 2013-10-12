" Vim syntax file
" Language: Python
" Maintainer: Julian K
" Latest Revision: Mon Oct  8 15:08:44 SAST 2012

"if exists("b:current_syntax")
"    finish
"endif

syn match pythonClassName "class\s[a-zA-Z_][a-zA-Z_\d]*"lc=5
syn match pythonMethod "\v(def\s)@<=[a-zA-Z_][a-zA-Z_0-9]*\s*"
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

command -nargs=+ HiLink hi def link <args>

hi pythonClassName          ctermfg=135 guifg=#AF5FFF  
HiLink pythonDefKeyword         FunctionKeyword
HiLink pythonKeyword            Keyword 
HiLink pythonMethod             FunctionName
hi pythonSelfKeyword        ctermfg=172 guifg=#D78700 

hi pythonStringSingleQuote  ctermfg=41 guifg=#00D75F 
hi pythonStringDoubleQuote  ctermfg=41 guifg=#00D75F 
hi pythonStringTrippleQuote ctermfg=47 guifg=#00FF5F

hi pythonDecorator          ctermfg=33 guifg=#0087FF

hi pythonCommentSingle      ctermfg=184 guifg=#D7D700

delcommand HiLink

let b:current_syntax = "python"

