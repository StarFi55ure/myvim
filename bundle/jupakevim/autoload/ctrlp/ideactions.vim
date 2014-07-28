if (exists('g:loaded_ctrlp_ideactions') && g:loaded_ctrlp_ideactions )
    finish
endif
let g:loaded_ctrlp_ideactions = 1

call add(g:ctrlp_ext_vars, {
            \ 'init': '_BabelIDE("Base_list_actions")',
            \ 'accept': '_BabelIDEAcceptAction',
            \ 'lname': 'IDE Actions',
            \ 'sname': 'actions',
            \ 'type': 'line'
            \ })

