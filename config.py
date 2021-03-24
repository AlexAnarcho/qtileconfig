import os
import random
import requests
import json

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy

import fontawesome as fa

# Basics
mod = "mod4"
terminal = "alacritty"
network_interface = "wlp8s0"

# ///////////////////////////////////////////////////////////////////////////
# Functions
# ///////////////////////////////////////////////////////////////////////////

# Hooks
@hook.subscribe.startup
def set_wallpaper():
    """Need to set a wallpaper directory"""
    wallpaper_dir = "/home/alex/Pictures/wallpaper-imgs/"
    wallpaper_list = []
    for file in os.listdir(wallpaper_dir):
        if not file.startswith("."):
            wallpaper_list.append(wallpaper_dir + file)
    wallpaper = random.choice(wallpaper_list)
    os.system("feh --bg-scale " + wallpaper)


@hook.subscribe.client_new
def programs_to_group_startup(window):
    if "KeePassXC" in window.name:
        window.togroup(fa.icons["key"], switch_group=True)
    elif "Brave" in window.name:
        window.togroup(fa.icons["globe"], switch_group=True)
    elif "Telegram" in window.name:
        window.togroup(fa.icons["comment"], switch_group=True)
    elif "Signal" in window.name:
        window.togroup(fa.icons["comment"], switch_group=True)
    elif "Element" in window.name:
        window.togroup(fa.icons["comment"], switch_group=True)
    elif "Lutris" in window.name:
        window.togroup(fa.icons["desktop"], switch_group=True)
    elif "OBS" in window.name:
        window.togroup(fa.icons["desktop"], switch_group=True)
    elif "Audacity" in window.name:
        window.togroup(fa.icons["desktop"], switch_group=True)
    elif "VLC" in window.name:
        window.togroup(fa.icons["file-alt"], switch_group=True)
    elif "Dolphin" in window.name:
        window.togroup(fa.icons["file-alt"], switch_group=True)
    elif "Okular" in window.name:
        window.togroup(fa.icons["file-alt"], switch_group=True)
    elif "KOrganizer" in window.name:
        window.togroup(fa.icons["inbox"], switch_group=True)
    elif "Tutanota" in window.name:
        window.togroup(fa.icons["inbox"], switch_group=True)
    elif "System Settings" in window.name:
        window.togroup(fa.icons["cog"], switch_group=True)
    elif "Add/Remove Software" in window.name:
        window.togroup(fa.icons["cog"], switch_group=True)


# Groups
def my_groups():
    return [
        (fa.icons["desktop"], {"layout": "monadtall"}),
        (fa.icons["globe"], {"layout": "monadtall"}),
        (fa.icons["code"], {"layout": "monadtall"}),
        (fa.icons["key"], {"layout": "monadtall"}),
        (fa.icons["comment"], {"layout": "monadtall"}),
        (fa.icons["file-alt"], {"layout": "monadtall"}),
        (fa.icons["headphones"], {"layout": "monadtall"}),
        (fa.icons["inbox"], {"layout": "monadtall"}),
        (fa.icons["cog"], {"layout": "monadtall"}),
    ]


