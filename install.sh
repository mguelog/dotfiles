#!/bin/bash

sudo pacman -Syu --noconfirm
mkdir ~/.config
mkdir ~/Images


# AUR helper
sudo pacman -S git base-devel --noconfirm
cd /opt
sudo git clone https://aur.archlinux.org/yay.git
sudo chown -R $USER yay
cd yay
makepkg -si
cd ~/.dotfiles


# Display server
sudo pacman -S xorg-server --noconfirm

# Input devices configuration
sudo ln -s ~/.dotfiles/00-keyboard.conf /etc/X11/xorg.conf.d/
sudo ln -s ~/.dotfiles/30-touchpad.conf /etc/X11/xorg.conf.d/
sudo ln -s ~/.dotfiles/50-mouse-acceleration.conf /etc/X11/xorg.conf.d/


# Display manager
sudo pacman -S lightdm lightdm-gtk-greeter --noconfirm
systemctl enable lightdm


# Window manager
sudo pacman -S qtile pacman-contrib python-pip --noconfirm
pip3 install psutil
ln -s ~/.dotfiles/.config/qtile ~/.config/


# Compositor
sudo pacman -S picom --noconfirm


# Wallpaper setter
sudo pacman -S feh --noconfirm
ln -s ~/.dotfiles/.wallpapers ~/Images/Wallpapers


# Command-line shell
ln -s ~/.dotfiles/.bashrc ~/


# Terminal emulator
sudo pacman -S alacritty --noconfirm
ln -s ~/.dotfiles/.config/alacritty ~/.config/


# File manager
sudo pacman -S thunar --noconfirm
ln -s ~/.dotfiles/.config/Thunar ~/.config/


# Application launcher
sudo pacman -S rofi papirus-icon-theme rofi-emoji xdotool xclip noto-fonts-emoji --noconfirm
ln -s ~/.dotfiles/.config/rofi ~/.config/


# Theming
sudo pacman -S gtk3 --noconfirm
mkdir ~/.themes
cd ~/.themes
git clone https://github.com/UnnatShaneshwar/AtomOneDarkTheme.git onedark
git clone https://github.com/dracula/gtk.git dracula
mkdir ~/.icons
cd ~/.icons
git clone https://github.com/adhec/one-dark-icons onedark
git clone https://github.com/m4thewz/dracula-icons dracula
cd ~/.dotfiles
ln -s ~/.dotfiles/.config/gtk-3.0 ~/.config/


# Git
sudo pacman -S git --noconfirm
ln -s ~/.dotfiles/.config/git ~/.config/
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh > ~/.dotfiles/.config/git/git-prompt.sh
