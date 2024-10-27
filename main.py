from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
import math

class TheLabApp(App):
    def build(self):
        return MainWidget()

class MainWidget(GridLayout):
    display_text = StringProperty("")

    def click(self, button_text):
        if button_text == "C":
            self.display_text = ""
        elif button_text == "=":
                if self.display_text.startswith("√"):
                    value = float(self.display_text[1:])
                    if value < 0:
                        self.display_text="Error"
                    else:
                       y = math.sqrt(value)
                       self.display_text = str(y)
                else:
                    x = str(eval(self.display_text))
                    self.display_text = x
        elif button_text == "√":
            if not self.display_text:
                self.display_text += "√"
        else:
            self.display_text += button_text

TheLabApp().run()