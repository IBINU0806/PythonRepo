import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello VietNam")
    stdscr.refesh()
    stdscr.getkey()
    
wrapper(main)