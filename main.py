import curses
from curses import wrapper
from Player import Player


def main(stdscr):
    player = Player(5, 100)

    stdscr.clear()
    stdscr.refresh()

    player_pad = curses.newpad(50, 5)
    player_pad.addstr(player.y, 0, player)
    stdscr.addstr(player.y, 0, player)

    while True:
        #Make sure wrong input will come out as None
        try: 
            key = stdscr.getkey()
        except: 
            key = None

        if key == "KEY_UP":
            player.move(-1)
        elif key == "KEY_DOWN":
            player.move(1)

        # player_pad.clear()
        # player_pad.refresh(0, 0, player.y, 0, player.height - 1 + player.y, player.width)
        stdscr.clear()
        stdscr.addstr(player.y, 0, player)
        stdscr.refresh()

    stdscr.getch()


wrapper(main)