

all: install_infrastructure setup
	./setup.zsh

setup:
	./setup.zsh

install-infrastructure:
	./install_infrastructure.zsh

clear-workarea:
	rm -fr bundle/babelide/plugin/workarea/*
