import curses
import time
import random
from curses import wrapper

from Zombie import Zombie
from Player import Player
from Bullet import Bullet


mark = "[==================]                    "


def start_screen(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(int(screen_height / 2), int(screen_width / 2) - 9, "Press 'p' to Start")
    stdscr.refresh()
    key = stdscr.getkey()
    if key == "p":
        play(stdscr)
    else:
        start_screen(stdscr)


def death_screen(stdscr, score):
    screen_height, screen_width = stdscr.getmaxyx()
    stdscr.clear()

    stdscr.addstr(int(screen_height / 2) - 3, int(screen_width / 2) - 4, f"GAME OVER")
    stdscr.addstr(int(screen_height / 2) - 2, int(screen_width / 2) - int(len(f"Score: {score}") / 2),
                  f"Score: {score}")
    stdscr.addstr(int(screen_height / 2), int(screen_width / 2) - 5, f"Restart (r)")
    stdscr.addstr(int(screen_height / 2) + 1, int(screen_width / 2) - 4, f"Quit (q)")
    stdscr.refresh()
    stdscr.nodelay(False)
    time.sleep(1)
    key = stdscr.getkey()

    if key == "r":
        play(stdscr)
    elif key == "q":
        stdscr.addstr(10000, 10000, "crash")


def play(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    player = Player(5, 5)
    hp = player.hp

    environmentCounter = 0

    bullets = []
    zombies = []

    spawnrate = 6

    gameover = False
    counter = 0
    points = 0
    counter_tree = 0
    stdscr.clear()
    stdscr.refresh()
    bullet_counter = 0
    fire = True

    reload_timer = 0

    player.update_stance()
    stdscr.addstr(player.y, 0, player.stance)
    stdscr.nodelay(True)

    laneMarkY = screen_height // 2

    while True:
        # Make sure wrong input will come out as None
        try:
            key = stdscr.getkey()
        except:
            key = None

        if not gameover:
            if key == "KEY_UP" and player.y > 4:
                player.y -= 1
            elif key == "KEY_DOWN" and player.y + player.height < screen_height - 3:
                player.y += 1
            elif key == " " and fire:

                bullets.append(Bullet(player.width + 1, player.y + 1, 1))
                bullet_counter += 1

        if key == "q":  # exit program
            player.y += 10000

        for bullet in bullets:
            if bullet.x < screen_width - 1:
                bullet.move()
            else:
                bullets.remove(bullet)

        if bullet_counter >= 10:
            fire = False
            reload_timer += 1

            if reload_timer >= 20:
                bullet_counter = 0
                fire = True
        else:
            reload_timer = 0

        if not gameover:
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
            counter_tree += 1
            for zombie in zombies:
                zombie.counter += 1

        if not gameover:
            if counter == spawnrate:
                zombies.append(Zombie(screen_width - 5, random.randrange(5, screen_height - 6)))

                counter = 0

        stdscr.clear()
        environmentCounter += 1
        for i in range(screen_width):
            stdscr.addstr(laneMarkY, i, mark[(i+environmentCounter//2) % 40])

        for i in range(1, screen_width):
            stdscr.addstr(3, i, "_")
            stdscr.addstr(screen_height - 4, i, "_")

        player.update_stance()
        stdscr.addstr(player.y, 0, player.stance)
        for zombie in zombies:
            zombie.update_leg()
            stdscr.addstr(zombie.y, zombie.x, zombie.big_face)
            stdscr.addstr(zombie.y + 1, zombie.x, zombie.leg)

        for zombie in zombies:
            if zombie.x <= player.width:
                if player.y - 1 <= zombie.y <= player.y + 2:
                    zombies.remove(zombie)
                    hp -= 1

                    if hp == 0:
                        gameover = True
                        death_screen(stdscr, points)

        for bullet in bullets:
            stdscr.addstr(bullet.y, bullet.x, "-")

        # Bullets zombie collision
        for bullet in bullets:
            for zombie in zombies:
                if zombie.x == bullet.x + 1 or zombie.x == bullet.x or zombie.x == bullet.x - 1:
                    if zombie.y == bullet.y + 1 or zombie.y == bullet.y or zombie.y == bullet.y - 1:
                        bullets.remove(bullet)
                        zombie.hp -= 1
                        if zombie.hp == 0:
                            zombies.remove(zombie)
                            points += round(1 / zombie.x * 25 + 5)

        hp_string = "HP: "
        for i in range(player.hp):
            if i < hp:
                hp_string += "▩"
            else:
                hp_string += "▢"

        bullet_string = "Bullets: "
        if reload_timer != 0 and reload_timer % 2 == 0:
            for i in range(reload_timer // 2):
                if i < 10:
                    bullet_string += "-"
                else:
                    bullet_string += " "

        if reload_timer == 20:
            bullet_string = "Bullets: "

        for i in range(10 - bullet_counter):
            if i < 10:
                bullet_string += "|"
            else:
                bullet_string += " "

        stdscr.addstr(screen_height - 2, 1, hp_string)
        stdscr.addstr(screen_height - 1, 1, bullet_string)
        stdscr.addstr(screen_height - 1, screen_width - len(str(points)) - 10, f"Points: {str(points)}")

        stdscr.refresh()


wrapper(start_screen)
