from kivy.app import App
from kivy.uix.widget import Widget

class transcribe(Widget):
    pass

class transcribeApp(App):
    def build(self):
        return transcribe()


if __name__ == '__main__':
    transcribeApp().run()