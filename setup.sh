#!/bin/bash

# first sort out the git inits and updates

git checkout master
git submodule update --init
git submodule foreach --recursive git checkout master

# create vimrc
if [ -e $HOME/.vimrc ]; then
    rm -f $HOME/.vimrc
fi
vimrc_file=`readlink -f vimrc`
ln -s $vimrc_file $HOME/.vimrc

# link vim directory
if [ -d $HOME/.vim ]; then
    rm -fr $HOME/.vim
fi
echo "Linking `pwd` to \$HOME/.vim"
ln -s `pwd` $HOME/.vim


