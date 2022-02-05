import pygame

# Loads image
def load_image(path):
    return pygame.image.load(path)

# Scales image
def scale_image(img, width=None, height=None):
    return pygame.transform.scale(img, (width, height))

# Flip the image horizontally
def flip_image(img):
    return pygame.transform.flip(img, False, True)

# Detects if collision has occured
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    if obj1.image_rect.colliderect(obj2.image_rect):
        return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None
    else:
        return False

