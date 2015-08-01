from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.image import Image

from kivy.graphics import Rotate
from kivy.properties import NumericProperty

from math import atan2, degrees

from kivy.animation import Animation

Builder.load_string('''                                                                                                                                        
<PlayerImage>:                                                                                                                                                 
    canvas.before:                                                                                                                                             
        PushMatrix                                                                                                                                             
        Rotate:                                                                                                                                                
            angle: self.angle                                                                                                                                  
            axis: (0, 0, 1)                                                                                                                                    
            origin: self.center                                                                                                                                
    canvas.after:                                                                                                                                              
        PopMatrix                                                                                                                                              
''')

class PlayerImage(Image):
    angle = NumericProperty(0)

    def on_touch_down(self, touch):
        Animation.cancel_all(self)
        angle = 0

        Animation(center=(touch.pos[0],0), angle=angle).start(self)



root = Builder.load_string('''                                                                                                                                 
Widget:                                                                                                                                                        
    PlayerImage:                                                                                                                                               
        source: '/assets/party.png'                                                                                                                                  
        allow_stretch: True                                                                                                                                    
        keep_ratio: False                                                                                                                                      
''')

runTouchApp(root)