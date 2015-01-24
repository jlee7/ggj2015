class ItemModel(object):
    def __init__(self):
        self.partytime = True

class BeerModel(ItemModel):
    def __init__(self):
        ItemModel.__init__(self)

class CocktailModel(ItemModel):
    def __init__(self):
        ItemModel.__init__(self)

class BookModel(ItemModel):
    def __init__(self):
        ItemModel.__init__(self)
        self.partytime = False

class PenModel(ItemModel):
    def __init__(self):
        ItemModel.__init__(self)
        self.partytime = False