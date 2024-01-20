import curses
import time
from curses import wrapper
from Player import Player
from Bullet import Bullet

bullets = []


def main(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    player = Player(5, 100)

    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(player.y, 0, player.get_stance())
    stdscr.nodelay(True)

    while True:
        # Make sure wrong input will come out as None
        try: 
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_UP" and player.y > 0:
            player.y -= 1
            # player.change_stance()
        elif key == "KEY_DOWN" and player.y + player.height < screen_height:
            player.y += 1
            # player.change_stance()
        elif key == " ":
            bullets.append(Bullet(player.width + 1, player.y + 1, 1))
        elif key == "p":    # exit program
            player.y += 10000

        for bullet in bullets:
            if bullet.x < screen_width - 1:
                bullet.move()
            else:
                bullets.remove(bullet)

        time.sleep(0.05)

        stdscr.clear()

        stdscr.addstr(player.y, 0, player.get_stance())
        for bullet in bullets:
            stdscr.addstr(bullet.y, bullet.x, "-")

        stdscr.refresh()

    stdscr.getch()


wrapper(main)
