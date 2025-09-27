# -*- coding: utf-8 -*-
# DARK Greeting with Subscription Expiry Notice

import os, sys, time

# Colors (ANSI)
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

# Dark palette
PALETTE = [
    "\033[38;5;240m", "\033[38;5;241m", "\033[38;5;242m",  # Dark gray
    "\033[38;5;60m",  "\033[38;5;61m",  "\033[38;5;62m",   # Dark purple
    "\033[38;5;44m",  "\033[38;5;45m",  "\033[38;5;37m",   # Teal shades
]

BOX_FG = "\033[38;5;246m"
ACCENT = "\033[38;5;135m"  # Purple accent

try:
    import pyfiglet
    def big(text):
        try:
            return pyfiglet.figlet_format(text, font="slant")
        except Exception:
            return text
except Exception:
    def big(text):
        bar = "═" * (len(text) + 6)
        return f"╔{bar}╗\n║   {text}   ║\n╚{bar}╝"

def gradient(text: str, palette=PALETTE) -> str:
    out, n, i = [], len(palette), 0
    for ch in text:
        if ch == "\n":
            out.append(ch); i = 0
        else:
            out.append(palette[i % n] + ch + RESET)
            i += 1
    return "".join(out)

def strip_ansi(s: str) -> str:
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", s)

def boxify(lines):
    width = max(len(strip_ansi(s)) for s in lines)
    top = BOX_FG + "┏" + "━" * (width + 2) + "┓" + RESET
    bottom = BOX_FG + "┗" + "━" * (width + 2) + "┛" + RESET
    body = []
    for s in lines:
        pad = " " * (width - len(strip_ansi(s)))
        body.append(BOX_FG + "┃ " + RESET + s + pad + BOX_FG + " ┃" + RESET)
    return "\n".join([top, *body, bottom])

def dark_divider(text="DARK"):
    core = f"  {text}  "
    line_left  = "─" * 12
    line_right = "─" * 12
    return f"{DIM}{BOX_FG}{line_left}{RESET}{ACCENT}{core}{RESET}{DIM}{BOX_FG}{line_right}{RESET}"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    title = big("DARK")
    print(gradient(title))

    greet = [
        ACCENT + BOLD + "Welcome to DARK Mode" + RESET,
        "✨ " + PALETTE[3] + "Dark Magic" + RESET + " — " + PALETTE[6] + "Calm Colors" + RESET + " — " + PALETTE[1] + "Muted Mood" + RESET,
        ACCENT + "Your subscription expires on: 05.10.2025" + RESET,
    ]
    print(boxify(greet))
    print()
    print(dark_divider("WELCOME"))
    print()
    msg = "Enjoy the dark vibes and stay productive!"
    print(gradient(msg))
    print()

    sys.stdout.write(DIM + BOX_FG + "Loading DARK theme: " + RESET)
    sys.stdout.flush()
    for i in range(8):
        sys.stdout.write(PALETTE[i % len(PALETTE)] + "⬤" + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

if __name__ == "__main__":
    main()
