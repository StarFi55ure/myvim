" Vim syntax file
" Language: Python
" Maintainer: Julian K
" Latest Revision: Mon Oct  8 15:08:44 SAST 2012

"if exists("b:current_syntax")
"    finish
"endif

syn match pythonMethod "def\s[a-zA-Z_][a-zA-Z_\d]*\s*"lc=3

syn keyword pythonKeyword and as assert break class continue
syn keyword pythonKeyword del elif else except exec finally
syn keyword pythonKeyword for from global if import in is
syn keyword pythonKeyword lambda not or pass print raise 
syn keyword pythonKeyword return try while with yield

syn keyword pythonDefKeyword def 
syn keyword pythonSelfKeyword self

set t_Co=256

hi pythonKeyword            ctermfg=33
hi pythonDefKeyword         ctermfg=46
hi pythonSelfKeyword        ctermfg=172 cterm=Bold
hi pythonMethod             ctermfg=124

let b:current_syntax = "pythonj"

