# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.





from datetime import datetime as time
import os
import socket
import re
# from time import time
from pathlib import Path
from typing import List  # noqa: F401
import subprocess
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
# from libqtile.command import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
myTerm = "alacritty"
home = os.path.expanduser('~')
file_manager = "pcmanfm"
browser = "firefox"


# Function to take screenshots

def screenshot(to_clip = False, rect_select = False):
    def f(qtile):
        command = []
        
        if to_clip:
            # Requires to write one-line script `maim_to_clip` and have it in $PATH
            command += ["maim_clip"]
            # The script contains the command down below
            # 'maim -s | xclip -selection clipboard -t image/png'
        else:
            command += ["maim", f"/home/zeyrie/Pictures/Screenshots/{time.now().isoformat()}.png"]
            # command += ["maim /home/zeyrie/Pictures/Screenshots/%F-@%T-$wx$h.png"]

        if rect_select:
            command += ["-s"]

        subprocess.run(command)

    return f

########################################################################
########################################################################
##																	  ##
##							   KEYBINDINGS						  	  ##
## 																	  ##
########################################################################
########################################################################


keys = [
    Key(["mod1"], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # --------------------------------------------------------------- ##
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        # lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        # lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod,"shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move windows to the left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move windows to the right"
        ),
     Key([mod], "h",
         lazy.layout.shrink(),
         # lazy.layout.decrease_nmaster(),
         desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
         ),
     Key([mod], "l",
         lazy.layout.grow(),
         # lazy.layout.increase_nmaster(),
         desc='Expand window (MonadTall), increase number in master pane (Tile)'
         ),
     Key([mod], "n",
         lazy.layout.normalize(),
         desc='normalize window size ratios'
         ),
     Key([mod], "m",
         lazy.layout.maximize(),
         desc='toggle window between minimum and maximum sizes'
         ),
     Key([mod, "shift"], "f",
         lazy.window.toggle_floating(),
         desc='toggle floating'
         ),
     Key([mod], "f",
         lazy.window.toggle_fullscreen(),
         desc='toggle fullscreen'
         ),


    # --------------------------------------------------------------- ##
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),



    # Toggle between different layouts as defined below
    # --------------------------------------------------------------- ##
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # These are KeyChords that are used to access rofi and other shortcuts
    KeyChord([mod], "space", [
        Key([], "space", 
            lazy.spawn("rofi -show drun"),
            desc="Opens the Rofi drun prompt"
            ),
        Key([], "j",
            lazy.spawn("rofi -show run"),
            desc="Opens the Rofi run prompt"
            ),
        Key([], "k", 
            lazy.spawn("rofi -show window"),
            desc="Opens the Rofi window prompt"
            ),
        Key([], "f",
            lazy.spawn(file_manager),
            desc="Opens the PCmanfm file manager."
            ),
        Key([], "b",
            lazy.spawn(browser),
            desc="Opens the firefox browser"
            ),
            
    ]),

    # Audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 10")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 10")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #ScreenShots
    # Key([], "Print",
    #     lazy.spawn("maim \"/home/zeyrie/Pictures/Screenshots/%F-@%T-$wx$h.png\" | notify-send -u low 'Scrot' 'FullScreen taken, saved in Screenshots'"),
    #     desc='Takes a screenshot of the whole screen and saves it'
    #     ),
    # Key(["control"], "Print",
    #     lazy.spawn('maim_to_clip'),
    #     desc='Takes a screenshot of the whole screen and copies to clipboard'
    #     ),
    # Key(["shift"], "Print",
    #     lazy.spawn("scrot -s \"/home/zeyrie/Pictures/Screenshots/%F-@%T-scrot.png\" -e \"notify-send -u low 'Scrot' 'Selection taken, saved in Screenshots'\""),
    #     desc='Takes a screenshot of a selection or window and saves it'
    #     ),
    # Key(["shift", "control"], "Print",
    #     lazy.spawn("scrot -s '/home/zeyrie/Pictures/Screenshots/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f && rm $f'  -e \"notify-send -u low 'Scrot' 'Selection is copied to clipboard'\""),
    #     desc='Takes a screenshot of a selection and copies to clipboard'
    #     ),

    Key([], "Print",
        lazy.function(screenshot()),
        desc='Takes a fullscreen snap and saves it.'
        ),
    Key(["control"], "Print",
        lazy.function(screenshot(True)),
        desc='Prompts a selection for screenshot and saves it'
        ),
    Key(["shift"], "Print",
        lazy.function(screenshot(rect_select = True)),
        desc='Prompts a selection for screenshot and copies to clipboard'
        ),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      ),
    layout.Floating(**layout_theme)

]


########################################################################
########################################################################
##																	  ##
##					WIDGETS AND COLOR SCHEME						  ##
## 																	  ##
########################################################################
########################################################################


colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens


widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0],
                ), 
                widget.Image(
                    filename = "~/.config/qtile/icons/python-white.png",
                    scale = "False",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2], 
                    background = colors[0],
                ),
                widget.GroupBox(
                    font='Hurmit', 
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[2],
                    inactive = colors[7],
                    rounded = False,
                    highlight_color = colors[1],
                    highlight_method = 'line',
                    foreground = colors[2],
                    background = colors[0],
                ),
                widget.Prompt(
                    prompt = prompt,
                    font = 'Hack Mono',
                    padding = 10,
                    foreground = colors[3],
                    background = colors[1]
                ),
                # widget.Prompt(),
                widget.Sep(
                    linewidth = 0, 
                    padding = 40,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.WindowName(
                    foreground = colors[6],
                    background = colors[0],
                    padding = 0
                ),
                # widget.Systray(
                #     background = colors[0],
                #     padding = 5
                # ),
                widget.Sep(
                    linewidth = 0, 
                    padding = 40,
                    foreground = colors[0],
                    background = colors[0]
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[0],
                    foreground = colors[4],
                    padding = 0,
                    fontsize = 37
                ),
                widget.Net(
                    interface = 'wlp2s0',
                    format = '{down} ??? {up}',
                    foreground = colors[2],
                    background = colors[4],
                    padding = 5,
                    fontsize = 14
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[4],
                    foreground = colors[5],
                    padding = 0,
                    fontsize = 37
                ),
                widget.TextBox(
                    text = "???",
                    padding = 2,
                    foreground = colors[2],
                    background = colors[5],
                    fontsize = 30
                ),
                widget.CheckUpdates(
                    update_interval = 60,
                    distro = "Arch",
                    display_format = "{updates} Updates",
                    foreground = colors[2],
                    execute = ' '.join([myTerm, '-e',  'sudo pacman -Syu']),
                    # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + '-e sudo pacman -Syu')},
                    background = colors[5],
                    fontsize = 14
                ),
                # I think this widget is not properly build So CPU doesn't work 
                widget.TextBox(
                    text = '???',
                    background = colors[5],
                    foreground = colors[4],
                    padding = 0,
                    fontsize = 37
                ),
                widget.TextBox(
                    text = '???',
                    foreground = colors[2],
                    background = colors[4],
                    padding = 0,
                    fontsize = 30
                ),
                widget.CPU(
                    foreground = colors[2],
                    background = colors[4],
                    format = '{load_percent}%',
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    update_interval = 1.0,
                    fontsize = 14,
                    padding = 5,
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[4],
                    foreground = colors[5],
                    padding = 0,
                    fontsize = 37
                ),
                widget.TextBox(
                    text = '???',
                    foreground = colors[2],
                    background = colors[5],
                    padding = 0,
                    fontsize = 25
                ),
                widget.Memory(
                    foreground = colors[2],
                    background = colors[5],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + '-e htop')},
                    padding = 5,
                    fontsize = 14
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[5],
                    foreground = colors[4],
                    padding = 0,
                    fontsize = 37
                ), 
                widget.TextBox(
                    # text = '???',
                    text = '???',
                    foreground = colors[2],
                    background = colors[4],
                    padding = 0,
                    fontsize = 25
                ),
                # widget.Volume(
                #     foreground = colors[2],
                #     background = colors[4],
                #     volume_app = 'pamixer',
                #     get_volume_command="pamixer --get-volume-human",
                #     padding = 5,
                # ),
                widget.Systray(
                    background = colors[4],
                    padding = 5,
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[4],
                    foreground = colors[5],
                    padding = 0,
                    fontsize = 37
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground = colors[0],
                    background = colors[5],
                    padding = 0,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    foreground = colors[2],
                    background = colors[5],
                    padding = 5,
                    fontsize = 14
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[5],
                    foreground = colors[4],
                    padding = 0,
                    fontsize = 37
                ),
                widget.Battery(
                    foreground = colors[2],
                    background = colors[4],
                    padding = 0,
                    low_foreground = 'FF0000',
                    charge_char = '???',
                    discharge_char = '???',
                    empty_char = '???',
                    full_char = '???',
                    unknown_char = '???',
                    fontsize = 14,
                    format = "{char} {percent:2.0%} {hour:d}:{min:02d}",
                    low_percentage = 0.2,
                    notify_below = 20,
                    show_short_text = False,
                    update_interval = 60
                ),
                widget.TextBox(
                    text = '???',
                    background = colors[4],
                    foreground = colors[5],
                    padding = 0,
                    fontsize = 37
                ),
                widget.TextBox(
					text = '???',
					background = colors[5],
					foreground = colors[2],
					fontsize = 25,
					padding = 0
                ),
                widget.Clock(
                    foreground = colors[2],
                    background = colors[5],
                    format = "%A, %B %d - %H:%M ",
                    fontsize = 14
                    ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


########################################################################
########################################################################
##																	  ##
##						AUTO START HOOKER							  ##
##																	  ##
########################################################################
########################################################################


@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
