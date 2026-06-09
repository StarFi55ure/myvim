return {
  'neovim-treesitter/nvim-treesitter',
  dependencies = { 'neovim-treesitter/treesitter-parser-registry' },
  lazy = false,
  build = ':TSUpdate',
  config = function()
      require('plugins-config.treesitter')
  end
}
