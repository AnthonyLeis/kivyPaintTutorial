from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Ellipse, Line
from random import random


class PaintWidget(Widget):
    def setup(self):
        self.color = (random(), random(), random())
        self.radius = 30.

    def setColor(self, color):
        self.color = color

    def on_touch_down(self, touch):
        with self.canvas:
            # print(self.parent.getColor())
            self.setColor(self.parent.getColor())
            Color(self.color[0], self.color[1], self.color[2])
            d = 30.
            # Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        with self.canvas:
            touch.ud['line'].points += [touch.x, touch.y]

class MyToggleButton(ToggleButton):
    def on_press(self):
        self.parent.setColor(self.color)

    def setup(self, color):
        self.colorData = color

class MyWidget(Widget):
    def __init__(self):
        super().__init__()
        self.painter = PaintWidget()
        self.painter.setup()
        clearbtn = Button(text='Clear')
        self.currentColor = (1,1,1,1)
        self.colors = [self.currentColor]
        self.addColor((.1,1,1,1))
        self.addColor((1,.1,1,1))
        self.addColor((1,1,.1,1))
        self.addColor((1,.1,.1,1))
        clearbtn.bind(on_release=self.clear_canvas)
        self.add_widget(self.painter)
        self.add_widget(clearbtn)
        for color in range(len(self.colors)):
            button = MyToggleButton(text=str(color), group="colors", pos=((color+1)*100,0), color=self.colors[color], background_color=self.colors[color])
            self.add_widget(button)

    def addColor(self, color):
        self.colors += [color]

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def getColor(self):
        return self.currentColor

    def setColor(self, color):
        self.currentColor = (color[0], color[1], color[2], color[3])

class PaintApp(App):
    def build(self):
        parent = MyWidget()

        return parent


if __name__ == '__main__':
    PaintApp().run()
