
sudo pacman -Syu --noconfirm
mkdir ~/.config
mkdir ~/Images

# Display server
sudo pacman -S xorg-server --noconfirm

# Input devices configuration
ln -s ~/.dotfiles/00-keyboard.conf /etc/X11/xorg.conf.d/
ln -s ~/.dotfiles/30-touchpad.conf /etc/X11/xorg.conf.d/
ln -s ~/.dotfiles/50-mouse-acceleration.conf /etc/X11/xorg.conf.d/


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
