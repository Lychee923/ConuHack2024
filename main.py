import curses
import time
import random
from curses import wrapper

from Zombie import Zombie
from Player import Player
from Bullet import Bullet

bullets = []
zombies = []

spawnrate = 6


def main(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    player = Player(5, 5)
    hp = player.hp

    gameover = False
    counter = 0
    points = 0
    counterTree = 0
    stdscr.clear()
    stdscr.refresh()
    bulletCounter = 0
    Fire = True

    reloadTimer = 0

    player.update_stance()
    stdscr.addstr(player.y, 0, player.stance)
    stdscr.nodelay(True)

    while True:
        # Make sure wrong input will come out as None
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_UP" and player.y > 0:
            player.y -= 1
        elif key == "KEY_DOWN" and player.y + player.height < screen_height - 2:
            player.y += 1
            # player.change_stance()
        elif key == " " and Fire:

            bullets.append(Bullet(player.width + 1, player.y + 1, 1))
            bulletCounter += 1

        elif key == "p":  # exit program
            player.y += 10000

        for bullet in bullets:
            if bullet.x < screen_width - 1:
                bullet.move()
            else:
                bullets.remove(bullet)

        if (bulletCounter > 12):
            Fire = False
            reloadTimer += 1
            if reloadTimer >= 40:
                bulletCounter = 0
                Fire = True
        else:
            reloadTimer = 0


        for zombie in zombies:
            if zombie.x > 0:
                zombie.move("LEFT")
                if player.y > zombie.y and zombie.counter >= random.randrange(10, 40):
                    zombie.move("UP")
                    zombie.counter = 0
                elif player.y < zombie.y and zombie.counter >= random.randrange(10, 40):
                    zombie.move("DOWN")
                    zombie.counter = 0
            else:
                zombies.remove(zombie)

        time.sleep(0.05)
        if random.getrandbits(1):
            counter += 1
            counterTree += 1
            for zombie in zombies:
                zombie.counter += 1

        if counter == spawnrate:
            zombies.append(Zombie(screen_width - 2, random.randrange(1, screen_height - 5)))
            counter = 0

        stdscr.clear()

        player.update_stance()
        stdscr.addstr(player.y, 0, player.stance)
        for zombie in zombies:
            zombie.update_leg()
            stdscr.addstr(zombie.y, zombie.x, zombie.face)
            stdscr.addstr(zombie.y + 1, zombie.x, zombie.leg)

        for zombie in zombies:
            if zombie.x == player.width:
                if zombie.y == player.y + 1 or zombie.y == player.y or zombie.y == player.y - 1:
                    zombies.remove(zombie)
                    hp -= 1

                    if hp == 0:
                        gameover = True

        for bullet in bullets:
            stdscr.addstr(bullet.y, bullet.x, "-")

        for bullet in bullets:
            for zombie in zombies:
                if zombie.x == bullet.x + 1 or zombie.x == bullet.x or zombie.x == bullet.x - 1:
                    if zombie.y == bullet.y + 1 or zombie.y == bullet.y or zombie.y == bullet.y - 1:
                        bullets.remove(bullet)
                        zombies.remove(zombie)
                        points += round(1 / zombie.x * 25 + 5)

        hp_string = "HP: "
        for i in range(player.hp):
            if i < hp:
                hp_string += "▩"
            else:
                hp_string += "▢"

        stdscr.addstr(screen_height - 1, 1, hp_string)
        stdscr.addstr(screen_height - 1, screen_width - len(str(points)) - 10, f"Points: {str(points)}")

        stdscr.refresh()


wrapper(main)
