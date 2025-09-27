# -*- coding: utf-8 -*-
# DARK Greeting (auto clear after 3s)

_y = None; _Y = None
import os, sys, time, datetime, argparse, re

RESET = "\033[0m"; BOLD="\033[1m"; DIM="\033[2m"
PALETTE=["\033[38;5;240m","\033[38;5;241m","\033[38;5;242m",
         "\033[38;5;60m","\033[38;5;61m","\033[38;5;62m",
         "\033[38;5;44m","\033[38;5;45m","\033[38;5;37m"]
BOX_FG="\033[38;5;246m"; ACCENT="\033[38;5;135m"

def _big(text):
    try:
        import pyfiglet
        return pyfiglet.figlet_format(text, font="slant")
    except Exception:
        bar="═"*(len(text)+6)
        return f"╔{bar}╗\n║   {text}   ║\n╚{bar}╝"

def _strip(s): return re.sub(r"\x1b\[[0-9;]*m","",s)
def _grad(text,p=PALETTE):
    out=[]; n=len(p); i=0
    for ch in text:
        if ch=="\n": out.append(ch); i=0
        else: out.append(p[i % n]+ch+RESET); i+=1
    return "".join(out)

def _box(lines):
    w=max(len(_strip(s)) for s in lines)
    top=BOX_FG+"┏"+"━"*(w+2)+"┓"+RESET
    bot=BOX_FG+"┗"+"━"*(w+2)+"┛"+RESET
    b=[]
    for s in lines:
        pad=" "*(w-len(_strip(s)))
        b.append(BOX_FG+"┃ "+RESET+s+pad+BOX_FG+" ┃"+RESET)
    return "\n".join([top,*b,bot])

def _divider(txt="WELCOME"):
    core=f"  {txt}  "; line="─"*12
    return f"{DIM}{BOX_FG}{line}{RESET}{ACCENT}{core}{RESET}{DIM}{BOX_FG}{line}{RESET}"

def _clear(): os.system("cls" if os.name=="nt" else "clear")
def _parse_exp(s):
    for fmt in ("%d.%m.%Y","%Y-%m-%d"):
        try: return datetime.datetime.strptime(s,fmt).date()
        except: pass
    return datetime.date(2025,10,5)

def _days_left(d): return (d-datetime.date.today()).days

def dark_greet(exp="05.10.2025"):
    expiry=_parse_exp(exp); left=_days_left(expiry)
    _clear()
    print(_grad(_big("DARK")))
    lines=[ACCENT+BOLD+"Welcome to DARK Mode"+RESET,
           "✨ "+PALETTE[3]+"Dark Magic"+RESET+" — "+PALETTE[6]+"Calm Colors"+RESET+" — "+PALETTE[1]+"Muted Mood"+RESET,
           ACCENT+f"Your subscription expires on: {exp}"+RESET,
           ACCENT+(f"Days left: {max(left,0)}" if left>=0 else "Subscription has expired.")+RESET]
    print(_box(lines)); print(); print(_divider("WELCOME")); print()
    print(_grad("Enjoy the dark vibes and stay productive!")); print()
    sys.stdout.write(DIM+BOX_FG+"Loading DARK theme: "+RESET); sys.stdout.flush()
    for j in range(8):
        sys.stdout.write(PALETTE[j%len(PALETTE)]+"⬤"+RESET); sys.stdout.flush(); time.sleep(0.08)
    print("\n")
    # انتظر 3 ثواني ثم امسح الشاشة
    time.sleep(3)
    _clear()

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--expiry",default="05.10.2025",help="Expiry date dd.mm.yyyy or yyyy-mm-dd")
    args=ap.parse_args()
    try: dark_greet(args.expiry)
    finally: print(RESET,end="")
