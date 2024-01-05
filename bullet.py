from imagerect import ImageRect


class Bullet:
    def __init__(self, bullettype):
        self.bullettype = bullettype
        self.rect = ImageRect(bullettype + ".png")
        self.rect.set_rect_offset(0.4, 0.4) # center tiny htibox
        self.rect.set_rect_scale(0.2, 0.2)
        self.size = self.rect.size

        # this is the center of the bullet
        # remember that for later logic to place this -size/2
        self.x = 0
        self.y = 0
        self.velocity = (0, 0)
        self.rotation = 0
        self.rot_velocity = 0
        self.destroy_callback = None

    def set_velocity(self, x, y):
        self.velocity = (x, y)

    def set_rotation(self, rot):
        self.rotation = rot
        self.rect.rotate(self.rotation)

    def set_rot_velocity(self, rot_velo):
        self.rot_velocity = rot_velo

    def set_size(self, x, y):
        self.size = (x, y)
        self.rect.resize(x, y)

    def set_destroy_callback(self, f):
        self.destroy_callback = f

    def destroy(self):
        self.destroy_callback()

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.moveto(self.x - self.size[0] / 2, self.y - self.size[1] / 2)

    def step(self, delta):
        self.x += self.velocity[0]*delta
        self.y += self.velocity[1]*delta
        self.rotation += self.rot_velocity*delta
        self.rect.rotate(self.rotation)
        self.rect.moveto(self.x - self.size[0]/2, self.y - self.size[1]/2)
