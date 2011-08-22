#!/bin/bash

rm -f $HOME/.vimrc
vimrc_file=`readlink -f vimrc`
ln -s $vimrc_file $HOME/.vimrc
