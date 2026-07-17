#!/bin/bash

platform=`uname`

VIM_ROOT=$PWD/vim
NVIM_ROOT=$PWD/nvim

if [[ $platform == 'Darwin' ]]; then
    alias readlink=greadlink
fi

# create vimrc
if [ -L $HOME/.vimrc ]; then
    echo "Removing vimrc"
    rm -f $HOME/.vimrc
fi
vimrc_file=`readlink -f $VIM_ROOT/vimrc`
ln -s $vimrc_file $HOME/.vimrc

# create gvimrc
if [ -L $HOME/.gvimrc ]; then
    echo "Removing gvimrc"
    rm -f $HOME/.gvimrc
fi
gvimrc_file=`readlink -f $VIM_ROOT/gvimrc`
ln -s $gvimrc_file $HOME/.gvimrc

# ideavimrc
if [ -L $HOME/.ideavimrc ]; then
    echo "Removing ideavimrc"
    rm -f $HOME/.ideavimrc
fi
ideavimrc_file=`readlink -f $VIM_ROOT/ideavimrc`
ln -s $ideavimrc_file $HOME/.ideavimrc

echo "Starting VIM setup..."
# link vim directory
if [ -L $HOME/.vim ]; then
    echo "Removing vim directory"
    rm -fr $HOME/.vim
fi
echo "Linking $VIM_ROOT to \$HOME/.vim"
ln -s $VIM_ROOT $HOME/.vim

root_dir=`pwd`


#echo "Starting NVIM setup..."
#if [ -d $HOME/.config/nvim ]; then
#    echo "Removing old nvim config directory"
#    rm -fr $HOME/.config/nvim
#fi
#echo "Linking $NVIM_ROOT to \$HOME/.config/nvim"
#mkdir -p $HOME/.config
#ln -s $NVIM_ROOT $HOME/.config/nvim

