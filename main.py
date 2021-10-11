from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import platform


class MafiaGameApp(MDApp):

    def __init__(self, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        if platform not in ('android', 'ios'):
            Config.set('graphics', 'resizable', '0')
            Window.size = (480,1080)


    def build(self):
        '''
        :return: None
        '''

    def update_profile(self):
        if len(self.root.ids.email.text):
            print(self.root.ids.email.text)
        if len(self.root.ids.nickname.text):
            print(self.root.ids.nickname.text)

        print(self.root.ids.avatar.source)

if __name__ == '__main__':
    MafiaGameApp().run()