require('nvim-treesitter').install { 'rust', 'python', 'typescript', 'lua' }

require('nvim-treesitter').setup {
    ensure_installed = { 'lua', 'python', 'typescript' },
    auto_install = true,
    highlight = { enable = true },
}

vim.api.nvim_create_autocmd('FileType', {
  pattern = { 'rust', 'python', 'typescript', 'lua' },
  callback = function()
    vim.treesitter.start()                                    -- highlighting
    --vim.wo.foldexpr = 'v:lua.vim.treesitter.foldexpr()'     -- folds
    --vim.wo.foldmethod = 'expr'
    vim.bo.indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()" -- indentation
  end,
})

return {}
