
class GameModel(object):

    def __init__(self):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def notify(self, event):
        pass