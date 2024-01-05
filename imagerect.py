import pygame


class ImageRect:
    def __init__(self, img):
        self.orig_image = pygame.image.load(img)
        self.image = self.orig_image
        self.x = 0
        self.y = 0
        self.size = self.image.get_size()
        self.image_size = self.size
        self.rect_offset = (0, 0)
        self.rect_scale = (1, 1)
        self.rotation = 0
        self.rect = None
        self.create_rect()

    def create_rect(self):
        self.rect = pygame.Rect(
            self.x + self.rect_offset[0]*self.size[0],
            self.y + self.rect_offset[1]*self.size[1],
            self.size[0]*self.rect_scale[0],
            self.size[1]*self.rect_scale[1]
        )

    def moveto(self, x, y):
        self.x = x
        self.y = y
        self.create_rect()

    def resize(self, x, y):
        self.size = (x, y)
        self.image = pygame.transform.scale(self.orig_image, self.size)
        self.image_size = self.image.get_size()
        self.create_rect()

    def set_rect_offset(self, x, y):
        self.rect_offset = (x, y)
        self.create_rect()

    def set_rect_scale(self, x, y):
        self.rect_scale = (x, y)
        self.create_rect()

    def rotate(self, deg):
        self.rotation = deg
        self.image = pygame.transform.rotate(self.orig_image, deg)
        self.image_size = self.image.get_size()
        # self.create_rect()
