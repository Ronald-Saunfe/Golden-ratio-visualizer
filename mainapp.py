from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Bezier, Line, Rectangle
import math
import threading
from kivy.config import Config

Config.set('kivy','window_icon','icon.ico')

class Bex(Widget):
    def __init__(self, **kwargs):
        super(Bex, self).__init__(**kwargs)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.calc(touch)
            self.show()

    def calc(self, touch):
        self.points = []
        dist =  int(self.parent.ids.txtd.value)
        for theta in range(int(self.parent.ids.txtanglestart.value), int(self.parent.ids.txtangleend.value)):
            #x
            self.points.append(touch.pos[0]+ dist * math.cos(theta))
            # y
            self.points.append(touch.pos[1]+ dist * math.sin(theta))
            dist += int(self.parent.ids.distanceincr.value)
                
    def show(self):
        self.canvas.clear()
        with self.canvas:
            Bezier(points =self.points,
                   segments = int(self.parent.ids.lnsegm.value))
                
                    
  
class Mm(FloatLayout):
    pass

class mainapp(App):
    
    def build(self):
        self.icon ="icon.ico"
        self.title = "Golden ratio analyzer"
        m = Mm()
        return m

mainapp().run()
