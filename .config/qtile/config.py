from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from os import path
import subprocess

from theme import colors


@hook.subscribe.startup_once
def autostart():
    subprocess.call(
        [path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])


mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key([mod], "e", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Toggle mute
    Key([mod], "shift_r", lazy.spawn("pamixer --toggle-mute"),
        desc="Toggle audio mute"),
    # Volume down
    Key([mod], "down", lazy.spawn("pamixer --decrease 5"),
        desc="Decrease audio volume"),
    # Volume up
    Key([mod], "up", lazy.spawn("pamixer --increase 5"),
        desc="Increase audio volume"),

    # Brightness down
    Key([mod], "left", lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease screen brightness"),
    # Brightness up
    Key([mod], "right", lazy.spawn("brightnessctl set +5%"),
        desc="Increase screen brightness"),

    # Applications

    # Rofi menu
    Key([mod], "m", lazy.spawn("rofi -show drun"),
        desc="Launch Rofi menu"),
    # Rofi windows nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"),
        desc="Launch Rofi windows nav"),
    # Rofi emoji selection menu
    Key([mod, "control"], "m", lazy.spawn("rofi -modi emoji -show emoji -emoji-mode menu"),
        desc="Launch Rofi emoji selection menu"),

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),
    # Launch file manager
    Key([mod], "f", lazy.spawn("thunar"),
        desc="Launch file manager"),
    # Lauch browser
    Key([mod], "b", lazy.spawn("firefox"),
        desc="Launch browser"),
    # Lauch Chrome
    Key([mod], "c", lazy.spawn("google-chrome-stable"),
        desc="Launch Google Chrome"),
    # Lauch Notion
    Key([mod], "n", lazy.spawn("notion-app"),
        desc="Lauch Notion"),
    # Lauch Discord
    Key([mod], "d", lazy.spawn("discord"),
        desc="Lauch Discord"),

    # Take screenshot
    Key([mod], "s", lazy.spawn("flameshot gui"),
        desc="Take screenshot"),

    # Media control
    Key([mod], "period", lazy.spawn("playerctl play-pause"),
        desc="Toggle between play/pause"),
    Key([mod], "minus", lazy.spawn("playerctl next"),
        desc="Skip to the next track"),
    Key([mod], "comma", lazy.spawn("playerctl previous"),
        desc="Skip to the previous track"),

]

groups = [Group(i) for i in [" ", "󰖟 ", " ", " ", " ", " ", " ", "󰌨 "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # mod + letter of group = switch to group
            Key(
                [mod],
                actual_key,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                actual_key,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    group.name),
            )
        ]
    )

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 3,
    'margin': 3
}

layouts = [
    layout.Columns(**layout_conf),
    layout.Max(**layout_conf),
    layout.RatioTile(**layout_conf),
]


def powerline(fg, bg):
    return widget.TextBox(
        foreground=[fg, fg],
        background=[bg, bg],
        text="",
        fontsize=38,
        padding=2
    )


widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=19,
    padding=3,
    background=colors['background'],
    foreground=colors['text'],
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=26,
                    margin_x=0,
                    margin_y=3,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=colors['active'],
                    inactive=colors['inactive'],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=colors['focus'],
                    disable_drag=True
                ),

                widget.WindowName(
                    foreground=colors['focus'],
                    font='UbuntuMono Nerd Font Bold',
                    padding=7,
                ),

                widget.Prompt(
                    foreground=colors['color5'],
                    cursor=True,
                    cursor_color=colors['color5'][0]
                ),

                widget.Pomodoro(
                    font='UbuntuMono Nerd Font Bold',
                    padding=8,
                    notification_on=False,
                    prefix_inactive=' ',
                    prefix_paused=' ',
                    prefix_break='',
                    prefix_long_break=''

                ),

                powerline(colors['color1'][0], colors['background'][0]),
                widget.TextBox(
                    background=colors['color1'],
                    fontsize=18,
                    text=' '
                ),
                widget.CheckUpdates(
                    background=colors['color1'],
                    colour_have_updates=colors['text'],
                    colour_no_updates=colors['text'],
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),

                powerline(colors['color2'][0], colors['color1'][0]),
                widget.TextBox(
                    background=colors['color2'][0],
                    fontsize=18,
                    text=' '
                ),
                widget.CPU(
                    background=colors['color2'][0],
                ),

                powerline(colors['color3'][0], colors['color2'][0]),
                widget.TextBox(
                    background=colors['color3'][0],
                    fontsize=18,
                    text='󰃭 '
                ),
                widget.Clock(
                    format='%d/%m/%Y',
                    background=colors['color3'][0]
                ),

                powerline(colors['color4'][0], colors['color3'][0]),
                widget.TextBox(
                    background=colors['color4'][0],
                    fontsize=18,
                    text=' '
                ),
                widget.Clock(
                    format='%H:%M',
                    background=colors['color4'][0]
                ),

                powerline(colors['color5'][0], colors['color4'][0]),
                widget.CurrentLayoutIcon(
                    background=colors['color5'],
                    scale=0.75,
                ),
                widget.CurrentLayout(
                    background=colors['color5'],
                ),

                powerline(colors['background'][0], colors['color5'][0]),
                widget.Systray(),
            ],
            28,
            opacity=1,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=colors['color5'][0],
    border_width=3
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Java UI toolkits
wmname = "LG3D"
