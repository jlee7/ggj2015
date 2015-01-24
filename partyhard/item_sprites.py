import pygame

DEMOSPRITE = "assets/dummy.png"


#----------------------------------------------------------------------

class ItemSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(DEMOSPRITE)
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.fall_speed = 5

#----------------------------------------------------------------------

class BeerSprite(ItemSprite):
    def __init__(self, beer_model):
        pass
