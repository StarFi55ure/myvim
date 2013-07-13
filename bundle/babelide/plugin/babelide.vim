" File: babelide.vim
" Author: Julian Kennedy 
"
" Description: My custom IDE
"

if exists('did_BabelIDE_vim')
    finish
endif


"==================================================================
" Initialize python for this plugin
"==================================================================

" Set python version to use 
" (Taken from Ultisnips
"
if !exists("g:BabelIDEUsePythonVersion")
    let g:_uspy=":py3 "
    if !has("python3")
        if !has("python")
            if !exists("g:UltiSnipsNoPythonWarning")
                echo  "BabelIDE requires py >= 2.7 or any py3"
            endif
            finish
        endif
        let g:_uspy=":py "
    endif
    let g:BabelIDEUsePythonVersion = "<tab>"
else
    if g:BabelIDEUsePythonVersion == 2
        let g:_uspy=":py "
    else
        let g:_uspy=":py3 "
    endif
endif

" Expand our path
" (Based on implementation in Ultisnips)
"
let g:BabelIDEBaseDir=expand("<sfile>:h")

exec g:_uspy "import vim, os, sys"
exec g:_uspy "babelide_basedir = vim.eval('g:BabelIDEBaseDir')"
exec g:_uspy "vim.command(\"let g:BabelIDEPythonPath = '%s'\" % babelide_basedir)"
exec g:_uspy "sys.path.append(babelide_basedir)"

"==================================================================
" Initialize the plugin
"==================================================================

exec g:_uspy "from babelide import BabelIDE_Manager"
exec g:_uspy "BabelIDE_Manager.init(babelide_basedir)"

"==================================================================
" Create the global function bindings
"==================================================================

"==================================================================
" Setup HTML5 module
"==================================================================

"==================================================================
" Setup Python module
"==================================================================

"==================================================================
" Setup global plugin key bindings
"==================================================================



let did_BabelIDE_vim=1
