# -*- coding: utf-8 -*-
"""
DARK greeting module — importable and runnable as a script.
Usage:
  python dark_greet.py --expiry 05.10.2025
  # or import and call: from dark_greet import dark_greet; dark_greet("05.10.2025")
"""

# Guard some weird globals seen on certain mobile IDEs
_y = None; _Y = None

import os, sys, time, datetime, argparse, re

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

def _big(text: str) -> str:
    try:
        import pyfiglet
        try:
            return pyfiglet.figlet_format(text, font="slant")
        except Exception:
            return pyfiglet.figlet_format(text)
    except Exception:
        bar = "═" * (len(text) + 6)
        return f"╔{bar}╗\n║   {text}   ║\n╚{bar}╝"

def _strip_ansi(s: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", s)

def _gradient(text: str, palette=PALETTE) -> str:
    if not text:
        return text
    out, n, i = [], len(palette), 0
    for ch in text:
        if ch == "\n":
            out.append(ch); i = 0
        else:
            out.append(palette[i % n] + ch + RESET); i += 1
    return "".join(out)

def _box(lines):
    width = max(len(_strip_ansi(s)) for s in lines) if lines else 0
    top = BOX_FG + "┏" + "━" * (width + 2) + "┓" + RESET
    bot = BOX_FG + "┗" + "━" * (width + 2) + "┛" + RESET
    body = []
    for s in lines:
        pad = " " * (width - len(_strip_ansi(s)))
        body.append(BOX_FG + "┃ " + RESET + s + pad + BOX_FG + " ┃" + RESET)
    return "\n".join([top, *body, bot])

def _divider(text="WELCOME"):
    core = f"  {text}  "
    line = "─" * 12
    return f"{DIM}{BOX_FG}{line}{RESET}{ACCENT}{core}{RESET}{DIM}{BOX_FG}{line}{RESET}"

def _clear():
    try: os.system("cls" if os.name == "nt" else "clear")
    except Exception: pass

def _parse_expiry(s: str) -> datetime.date:
    """
    Accepts dd.mm.yyyy or yyyy-mm-dd
    """
    s = s.strip()
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except Exception:
            pass
    raise ValueError("Invalid expiry format. Use dd.mm.yyyy or yyyy-mm-dd")

def _days_until(date_obj: datetime.date) -> int:
    return (date_obj - datetime.date.today()).days

def dark_greet(expiry_str: str = "05.10.2025") -> None:
    """
    Render the DARK greeting with expiry info.
    """
    try:
        expiry_date = _parse_expiry(expiry_str)
    except Exception:
        expiry_date = datetime.date(2025, 10, 5)
        expiry_str  = "05.10.2025"

    days_left = _days_until(expiry_date)

    _clear()
    print(_gradient(_big("DARK")))

    lines = [
        ACCENT + BOLD + "Welcome to DARK Mode" + RESET,
        "✨ " + PALETTE[3] + "Dark Magic" + RESET + " — " + PALETTE[6] + "Calm Colors" + RESET + " — " + PALETTE[1] + "Muted Mood" + RESET,
        ACCENT + f"Your subscription expires on: {expiry_str}" + RESET,
        (ACCENT + f"Days left: {max(days_left,0)}" + RESET) if days_left >= 0 else (ACCENT + "Subscription has expired." + RESET),
    ]
    print(_box(lines))
    print()
    print(_divider("WELCOME"))
    print()
    print(_gradient("Enjoy the dark vibes and stay productive!"))
    print()

    sys.stdout.write(DIM + BOX_FG + "Loading DARK theme: " + RESET)
    sys.stdout.flush()
    for j in range(8):
        sys.stdout.write(PALETTE[j % len(PALETTE)] + "⬤" + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DARK Greeting")
    parser.add_argument("--expiry", default="05.10.2025",
                        help="Expiry date (dd.mm.yyyy or yyyy-mm-dd). Default: 05.10.2025")
    args = parser.parse_args()
    try:
        dark_greet(args.expiry)
    finally:
        print(RESET, end="")
