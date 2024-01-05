import math
import random


def Game(game):
    # game functions
    new = game["new"]
    wait = game["wait"]

    set_rotation = game["set_rotation"]
    set_velocity = game["set_velocity"]
    set_rot_velocity = game["set_rot_velocity"]
    set_position = game["set_position"]
    destroy = game["destroy"]
    set_invincible = game["set_invincible"]
    set_start_time = game["set_start_time"]
    win = game["win"]

    # util functions

    def circle_coords(deg):
        deg = math.radians(deg)
        return (math.cos(deg), math.sin(deg))

    def run_game():
        set_invincible(False)
        set_start_time(0)

        b1 = new("bullet1")
        set_velocity(b1, (800, 800))
        set_rotation(b1, 20)

        wait(0.5)
        circle1_circles = []
        for i in range(5):
            our_circle = []
            for v in range(10):
                circle = circle_coords(360 / 10 * v + 360*i/5)

                b2 = new("bullet2")
                set_position(b2, (400 + circle[0]*20, 300 + circle[1]*20))
                set_velocity(b2, (circle[0] * 100, circle[1] * 100))
                set_rotation(b2, 360 / 10 * v)
                our_circle.append(b2)
            circle1_circles.append(our_circle)
            wait(0.1)

        for i in range(20):
            wait(0.1)
            for circle_idx in range(5):
                this_circle = circle1_circles[circle_idx]
                mult = circle_idx%2 == 0 and -1 or 1
                for bullet_idx in range(10):
                    circle = circle_coords(360 / 10 * bullet_idx + 360 / 5 * circle_idx)
                    set_velocity(this_circle[bullet_idx], (circle[0] * 100 + i*4.5*mult, circle[1] * 100 + i*4.5*mult))

        wait(1)

        other_names = []
        for i in range(20):
            wait(0.5)
            amt = i*2
            for v in range(amt):
                circle = circle_coords(360/20*i + 360/amt*v)
                b3 = new("bullet1")
                set_position(b3, (400 - circle[0]*50, 300 - circle[1]*50))
                set_velocity(b3, (circle[0]*300, circle[1]*300))
                other_names.append(b3)

        wait(0.5)

        CIRCLE_POSITIONS = [
            (200, 200),
            (600, 400),
            (200, 400),
            (600, 200),
            (400, 300)
        ]

        more_bullets = []
        for _ in range(5):
            for pos in CIRCLE_POSITIONS:
                for i in range(20):
                    circle = circle_coords(360 / 20 * i)
                    b3 = new("bullet1")
                    set_position(b3, (pos[0] + circle[0], pos[1] + circle[1] * 10))
                    set_velocity(b3, (circle[0] * 100, circle[1] * 100))
                    more_bullets.append(b3)
            wait(0.3)

        wait(5)

        even_more_bullets = []
        for i in range(2):
            for v in range(26):
                horiz_bullet = new("bullet1")
                set_position(horiz_bullet, (800/25*v, i*600))
                set_velocity(horiz_bullet, (0, 200 - i*400))
                even_more_bullets.append(horiz_bullet)
        for i in range(2):
            for v in range(21):
                vert_bullet = new("bullet1")
                set_position(vert_bullet, (i*800, 600/20*v))
                set_velocity(vert_bullet, (200 - i*400, 0))
                even_more_bullets.append(vert_bullet)

        wait(2.5)

        so_many_bullets = []
        for i in range(2):
            for v in range(60):
                circle = circle_coords(360 / 60 * v + 360/4)
                b1 = new("bullet1")
                b2 = new("bullet1")
                b3 = new("bullet1")
                b4 = new("bullet1")
                set_position(b1, (400 - circle[0], 300 - circle[1]))
                set_position(b2, (400 - circle[0] * 100, 300 - circle[1] * 100))
                set_position(b3, (400 - circle[0] * 200, 300 - circle[1] * 200))
                set_position(b4, (400 - circle[0] * 300, 300 - circle[1] * 300))
                set_velocity(b1, (300 * circle[0], 300 * circle[1]))
                set_velocity(b2, (300 * circle[0], 300 * circle[1]))
                set_velocity(b3, (300 * circle[0], 300 * circle[1]))
                set_velocity(b4, (300 * circle[0], 300 * circle[1]))
                so_many_bullets.append(b1)
                so_many_bullets.append(b2)
                so_many_bullets.append(b3)
                so_many_bullets.append(b4)

                if v % 20 == 0:
                    for v2 in range(25):
                        circle2 = circle_coords(360 / 25 * v2)
                        b5 = new("bullet1")
                        set_position(b5, (400 - circle[0] * 500 + circle2[0] * 400, 300 - circle[1] * 500 + circle2[1] * 400))
                        set_velocity(b5, (250 * circle[0], 250 * circle[1]))
                        so_many_bullets.append(b5)

                wait(0.1)

        wait(1.5)

        wave_bullets = []
        for i in range(20):
            for v2 in range(25):
                circle = circle_coords(360 / 20 * i)
                circle2 = circle_coords(360 / 25 * v2)
                b1 = new("bullet1")
                set_position(b1, (400 - circle[0] * 500 + circle2[0] * 400, 300 - circle[1] * 500 + circle2[1] * 400))
                set_velocity(b1, (250 * circle[0], 250 * circle[1]))
                wave_bullets.append(b1)

            wait(0.4)

        wait(2.5)

        all_the_bullets = []
        b1 = new("bullet1")
        set_velocity(b1, (100, 100))
        for v in range(500):
            for v2 in range(3):
                circle2 = circle_coords(360 / 60 * v + 120*v2)
                b1 = new("bullet1")
                set_position(b1, (400 + circle2[0], 300 + circle2[1]))
                set_velocity(b1, (300 * circle2[0], 300 * circle2[1]))
                all_the_bullets.append(b1)
            wait(math.cos(v))

        wait(4)
        for bullet in all_the_bullets:
            destroy(bullet)

        grid_bullets = []
        for x in range(31):
            for y in range(21):
                bullet = new("bullet1")
                set_position(bullet, (800/15 * x - 800/15, 600/10 * y - 600/10))
                grid_bullets.append(bullet)
                wait(0.002)

        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (-100, -100))
        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (100, 0))
        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (0, 100))
        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (100, 0))
        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (-100, 0))
        wait(2)
        for bullet in grid_bullets:
            set_velocity(bullet, (0, -100))

        wait(4)
        for bullet in grid_bullets:
            set_velocity(bullet, (0,0 ))
        wait(1)
        for bullet in grid_bullets:
            set_velocity(bullet, (random.randint(-100, 100), random.randint(-100, 100)))

        for circle_list in circle1_circles:
            for name in circle_list:
                destroy(name)

        for name in even_more_bullets:
            destroy(name)


        wait(3)

        for name in other_names:
            destroy(name)

        for name in so_many_bullets:
            destroy(name)

        for name in wave_bullets:
            destroy(name)


        wait(6)
        for bullet in grid_bullets:
            destroy(bullet)
            wait(0.01)

        wait(1)
        win()

    return run_game
