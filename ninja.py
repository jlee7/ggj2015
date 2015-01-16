import cocos

class Ninja(cocos.sprite.Sprite):

    def __init__(self):

        super(Ninja, self).__init__("Idle__000.png")
        self.scale_x = -1
