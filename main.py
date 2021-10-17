import os
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import platform
from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer

class PlayerProfile(MDNavigationDrawer):
    def __init__(self, **kwargs):
        self.profile_data_file = os.path.join(App.get_running_app().user_data_dir, "profile.txt")
        self.load_profile()
        super().__init__(**kwargs)

    def save_profile(self):
        with open(self.profile_data_file, "w") as outfile:
            outfile.write(self.profile_email)
            outfile.write(self.profile_nickname)

    def load_profile(self):
        with open(self.profile_data_file, "r") as infile:
            self.profile_email = infile.read()
            self.profile_nickname = infile.read()
            print(self.profile_email)

    def update_status(self, *_):
        Save_Profile = False
        if self.open_progress == 0 and self.status == "closing_with_animation":
            if len(self.email.text):
                self.profile_email = self.email.text
                Save_Profile = True
            else:
                print("Need a valid email")


            if len(self.nickname.text):
                self.profile_nickname = self.nickname.text
                Save_Profile = True
            else:
                print("Need a valid nickname")

            #print(self.root.ids.avatar.source)

        super().update_status()

        if Save_Profile:
            self.save_profile()

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


if __name__ == '__main__':
    MafiaGameApp().run()