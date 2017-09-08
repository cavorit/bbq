#!/bin/sh
apt-get install tmux, tree

apt-get install libncurses5-dev libgnome2-dev libgnomeui-dev
apt get libgtk2.0-dev libatk1.0-dev libbonoboui2-dev
apt-get libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev
apt-get python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git

apt-get remove vim vim-runtime gvim
apt-get remove vim-tiny vim-common vim-gui-common vim-nox

cd ~
git clone https://github.com/vim/vim.git
cd vim

# /usr/lib/python3.5 evtl. anpassen an die Verzeichnisstruktur auf Deinem Rechner

./configure --with-features=huge \
            --enable-multibyte \
            --enable-rubyinterp=yes \
            --enable-python3interp=yes \
            --with-python3-config-dir=/usr/lib/python3.5/config \
            --enable-perlinterp=yes \
            --enable-luainterp=yes \
            --enable-gui=gtk2 \
            --enable-cscope \
            --prefix=/usr/local
make VIMRUNTIMEDIR=/usr/local/share/vim/vim80

cd ~/vim
make install

update-alternatives --install /usr/bin/editor editor /usr/bin/vim 1
update-alternatives --set editor /usr/bin/vim
update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1
update-alternatives --set vi /usr/bin/vim

cp vimrc.default ~/.vimrc
cp tmux.conf.default ~/.tmux.conf
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

echo "Bitte vim starten mit test.py und :PluginInstall ausführen"
echo "vim wurde für YouCompleteMe mit /usr/lib/python3.5 kompiliert"
