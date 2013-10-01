#!/bin/zsh

# Install all the necessary infrastructure

root_dir=`pwd`

########################################################################
# setup babelide python environment
########################################################################

if [ ! -d bundle/babelide/plugin/pyenv ]; then
    echo "Creating virtual python for babelide"
    cd bundle/babelide/plugin

    virtualenv pyenv
    source pyenv/bin/activate
    /usr/bin/env python setup.py develop
    deactivate

    cd $root_dir

else
    echo "Updating virtual python for babelide"
    cd bundle/babelide/plugin

    source pyenv/bin/activate
    /usr/bin/env python setup.py develop
    deactivate

    cd $root_dir

fi

