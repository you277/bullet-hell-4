import pygame
import time
from bullet import Bullet
from cirno import Cirno
from game import Game

WINDOW_SIZE = (800, 600)
STARTING_LIVES = 3

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
pygame.display.set_caption("g")

screen = pygame.display.set_mode(WINDOW_SIZE)
background = pygame.transform.scale(pygame.image.load("background.png"), WINDOW_SIZE)
win_label = font.render("You Win!", True, (254, 173, 242))

title_screen = True
game_running = False
closed = False

title_labels = [
    (font.render("SPACE to start", True, (255, 255, 255)), (30, 30)),
    (font.render("WASD to move", True, (255, 255, 255)), (30, 60)),
    (font.render("LSHIFT and RSHIFT to slow", True, (255, 255, 255)), (30, 90)),
    (font.render("LCTRL and RCTRL to fast", True, (255, 255, 255)), (30, 120)),
]

while title_screen:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            title_screen = False
            game_running = True
        if event.type == pygame.QUIT:
            title_screen = False
            game_running = False
            closed = True

    screen.blit(background, (0, 0))

    for label_info in title_labels:
        screen.blit(label_info[0], label_info[1])
    pygame.display.update()

bullets = []
instances = {}


def remove_bullet(bullet):
    global bullets
    bullets.pop(bullets.index(bullet))


def create_bullet(bullet_type):
    global bullets
    new_bullet = Bullet(bullet_type)

    def die():
        remove_bullet(new_bullet)

    new_bullet.set_destroy_callback(die)
    bullets.append(new_bullet)
    return new_bullet

# game events
game_events = []
current_time = 0
game_start_timeframe = 0
game = {}

lives = STARTING_LIVES
win = False
alive = True
invincible = False

instance_num = 0


def time_frame(t):
    global game_events
    if game_start_timeframe > t:
        return [0, []]
    if len(game_events) > 0:
        existing = game_events[len(game_events) - 1]
        if existing and existing[0] == t:
            return existing[1]
    event_frame = [t, []]
    game_events.append(event_frame)
    return event_frame[1]


# create new instance at this time
def new(type_name):
    global instance_num
    instance_num += 1
    inst_name = "INSTANCE_" + str(instance_num)
    time_frame(current_time).append(["new", type_name, inst_name])
    return inst_name


# advance time pointer
def wait(wait_time):
    global current_time
    current_time += wait_time


# set velocity of bullet at this time
def set_velocity(bullet_name, velocity):
    time_frame(current_time).append(["setvelocity", bullet_name, velocity])


# set rotation of bullet at this time
def set_rotation(bullet_name, rotation):
    time_frame(current_time).append(["setrotation", bullet_name, rotation])


# set rotation velocity of bullet at this time
def set_rot_velocity(bullet_name, rot_velocity):
    time_frame(current_time).append(["setrotvelocity", bullet_name, rot_velocity])


# set position of bullet at this time
def set_position(bullet_name, position):
    time_frame(current_time).append(["setposition", bullet_name, position])


# destroy the instance named at this time
def destroy(instance_name):
    time_frame(current_time).append(["destroy", instance_name])


# set invincible
def set_invincible(bool):
    global invincible
    invincible = bool


def set_start_time(t):
    global game_start_timeframe
    game_start_timeframe = t


# set win
def win():
    time_frame(current_time).append(["win"])


game["new"] = new
game["wait"] = wait
game["set_velocity"] = set_velocity
game["set_rotation"] = set_rotation
game["set_rot_velocity"] = set_rot_velocity
game["set_position"] = set_position
game["destroy"] = destroy
game["set_invincible"] = set_invincible
game["set_start_time"] = set_start_time
game["win"] = win

Game(game)()

char_x = 100
char_y = 100
cirno = Cirno(char_x, char_y)

score_label = font.render("score: 0", True, (255, 255, 255))
score = 0
hi_score = 0
elapsed = 0
invincibility_timer = 0

# run the game
last = time.time()
move_up = False
move_left = False
move_right = False
move_down = False

