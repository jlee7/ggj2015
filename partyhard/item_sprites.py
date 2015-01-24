import pygame
from random import randint


DEMOSPRITE = "assets/item-book.png"
BEER_IMAGE = "assets/dummy.png"
COCKTAIL_IMAGE = "assets/dummy.png"
BOOK_IMAGE = "assets/item-book.png"
PEN_IMAGE = "assets/dummy.png"

#----------------------------------------------------------------------

class ItemSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(DEMOSPRITE)
        #self.rect = self.image.get_rect()
        self.fall_speed = randint(4,8)


#----------------------------------------------------------------------

class BeerSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)
        self.image = pygame.image.load(BEER_IMAGE)
        self.rect = self.image.get_rect()

class CocktailSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)
        self.image = pygame.image.load(COCKTAIL_IMAGE)
        self.rect = self.image.get_rect()

class BookSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)
        self.image = pygame.image.load(BOOK_IMAGE)
        self.rect = self.image.get_rect()

class PenSprite(ItemSprite):
    def __init__(self, model):
        ItemSprite.__init__(self)
        self.image = pygame.image.load(PEN_IMAGE)
        self.rect = self.image.get_rect()

