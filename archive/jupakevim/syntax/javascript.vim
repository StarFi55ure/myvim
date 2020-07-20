" Vim syntax file
" 
" This is babelide syntax file for javascript
"

if !exists("main_syntax")
  if exists("b:current_syntax")
    finish
  endif
  let main_syntax = 'javascript'
endif

syn keyword javaScriptCommentTodo      TODO FIXME XXX TBD contained
syn match   javaScriptLineComment      "\v\/\/.*$" contains=@Spell,javaScriptCommentTodo
syn match   javaScriptCommentSkip      "^[ \t]*\*\($\|[ \t]\+\)"
syn region  javaScriptComment	       start="/\*"  end="\*/" contains=@Spell,javaScriptCommentTodo

syn match   javaScriptSpecial	       "\\\d\d\d\|\\."
syn region  javaScriptStringD	       start=+"+  skip=+\\\\\|\\"+  end=+"\|$+	contains=javaScriptSpecial,@htmlPreproc
syn region  javaScriptStringS	       start=+'+  skip=+\\\\\|\\'+  end=+'\|$+	contains=javaScriptSpecial,@htmlPreproc

syn match   javaScriptSpecialCharacter "'\\.'"
syn match   javaScriptNumber	       "-\=\<\d\+L\=\>\|0[xX][0-9a-fA-F]\+\>"
syn region  javaScriptRegexpString     start=+/[^/*]+me=e-1 skip=+\\\\\|\\/+ end=+/[gi]\{0,2\}\s*$+ end=+/[gi]\{0,2\}\s*[;.,)\]}]+me=e-1 contains=@htmlPreproc oneline
syn match   javaScriptOperator      "\v[+\-*=%]|\+\+|--"

syn keyword javaScriptConditional	if else switch
syn keyword javaScriptRepeat		while for do in
syn keyword javaScriptBranch		break continue
syn keyword javaScriptOperatorKeyword		new delete instanceof typeof
syn keyword javaScriptType		    Array Boolean Date Function Number Object String RegExp
syn keyword javaScriptStatement		return with
syn keyword javaScriptBoolean		true false
syn keyword javaScriptNull		    null undefined
syn keyword javaScriptIdentifier	arguments this var let
syn keyword javaScriptLabel		    case default
syn keyword javaScriptException		try catch finally throw
syn keyword javaScriptMessage		alert confirm prompt status
syn keyword javaScriptGlobal		self window top parent
syn keyword javaScriptMember		document event location 
syn keyword javaScriptDeprecated	escape unescape
syn keyword javaScriptReserved		abstract boolean byte char class const debugger double enum export extends final float goto implements import int interface long native package private protected public short static super synchronized throws transient volatile 

if exists("javaScript_fold")
    syn match	javaScriptFunction	"\<function\>"
    syn region	javaScriptFunctionFold	start="\<function\>.*[^};]$" end="^\z1}.*$" transparent fold keepend

    syn sync match javaScriptSync	grouphere javaScriptFunctionFold "\<function\>"
    syn sync match javaScriptSync	grouphere NONE "^}"

    setlocal foldmethod=syntax
    setlocal foldtext=getline(v:foldstart)
else
    syn keyword javaScriptFunction	function
    syn match   javaScriptFunctionName    "\v(function\s)@<=[a-zA-Z_][a-zA-Z_0-9]*\s*"
    syn match	javaScriptBraces	    "[{}\[\]]"
    syn match	javaScriptParens	    "[()]"
endif

syn sync fromstart
syn sync maxlines=100

if main_syntax == "javascript"
  syn sync ccomment javaScriptComment
endif

" Define the default highlighting.
command -nargs=+ HiLink hi def link <args>

HiLink javaScriptComment		    CommentMultiLine
HiLink javaScriptLineComment		CommentSingleLine
HiLink javaScriptCommentTodo		Todo

hi javaScriptObjectLiteral          guifg=blue

HiLink javaScriptSpecial		    Special
HiLink javaScriptStringS		    String
HiLink javaScriptStringD		    String
HiLink javaScriptCharacter		    Character
HiLink javaScriptSpecialCharacter	javaScriptSpecial
HiLink javaScriptNumber		        javaScriptValue
HiLink javaScriptConditional		Keyword
HiLink javaScriptRepeat		        Keyword
HiLink javaScriptBranch		        Keywork
HiLink javaScriptOperator		    Operator
HiLink javaScriptOperatorKeyword    Operator
HiLink javaScriptType			    Type
HiLink javaScriptStatement		    Keyword
HiLink javaScriptFunction		    FunctionKeyword
HiLink javaScriptFunctionName       FunctionName
HiLink javaScriptBraces		        Function
HiLink javaScriptError		        Error
HiLink javaScrParenError		    javaScriptError
HiLink javaScriptNull			    Keyword
HiLink javaScriptBoolean		    Boolean
HiLink javaScriptRegexpString		String

HiLink javaScriptIdentifier		    Keyword
HiLink javaScriptLabel		        Label
HiLink javaScriptException		    Keyword
HiLink javaScriptMessage		    Keyword
HiLink javaScriptGlobal		        Keyword
HiLink javaScriptMember		        Keyword
HiLink javaScriptDeprecated		    Exception 
HiLink javaScriptReserved		    Keyword
HiLink javaScriptDebug		        Debug
HiLink javaScriptConstant		    Label

delcommand HiLink

let b:current_syntax = "javascript"
if main_syntax == 'javascript'
  unlet main_syntax
endif

" vim: ts=8
