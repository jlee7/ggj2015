import pygame
from random import randint


DEMOSPRITE = "assets/item-book.png"
BEER_IMAGE = "assets/item-six-pack.png"
BEER_IMAGE_GREEN = "assets/item-six-pack_green.png"
BEER_IMAGE_RED = "assets/item-six-pack_red.png"
COCKTAIL_IMAGE = "assets/item-cocktail.png"
COCKTAIL_IMAGE_GREEN = "assets/item-cocktail_green.png"
COCKTAIL_IMAGE_RED = "assets/item-cocktail_red.png"
BOOK_IMAGE = "assets/item-book.png"
BOOK_IMAGE_GREEN = "assets/item-book_green.png"
BOOK_IMAGE_RED = "assets/item-book_red.png"
LAPTOP_IMAGE = "assets/item-laptop.png"
LAPTOP_IMAGE_GREEN = "assets/item-laptop_green.png"
LAPTOP_IMAGE_RED = "assets/item-laptop_red.png"
POINT_PLUS_IMAGE = "assets/score_plus.png"
POINT_MINUS_IMAGE = "assets/score_minus.png"
KILL_TIME = 5

#----------------------------------------------------------------------

class ItemSprite(pygame.sprite.Sprite):

    def __init__(self, model):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(DEMOSPRITE)
        #self.rect = self.image.get_rect()
        self.fall_speed = randint(4,8)
        self.item_model = model
        self.collided = False
        self.kill_time = KILL_TIME

    def update(self, partytime):
        if (not self.collided
            and (partytime == True and self.item_model.partytime == True) 
            or (partytime == False and self.item_model.partytime == False)):
            self.set_positiv()
        else:
            self.set_negativ()

    def set_positiv(self):
        pass
    def set_negativ(self):
        pass

    def collide(self, partytime):
        if ((partytime == True and self.item_model.partytime == True) 
            or (partytime == False and self.item_model.partytime == False)):
            self.image = pygame.image.load(POINT_PLUS_IMAGE)
        else:
            self.image = pygame.image.load(POINT_MINUS_IMAGE)
        self.collided = True

    def kill_try(self):
        self.kill_time -=1
        if self.kill_time == 0:
            self.kill()


#----------------------------------------------------------------------

class BeerSprite(ItemSprite):
    def __init__(self, model, partytime):
        ItemSprite.__init__(self, model)
        self.update(partytime)
        self.rect = self.image.get_rect()
    def set_positiv(self):
        self.image = pygame.image.load(BEER_IMAGE_GREEN)
    def set_negativ(self):
        self.image = pygame.image.load(BEER_IMAGE_RED)

class CocktailSprite(ItemSprite):
    def __init__(self, model, partytime):
        ItemSprite.__init__(self, model)
        self.update(partytime)
        self.rect = self.image.get_rect()
    def set_positiv(self):
        self.image = pygame.image.load(COCKTAIL_IMAGE_GREEN)
    def set_negativ(self):
        self.image = pygame.image.load(COCKTAIL_IMAGE_RED)

class BookSprite(ItemSprite):
    def __init__(self, model, partytime):
        ItemSprite.__init__(self, model)
        self.update(partytime)
        self.rect = self.image.get_rect()
    def set_positiv(self):
        self.image = pygame.image.load(BOOK_IMAGE_GREEN)
    def set_negativ(self):
        self.image = pygame.image.load(BOOK_IMAGE_RED)

class PenSprite(ItemSprite):
    def __init__(self, model, partytime):
        ItemSprite.__init__(self, model)
        self.update(partytime)
        self.rect = self.image.get_rect()
    def set_positiv(self):
        self.image = pygame.image.load(LAPTOP_IMAGE_GREEN)
    def set_negativ(self):
        self.image = pygame.image.load(LAPTOP_IMAGE_RED)

