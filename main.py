from kivy.app import App
from kivy.uix.widget import Widget
from youtube_transcript_api import YouTubeTranscriptApi

class transcribe(Widget):
    pass

class transcribeApp(App):
    def build(self):
        return transcribe()


if __name__ == '__main__':
    transcribeApp().run()
