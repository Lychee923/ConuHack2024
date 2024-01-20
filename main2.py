import curses
import random

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    player = '0'
    px, py = sh // 2, sw // 2
    w.addch(px, py, player)

    zombies = []
    bullets = []

    while True:
        key = w.getch()
        if key == ord('q'):
            break
        elif key == ord(' '):
            bullets.append([px - 1, py])
        
        # Move player
        if key == curses.KEY_UP and px > 0:
            px -= 1
        elif key == curses.KEY_DOWN and px < sh - 1:
            px += 1
        elif key == curses.KEY_LEFT and py > 0:
            py -= 1
        elif key == curses.KEY_RIGHT and py < sw - 1:
            py += 1

        # Move bullets
        new_bullets = []
        for bullet in bullets:
            if bullet[0] > 0:
                bullet[0] -= 1
                new_bullets.append(bullet)
        bullets = new_bullets

        # Spawn zombies
        if random.randint(1, 10) == 1:
            zombies.append([random.randint(0, sh - 1), sw - 1])

        # Move zombies
        new_zombies = []
        for zombie in zombies:
            if zombie[1] > 0:
                zombie[1] -= 1
                new_zombies.append(zombie)
        zombies = new_zombies

        # Check collisions
        for bullet in bullets:
            for zombie in zombies:
                if bullet == zombie:
                    zombies.remove(zombie)
                    bullets.remove(bullet)

        for zombie in zombies:
            if zombie == [px, py]:
                stdscr.addstr(sh // 2, sw // 2 - 5, "Game Over!")
                stdscr.refresh()
                stdscr.getch()
                return

        # Clear screen
        w.clear()

        # Draw player
        w.addch(px, py, player)

        # Draw bullets
        for bullet in bullets:
            w.addch(bullet[0], bullet[1], '|')

        # Draw zombies
        for zombie in zombies:
            w.addch(zombie[0], zombie[1], 'Z')

        # Refresh screen
        w.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
