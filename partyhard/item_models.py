class ItemModel(object):
    def __init__(self, game_model):
        self.partytime = True
        self.game_model = game_model

class BeerModel(ItemModel):
    def __init__(self, game_model):
        ItemModel.__init__(self, game_model)

class CocktailModel(ItemModel):
    def __init__(self, game_model):
        ItemModel.__init__(self, game_model)

class BookModel(ItemModel):
    def __init__(self, game_model):
        ItemModel.__init__(self, game_model)
        self.partytime = False

class PenModel(ItemModel):
    def __init__(self, game_model):
        ItemModel.__init__(self, game_model)
        self.partytime = False