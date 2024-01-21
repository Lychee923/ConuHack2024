import curses
import subprocess
import time
import random
from curses import wrapper

from Zombie import Zombie
from Player import Player
from Bullet import Bullet

MARK = "====================                    "

grass = "\" \" , \" , \' \'    ,    \"          \" \" , \" , \'\' \"  ,    \"        \"        "

HYPPER_BULLETS = "●"
AMMO = 5


def start_screen(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()

    subprocess.run("./highscore.sh", shell=True, check=True, stdout=subprocess.PIPE, text=True)

    stdscr.clear()
    stdscr.addstr(int(screen_height / 2) - 2, int(screen_width / 2) - 15, "[ n+-- ")
    stdscr.addstr(int(screen_height / 2) - 2, int(screen_width / 2) - 8, "TERMINAL ASSAULT", curses.A_BOLD)
    stdscr.addstr(int(screen_height / 2) - 2, int(screen_width / 2) + 9, "_&_& ]")

    stdscr.addstr(int(screen_height / 2) - 1, int(screen_width / 2) - 1, ">_")
    stdscr.addstr(int(screen_height / 2) + 1, int(screen_width / 2) - 9, "Press 'p' to Start")
    stdscr.refresh()
    key = stdscr.getkey()
    if key == "p":
        play(stdscr)
    elif key == "q":
        exit(0)
    else:
        start_screen(stdscr)


def death_screen(stdscr, score, highscore):
    screen_height, screen_width = stdscr.getmaxyx()
    stdscr.clear()

    stdscr.addstr(int(screen_height / 2) - 4, int(screen_width / 2) - 5, f"GAME OVER!", curses.A_BOLD)
    stdscr.addstr(int(screen_height / 2) - 3, int(screen_width / 2) - int(len(f"Highscore: {highscore}") / 2),
                  f"Highscore: {highscore}")
    stdscr.addstr(int(screen_height / 2) - 2, int(screen_width / 2) - int(len(f"Score: {score}") / 2),
                  f"Score: {score}")

    stdscr.addstr(int(screen_height / 2), int(screen_width / 2) - 5, f"Restart (r)")
    stdscr.addstr(int(screen_height / 2) + 1, int(screen_width / 2) - 4, f"Quit (q)")
    stdscr.refresh()
    stdscr.nodelay(False)
    key = stdscr.getkey()

    if key == "r":
        play(stdscr)
    elif key == "q":
        exit(0)
    else:
        death_screen(stdscr, score, highscore)


def play(stdscr):
    screen_height, screen_width = stdscr.getmaxyx()
    player = Player(5, 5)
    hp = player.hp

    environment_counter = 0

    bullets = []
    zombies = []

    spawnrate = 10

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
                if bullet_counter >= AMMO - 1:
                    bullets.append(Bullet(player.width + 1, player.y + 1, 1, True))

                else:
                    bullets.append(Bullet(player.width + 1, player.y + 1, 1))
                bullet_counter += 1

        if key == "q":  # exit program
            exit(0)

        for bullet in bullets:
            # Hyper bullet speed
            if bullet.hyper:
                bullet.speed = 2
            else:
                bullet.speed = 1

            if bullet.x < screen_width - 5:
                bullet.move()
            else:
                bullets.remove(bullet)

        if bullet_counter >= AMMO:
            fire = False
            reload_timer += 1

            if reload_timer >= AMMO * 2:
                bullet_counter = 0
                fire = True
        else:
            reload_timer = 0

        if not gameover:
            for zombie in zombies:
                if zombie.x > 3:
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

        if not gameover and counter >= spawnrate:
            zombies.append(Zombie(screen_width - 5, random.randrange(5, screen_height - 6)))
            counter = 0

        stdscr.clear()
        environment_counter += 1

        for i in range(1, screen_width):
            stdscr.addstr(3, i, "_")
            stdscr.addstr(screen_height - 4, i, "_")

        player.update_stance()
        stdscr.addstr(player.y, 0, player.stance)

        for i in range(screen_width):
            if (player.y == laneMarkY or player.y + 1 == laneMarkY or player.y + 2 == laneMarkY) and i <= 3:
                continue
            stdscr.addstr(laneMarkY, i, MARK[(i + environment_counter // 2) % 40])

        for i in range(2, screen_width - 2):
            stdscr.addstr(2, i, grass[(i + environment_counter // 2) % 72])

        if not gameover:
            for zombie in zombies:
                zombie.update_body()
                stdscr.addstr(zombie.y, zombie.x, zombie.face)
                stdscr.addstr(zombie.y + 1, zombie.x, zombie.leg)

        # Change spawn rate
        if environment_counter >= 100 and spawnrate == 10:
            spawnrate -= 2
        if environment_counter >= 200 and spawnrate == 8:
            spawnrate -= 2
        if environment_counter >= 400 and spawnrate == 6:
            spawnrate -= 1

        # Player zombie collision
        for zombie in zombies:
            if zombie.x <= player.width:
                if player.y - 1 <= zombie.y <= player.y + 2:
                    zombies.remove(zombie)
                    hp -= 1

                    if hp == 0:
                        gameover = True
                        highscore = subprocess.run("./highscore.sh", shell=True, check=True,
                                                   stdout=subprocess.PIPE, text=True).stdout

                        if points > int(highscore):
                            highscore = subprocess.run(f"./highscore.sh {points}", shell=True, check=True,
                                                       stdout=subprocess.PIPE, text=True).stdout

                        death_screen(stdscr, points, highscore)

        for bullet in bullets:
            # Hyper bullets
            if bullet.x < screen_width:
                if bullet.hyper:
                    stdscr.addstr(bullet.y, bullet.x, HYPPER_BULLETS)
                else:
                    stdscr.addstr(bullet.y, bullet.x, "-")

        # Bullets zombie collision
        for bullet in bullets:
            for zombie in zombies:
                if (zombie.x == bullet.x + 1 or zombie.x == bullet.x or zombie.x == bullet.x - 1 or zombie.x == bullet.x - 2 or zombie.x == bullet.x -3) and \
                        (zombie.y == bullet.y + 1 or zombie.y == bullet.y or zombie.y == bullet.y - 1):

                    # Hypper bullet damage
                    if bullet.hyper:
                        bullet.damage = 3
                    else:
                        bullet.damage = 1

                    zombie.take_damage(bullet.damage)
                    bullets.remove(bullet)
                    # Check if zombie dead
                    if not zombie.alive:
                        zombies.remove(zombie)
                        points += round(1 / zombie.x * 25 + 5)

        hp_string = "HP: "
        for i in range(player.hp):
            if i < hp:
                hp_string += "❤"

        bullet_string = "Bullets: "
        if reload_timer != 0 and reload_timer % 2 == 0:
            for i in range(reload_timer // 2):
                if i < 10:
                    bullet_string += "-"
                    # Hypper bullet text
                    stdscr.addstr(1, screen_width // 2 - 10, "Extra Impact!!!")
                else:
                    bullet_string += " "

        if reload_timer == AMMO * 2:
            bullet_string = "Bullets: "

        # Mag constructurer
        for i in range(AMMO - bullet_counter):
            if 0 < i < AMMO:
                bullet_string += "*"
            elif i == 0:
                bullet_string += HYPPER_BULLETS  # Add inHypper bullets indicator
            else:
                bullet_string += " "

        stdscr.addstr(screen_height - 2, 1, hp_string)
        stdscr.addstr(screen_height - 1, 1, bullet_string)
        stdscr.addstr(1, 1, f"Points: {str(points)}")

        stdscr.refresh()


wrapper(start_screen)
