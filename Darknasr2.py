# -*- coding: utf-8 -*-
# DARK Greeting (hardened) + Subscription expiry & days left

import os, sys, time, datetime, math

# ===== ANSI =====
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

PALETTE = [
    "\033[38;5;240m", "\033[38;5;241m", "\033[38;5;242m",  # Dark gray
    "\033[38;5;60m",  "\033[38;5;61m",  "\033[38;5;62m",   # Dark purple
    "\033[38;5;44m",  "\033[38;5;45m",  "\033[38;5;37m",   # Teal
]
BOX_FG = "\033[38;5;246m"
ACCENT = "\033[38;5;135m"

# ===== Safe pyfiglet =====
def big(text: str) -> str:
    try:
        import pyfiglet
        try:
            return pyfiglet.figlet_format(text, font="slant")
        except Exception:
            return pyfiglet.figlet_format(text)
    except Exception:
        bar = "═" * (len(text) + 6)
        return f"╔{bar}╗\n║   {text}   ║\n╚{bar}╝"

# ===== Helpers =====
def strip_ansi(s: str) -> str:
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", s)

def gradient(text: str, palette=PALETTE) -> str:
    if not text:
        return text
    out = []
    n = len(palette)
    i = 0
    for ch in text:
        if ch == "\n":
            out.append(ch)
            i = 0
        else:
            out.append(palette[i % n] + ch + RESET)
            i += 1
    return "".join(out)

def boxify(lines):
    width = 0
    for s in lines:
        L = len(strip_ansi(s))
        if L > width:
            width = L
    top = BOX_FG + "┏" + "━" * (width + 2) + "┓" + RESET
    bot = BOX_FG + "┗" + "━" * (width + 2) + "┛" + RESET
    body = []
    for s in lines:
        pad = " " * (width - len(strip_ansi(s)))
        body.append(BOX_FG + "┃ " + RESET + s + pad + BOX_FG + " ┃" + RESET)
    return "\n".join([top, *body, bot])

def dark_divider(text="WELCOME"):
    core = f"  {text}  "
    line = "─" * 12
    return f"{DIM}{BOX_FG}{line}{RESET}{ACCENT}{core}{RESET}{DIM}{BOX_FG}{line}{RESET}"

def clear():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass

def days_until(day: int, month: int, year: int) -> int:
    try:
        today = datetime.date.today()
        target = datetime.date(year, month, day)
        delta = (target - today).days
        return delta
    except Exception:
        return 0

# ===== Main =====
SUB_EXPIRY = "05.10.2025"  # dd.mm.yyyy
D_LEFT = days_until(5, 10, 2025)

def main():
    clear()
    title = big("DARK")
    print(gradient(title))

    greet_lines = [
        ACCENT + BOLD + "Welcome to DARK Mode" + RESET,
        "✨ " + PALETTE[3] + "Dark Magic" + RESET + " — " + PALETTE[6] + "Calm Colors" + RESET + " — " + PALETTE[1] + "Muted Mood" + RESET,
        ACCENT + f"Your subscription expires on: {SUB_EXPIRY}" + RESET,
        (ACCENT + f"Days left: {max(D_LEFT,0)}" + RESET) if D_LEFT >= 0 else (ACCENT + "Subscription has expired." + RESET),
    ]
    print(boxify(greet_lines))
    print()
    print(dark_divider("WELCOME"))
    print()
    msg = "Enjoy the dark vibes and stay productive!"
    print(gradient(msg))
    print()

    # Minimal animation (no hidden names/vars)
    sys.stdout.write(DIM + BOX_FG + "Loading DARK theme: " + RESET)
    sys.stdout.flush()
    for j in range(8):
        sys.stdout.write(PALETTE[j % len(PALETTE)] + "⬤" + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # اطبع خطأ جميل بدل تتبع طويل
        print("\n" + BOX_FG + "[!] An error occurred: " + RESET + str(e))
        # إعادة ضبط الألوان دائمًا
        print(RESET, end="")