# Shortcuts
def my_shortcuts():
    return [
        # ---------- KEYBOARD LAYOUT ----------
        Key([mod, "shift"], "d", lazy.spawn("setxkbmap de")),
        Key([mod, "shift"], "e", lazy.spawn("setxkbmap us")),
        # ---------- WINDOW MANAGEMENT ----------
        Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
        Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
        Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),
        Key([mod], "h", lazy.layout.left(), desc="Move focus left in stack pane"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus right in stack pane"),
        Key(
            [mod, "shift"],
            "k",
            lazy.layout.shuffle_down(),
            desc="Move window down in current stack ",
        ),
        Key(
            [mod, "shift"],
            "j",
            lazy.layout.shuffle_up(),
            desc="Move window up in current stack ",
        ),
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window left in current stack ",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window right in current stack ",
        ),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        # ---------- FUNCTION KEYS ----------
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 3%- unmute")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 3%+ unmute")),
        # TODO Keyboard Backlight
        # ---------- QTILE ----------
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
        # ---------- SCRIPTS ----------
        KeyChord(
            [mod],
            "s",
            [
                Key(
                    [],
                    "c",
                    lazy.spawn("python /home/alex/Coding/pythonscripts/claphands.py"),
                    desc="Clap 👏 Hands",
                ),
                Key(
                    [],
                    "v",
                    lazy.spawn("script-ytv getclip"),
                    desc="Automatically download URL as video",
                ),
                Key(
                    [],
                    "a",
                    lazy.spawn("script-yta getclip"),
                    desc="Automatically download URL as audio",
                ),
            ],
        ),
        # ---------- LAUNCH PROGRAMS ----------
        KeyChord(
            [mod],
            "d",
            [
                Key([], "space", lazy.spawn(terminal), desc="Launch terminal"),
                Key([], "b", lazy.spawn("brave"), desc="Launch Browser"),
                Key(
                    [],
                    "s",
                    lazy.spawn("signal-desktop"),
                    desc="Launch Signal",
                ),
                Key(
                    [],
                    "m",
                    lazy.spawn("element-desktop"),
                    desc="Launch Matrix client Element",
                ),
                Key(
                    [],
                    "t",
                    lazy.spawn("telegram-desktop"),
                    desc="Launch Telegram",
                ),
                Key(
                    [],
                    "k",
                    lazy.spawn("keepassxc"),
                    desc="Launch KeepAssXC",
                ),
                Key([], "d", lazy.spawn("dolphin"), desc="Launch Dolphin"),
                Key([], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
            ],
        ),
        # ---------- ROFI ----------
        KeyChord(
            [mod],
            "space",
            [
                Key(
                    [],
                    "space",
                    lazy.spawn("rofi -show drun"),
                    desc="Spawn a command using a prompt widget",
                ),
                Key(
                    [],
                    "e",
                    lazy.spawn("rofi -show emoji -modi emoji"),
                    desc="Spawn a command using a prompt widget",
                ),
                Key(
                    [],
                    "w",
                    lazy.spawn("rofi -show window"),
                    desc="Spawn a command using a prompt widget",
                ),
                Key(
                    [],
                    "n",
                    lazy.spawn("rofi-wifi-menu -config ~/dotfiles/rofi/monokai.rasi"),
                    desc="Spawn wifi menu",
                ),
                Key(
                    [],
                    "b",
                    lazy.spawn("rofi-bluetooth"),
                    desc="Spawn bluetooth menu",
                ),
            ],
        ),
        # ---------- EMACS ----------
        KeyChord(
            [mod],
            "i",
            [
                Key(
                    [],
                    "e",
                    lazy.spawn("emacsclient -c -a 'emacs'"),
                    desc="Launch Emacs",
                ),
                Key(
                    [],
                    "s",
                    lazy.spawn("emacs --daemon"),
                    desc="Start Emacs daemon",
                ),
                Key(
                    [],
                    "b",
                    lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                    desc="Launch ibuffer inside Emacs",
                ),
                Key(
                    [],
                    "d",
                    lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                    desc="Launch dired inside Emacs",
                ),
                Key(
                    [],
                    "k",
                    lazy.spawn("pkill emacs"),
                    desc="Kill emacs",
                ),
            ],
        ),
    ]


def my_group_shortcuts(keys, group_names):
    for i, (name, kwargs) in enumerate(group_names, 1):
        keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
        keys.append(
            Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True))
        )


# Widgets
def get_line_sep():
    return widget.Sep(
        padding=10, linewidth=2, size_percentage=80, foreground=colors["black"]
    )


def get_groupbox():
    return widget.GroupBox(
        active=colors["green"],
        inactive=colors["black"],
        this_current_screen_border=colors["green"],
        urgent_border=colors["red"],
        padding=6,
        fontsize=18,
    )


def get_diskinfo():
    return widget.DF(
        format=fa.icons["save"] + " {r:.0f}% full [{uf}{m} left]",
        warn_space=50,
        visible_on_warn=False,
        warn_color=colors["red"],
        measure="G",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("dolphin")},
    )


def get_netstats():
    return widget.Net(
        format="{down} "
        + fa.icons["arrow-circle-down"]
        + fa.icons["arrow-circle-up"]
        + " {up}",
        update_interval=2,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi-wifi-menu")},
    )


def get_volume():
    return widget.Volume(
        # fmt=fa.icons["speaker"],
        padding=5,
    )


def get_battery():
    return widget.Battery(
        charge_char=fa.icons["bolt"],
        discharge_char=fa.icons["laptop"],
        empty_char=fa.icons["battery-empty"],
        full_char=fa.icons["battery-full"],
        show_short_text=False,
        low_percentage=0.30,
        notify_below=0.15,
        format="{char} {percent:2.0%} {hour:d}:{min:02d}",
        update_interval=30,
    )


def get_keyboard():
    return widget.KeyboardLayout(
        configured_keyboards=["us", "de"],
        display_map={"us": fa.icons["keyboard"], "de": "🇩🇪"},
        update_interval=1,
    )


def get_clock():
    return widget.Clock(
        format="%d %b "
        + fa.icons["calendar-alt"]
        + " %H:%M"
        + " "
        + fa.icons["hourglass"],
        update_interval=15,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("korganizer")},
    )