while not closed:
    if not closed:
        # cirno.place_cirno_at(char_x, char_y)

        # if event[1] in instances:
        #     instances[event[1]].destroy()

        # game_events = []
        # Game(game)()

        # last = time.time()
        # start_time = time.time()
        last = time.time()
        while game_running:
            screen.blit(background, (0, 0))

            current_time = time.time()
            delta = current_time - last
            last = current_time

            for event in pygame.event.get():
                # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #     game_running = True
                if event.type == pygame.QUIT:
                    game_running = False
                    closed = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    move_up = True
                else:
                    move_up = False
                if keys[pygame.K_a]:
                    move_left = True
                else:
                    move_left = False
                if keys[pygame.K_s]:
                    move_down = True
                else:
                    move_down = False
                if keys[pygame.K_d]:
                    move_right = True
                else:
                    move_right = False
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    cirno.set_speed_mult(0.5)
                elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                    cirno.set_speed_mult(2)
                else:
                    cirno.set_speed_mult(1)

            if move_up:
                cirno.move_cirno("up", delta)
            if move_left:
                cirno.move_cirno("left", delta)
            if move_down:
                cirno.move_cirno("down", delta)
            if move_right:
                cirno.move_cirno("right", delta)

            elapsed += delta
            if len(game_events) > 0:
                event_frame = game_events[0]
                if elapsed >= event_frame[0] - game_start_timeframe:
                    game_events.pop(0)
                    for event in event_frame[1]:
                        event_type = event[0]
                        if event_type == "new":
                            thing = None
                            t, name = event[1], event[2]
                            if t == "bullet1":
                                thing = create_bullet("bullet1")
                            elif t == "bullet2":
                                thing = create_bullet("bullet2")
                            elif t == "bullet3":
                                thing = create_bullet("bullet3")
                            elif t == "player":
                                ...
                            elif t == "boss":
                                ...
                            if thing:
                                instances[name] = thing

                        elif event_type == "setvelocity":
                            if event[1] in instances:
                                instances[event[1]].set_velocity(event[2][0], event[2][1])

                        elif event_type == "setrotation":
                            if event[1] in instances:
                                instances[event[1]].set_rotation(event[2])

                        elif event_type == "setrotvelocity":
                            if event[1] in instances:
                                instances[event[1]].set_rot_velocity(event[2])

                        elif event_type == "setposition":
                            if event[1] in instances:
                                instances[event[1]].set_position(event[2][0], event[2][1])

                        elif event_type == "destroy":
                            if event[1] in instances:
                                instances[event[1]].destroy()


                        elif event_type == "win":
                            win = True
                            game_running = False

            score_label = font.render("score: " + str(round(score)), True, (255, 255, 255))
            hi_score_label = font.render("hi score: " + str(round(hi_score)), True, (255, 255, 255))
            lives_labels = font.render("lives: " + str(lives), True, (255, 255, 255))
            screen.blit(score_label, (800 - score_label.get_width() - 5, 5))
            screen.blit(hi_score_label, (800 - hi_score_label.get_width() - 5, 30))
            screen.blit(lives_labels, (800 - lives_labels.get_width() - 5, 55))

            for bullet in bullets:
                bullet.step(delta)
                screen.blit(bullet.rect.image, (bullet.x - bullet.rect.image_size[0] / 2, bullet.y - bullet.rect.image_size[1] / 2))

            if invincibility_timer > 0:
                invincibility_timer -= delta
                label = font.render("INVINCIBILITY: " + str(round(invincibility_timer, 2)), True, (255, 255, 255))
                screen.blit(label, (cirno.x + 25, cirno.y))
            else:
                score += delta * 100
                hi_score = max(hi_score, score)
                for bullet in bullets:
                    if not invincible and cirno.rect.colliderect(bullet.rect.rect):
                        game_running = False
                        win = False
                        alive = False

            # cirno.place_cirno_at(char_x, char_y)
            screen.blit(cirno.image, cirno.rect)

            pygame.display.update()

    win_labels = [
        font.render("you win", True, (255, 255, 255)),
        font.render("score: " + str(round(score)), True, (255, 255, 255)),
        font.render("hi score: " + str(round(hi_score)), True, (255, 255, 255))
    ]

    lose_labels = [
        font.render("you lose", True, (255, 255, 255)),
        font.render("score: " + str(round(score)), True, (255, 255, 255)),
        font.render("hi score: " + str(round(hi_score)), True, (255, 255, 255)),
    ]

    # print(instances)

    if not alive:
        lives -= 1
        if lives == 0:
            lose_labels.append(font.render("r to RESTART", True, (255, 255, 255)))
        else:
            lose_labels.append(font.render("r to revive", True, (255, 255, 255)))

    ending_screen_open = True
    if not closed:
        while ending_screen_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closed = True
                    ending_screen_open = False
                elif event.type == pygame.KEYDOWN:
                    if not alive and event.key == pygame.K_r:
                        game_running = True
                        win = False
                        alive = True
                        ending_screen_open = False
                        if lives == 0:
                            for instname in enumerate(instances):
                                instances[instname[1]].destroy()

                            instance_num = 0
                            instances = {}
                            game_events = []
                            elapsed = 0
                            hi_score = 0

                            # Game(game)()
                            #print(game_events)

                            cirno.place_cirno_at(char_x, char_y)
                            last = time.time()
                            current_time = 0
                            lives = STARTING_LIVES

                            Game(game)()
                        else:
                            invincibility_timer = 1
                        score = 0

            labels = None
            if win:
                labels = win_labels
            else:
                labels = lose_labels

            screen.blit(background, (0, 0))

            for bullet in bullets:
                # bullet.step(delta)
                screen.blit(bullet.rect.image, (bullet.x - bullet.rect.image_size[0]/2, bullet.y - bullet.rect.image_size[1]/2))

            for i in range(len(labels)):
                label = labels[i]
                screen.blit(label, (400 - label.get_width()/2, 200 + i * 25))
            pygame.display.update()
