import curses
from curses import wrapper
from Player import Player

bullets = []


def main(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    player = Player(5, 100)

    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(player.y, 0, player.get_stance())

    while True:
        # Make sure wrong input will come out as None
        try: 
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_UP" and player.y > 0:
            player.y -= 1
        elif key == "KEY_DOWN" and player.y + player.height < screen_height:
            player.y += 1
        elif key == " ":
            bullets.append(Bullet(player.width + 1, player.y, 1))

        stdscr.clear()
        stdscr.addstr(player.y, 0, player.get_stance())
        stdscr.refresh()

    stdscr.getch()


wrapper(main)