def get_cryptoprice(tickerid):
    """Query coinpaprika API for USD price. Return price as int."""
    url = "https://api.coinpaprika.com/v1/tickers/" + tickerid
    try:
        resp = requests.get(url)
    except:
        resp = '{"quotes": {"USD": {"price": "loading"}}}'

    data = json.loads(resp.content)
    price = round(data["quotes"]["USD"]["price"])
    return price


def get_xmr_price():
    price = get_cryptoprice("xmr-monero")
    return f"${price}"


def get_btc_price():
    price = get_cryptoprice("btc-bitcoin")
    return f"${price}"


def get_xmr_btc():
    """Calculate xmr/btc via usd price of both"""
    ratio = round(get_cryptoprice("xmr-monero") / get_cryptoprice("btc-bitcoin"), 4)
    output = f"({str(ratio)} btc)"
    return output


def get_cpu():
    return widget.CPU(
        format="{freq_current}GHz {load_percent}%",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e bashtop")},
    )


def get_updates():
    # not showing correctly in bar
    return widget.CheckUpdates(
        update_interval=1800,
        distro="Arch_checkupdates",
        format="{updates} " + fa.icons["cubes"],
        foreground=colors["white"],
        colour_have_updates=colors["green"],
        colour_no_updates=colors["foreground"],
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo paru")
        },
    )


# Bars
def get_top_bar():
    return bar.Bar(
        [
            widget.Spacer(length=8),
            get_groupbox(),
            # widget.WindowName(font="Noto Sans", fontsize=13),
            widget.Spacer(),
            # widget.Notify(),
            widget.Cmus(
                noplay_color=colors["black"],
                play_color=colors["green"],
                fontsize=10,
            ),
            get_line_sep(),
            widget.TextBox(fmt=fa.icons["monero"], foreground=colors["white"]),
            widget.GenPollText(
                func=get_xmr_price,
                update_interval=60,
            ),
            widget.GenPollText(
                func=get_xmr_btc,
                update_interval=60,
                fontsize=10,
            ),
            get_line_sep(),
            widget.TextBox(fmt=fa.icons["bitcoin"], foreground=colors["white"]),
            widget.GenPollText(
                func=get_btc_price,
                update_interval=60,
            ),
            get_line_sep(),
            get_diskinfo(),
            get_line_sep(),
            widget.TextBox(fmt=fa.icons["hdd"]),
            get_cpu(),
            get_line_sep(),
            widget.TextBox(fmt=fa.icons["server"]),
            get_netstats(),
            # get_updates(),  # not working properly
            get_line_sep(),
            widget.TextBox(fmt=fa.icons["headphones"]),
            get_volume(),
            get_line_sep(),
            widget.Systray(),
            get_line_sep(),
            get_battery(),
            get_line_sep(),
            get_keyboard(),
            get_line_sep(),
            get_clock(),
            widget.Spacer(length=8),
        ],
        34,
        background=colors["background"],
    )


# Colorpalet - Dracula Theme
def my_colors():
    return {
        "background": "282a36",
        "foreground": "f8f8f2",
        "black": "#575b70",
        "red": "#ff5555",
        "green": "#50fa7b",
        "yellow": "#f1fa8c",
        "blue": "#caa9fa",
        "magenta": "#ff79c6",
        "cyan": "#8be9fd",
        "white": "#bfbfbf",
        # -------------------
        # "background": "1E3231",
        # "foreground": "4EFF47",
        # "lighter": "937680",
        # "calm": "3B73CE",
        # "white": "FEFDFF",
        # "gray": "725A62",
    }


# Theme
def my_layout_theme():
    layout_theme = {
        "border_width": 2,
        "margin": 5,
        "border_focus": colors["cyan"],
        "border_normal": colors["background"],
    }

    return layout_theme


def my_widget_defaults():
    widget_defaults = dict(
        font="Hack", fontsize=15, padding=3, foreground=colors["white"]
    )
    return widget_defaults


# ///////////////////////////////////////////////////////////////////////////
# Actual Config
# ///////////////////////////////////////////////////////////////////////////

# Colors
colors = my_colors()

# Shortcuts
keys = my_shortcuts()

# Groups
group_names = my_groups()
groups = [Group(name, **kwargs) for name, kwargs in group_names]
my_group_shortcuts(keys, group_names)

# Layouts
layout_theme = my_layout_theme()
layouts = [
    layout.Bsp(**layout_theme),
]

# Widgets
widget_defaults = my_widget_defaults()
extension_defaults = widget_defaults.copy()

# Screens
screens = [
    Screen(
        top=get_top_bar(),
    ),
]

# Default Settings
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "QT Doom Archer"
