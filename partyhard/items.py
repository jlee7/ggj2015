import pygame

DEMOSPRITE = "assets/dummy.png"

class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(DEMOSPRITE)
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.fall_speed = 5

class Beer(Item):
    def __init__(self):
        Item.__init__()
