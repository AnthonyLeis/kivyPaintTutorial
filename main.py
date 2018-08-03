from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.slider import Slider

from random import random


class PaintWidget(Widget):
    def __init__(self):
        super().__init__()
        self.radius = 30.

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.parent.getLineColor())
            d = 30.
            # Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.parent.getLineWidth())

    def on_touch_move(self, touch):
        with self.canvas:
            touch.ud['line'].points += [touch.x, touch.y]

class MyToggleButton(ToggleButton):
    def on_press(self):
        self.parent.setLineColor(self.color)

    def setup(self, color):
        self.colorData = color

class WrapperWidget(Widget):
    def __init__(self):
        super().__init__()
        self.painter = PaintWidget()
        self.currentLineColor = (1,1,1,1)
        self.lineWidth = 5.0
        self.colors = [self.currentLineColor]
        self.addColor((.1,1,1,1))
        self.addColor((1,.1,1,1))
        self.addColor((1,1,.1,1))
        self.addColor((1,.1,.1,1))
        clearbtn = Button(text='Clear')
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

    def getLineColor(self):
        return self.currentLineColor

    def setLineColor(self, color):
        self.currentLineColor = (color[0], color[1], color[2])

    def getLineWidth(self):
        return self.lineWidth

    def setLineWidth(self, width):
        self.lineWidth = width

class PaintApp(App):
    def build(self):
        parent = WrapperWidget()

        return parent


if __name__ == '__main__':
    PaintApp().run()
