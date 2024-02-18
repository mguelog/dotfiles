#!/bin/bash

sudo pacman -Syu --noconfirm
mkdir ~/.config


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
sudo pacman -S qtile pacman-contrib python-psutil --noconfirm
ln -s ~/.dotfiles/.config/qtile ~/.config/


# Compositor
sudo pacman -S picom --noconfirm


# Wallpaper setter
sudo pacman -S feh --noconfirm


# Command-line shell
ln -s ~/.dotfiles/.bashrc ~/


# Terminal emulator
sudo pacman -S alacritty --noconfirm
ln -s ~/.dotfiles/.config/alacritty ~/.config/


# File manager
sudo pacman -S thunar --noconfirm
ln -s ~/.dotfiles/.config/Thunar ~/.config/


# Text editor
sudo pacman -S code --noconfirm
yay -S code-oss-marketplace --noconfirm
ln -s ~/.dotfiles/.config/'Code - OSS' ~/.config/

code --install-extension ms-vscode.cpptools
code --install-extension ms-python.python
code --install-extension vivaxy.vscode-conventional-commits
code --install-extension pejmannikram.vscode-auto-scroll
code --install-extension naumovs.color-highlight

code --install-extension zhuangtongfa.Material-theme
code --install-extension dracula-theme.theme-dracula


# Application launcher
sudo pacman -S rofi papirus-icon-theme rofi-emoji xdotool xclip noto-fonts-emoji --noconfirm
ln -s ~/.dotfiles/.config/rofi ~/.config/


# Theming
sudo pacman -S gtk3 --noconfirm

mkdir ~/.dotfiles/.themes
cd ~/.dotfiles/.themes
git clone https://github.com/UnnatShaneshwar/AtomOneDarkTheme.git onedark
git clone https://github.com/dracula/gtk.git dracula
ln -s ~/.dotfiles/.themes ~/

mkdir ~/.dotfiles/.icons
cd ~/.dotfiles/.icons
git clone https://github.com/adhec/one-dark-icons onedark
git clone https://github.com/m4thewz/dracula-icons dracula
ln -s ~/.dotfiles/.icons ~/

cd ~/.dotfiles
ln -s ~/.dotfiles/.config/gtk-3.0 ~/.config/


# Notification daemon
sudo pacman -S notification-daemon --noconfirm
sudo ln -s ~/.dotfiles/org.freedesktop.Notifications.service /usr/share/dbus-1/services/


# Fonts
sudo pacman -S fontconfig noto-fonts ttf-ubuntu-mono-nerd --noconfirm
ln -s ~/.dotfiles/.config/fontconfig ~/.config/


# Screen capture
sudo pacman -S flameshot --noconfirm
ln -s ~/.dotfiles/.config/flameshot ~/.config/


# Backlight control
sudo pacman -S brightnessctl --noconfirm


# Screen temperature
sudo pacman -S redshift --noconfirm


# Audio control
sudo pacman -S pulseaudio pamixer pavucontrol --noconfirm


# Media control
sudo pacman -S playerctl --noconfirm


# Web browser
sudo pacman -S firefox --noconfirm
yay -S firefox-extension-arch-search --noconfirm


# Git
sudo pacman -S git --noconfirm
ln -s ~/.dotfiles/.config/git ~/.config/
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh > ~/.dotfiles/.config/git/git-prompt.sh
