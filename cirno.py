import pygame


class Cirno:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["cirnoright.png", "cirnoleft.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.rescale_image(self.image)
        self.speed = 250
        self.speedmult = 1

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        self.image_size = scale_size
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def set_speed_mult(self, mult):
        self.speedmult = mult

    def move_cirno(self, d, delta):
        x = self.x
        y = self.y
        move_dist = self.speed * self.speedmult * delta
        if d == "down":
            y += move_dist
        elif d == "up":
            y -= move_dist
        elif d == "left":
            x -= move_dist
            image = self.image_list[1]
            self.image = pygame.image.load(image)
            self.rescale_image(self.image)

        elif d == "right":
            x += move_dist
            image = self.image_list[0]
            self.image = pygame.image.load(image)
            self.rescale_image(self.image)

        x = min(max(x, 0), 800 - self.image_size[0])
        y = min(max(y, 0), 600 - self.image_size[1])
        self.x = x
        self.y = y
        #  print(x, y)

        self.rect = pygame.Rect(x, y, self.image_size[0], self.image_size[1])

    def place_cirno_at(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])