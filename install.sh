
# Display server
sudo pacman -S xorg-server

# Input devices configuration
localectl set-x11-keymap es
sudo cp 30-touchpad.conf /etc/X11/xorg.conf.d/
sudo cp 50-mouse-acceleration.conf /etc/X11/xorg.conf.d/


# Display manager
sudo pacman -S lightdm lightdm-gtk-greeter
systemctl enable lightdm


# Window manager
sudo pacman -S qtile
ln -s ~/.dotfiles/.config/qtile ~/.config/


# Compositor
sudo pacman -S picom


# Wallpaper setter
sudo pacman -S feh
ln -s ~/.dotfiles/.wallpapers ~/Images/Wallpapers
feh --bg-scale ~/Images/Wallpapers/arch-green.png &
