import cocos

class Ninja(cocos.sprite.Sprite):

    def __init__(self):

        super(Ninja, self).__init__("Idle__000.png")
        self.scale_x = -0.3
        self.scale_y = 0.3
        #self.anchor_y = "baseline"
