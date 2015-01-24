import pygame
from random import randint

DEMOSPRITE = "assets/dummy.png"
BEER_IMAGE = "assets/dummy.png"
COCKTAIL_IMAGE = "assets/dummy.png"
BOOK_IMAGE = "assets/dummy.png"
PEN_IMAGE = "assets/dummy.png"

#----------------------------------------------------------------------

class ItemSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(DEMOSPRITE)
        self.rect = self.image.get_rect()
        self.fall_speed = randint(4,8)


#----------------------------------------------------------------------

class BeerSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)

class CocktailSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)

class BookSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)

class PenSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)


