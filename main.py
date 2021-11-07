import os
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import platform
from kivy.app import App


from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.toast import toast


class PlayerProfile(MDNavigationDrawer):
    def __init__(self, **kwargs):
        self.profile_data_file = os.path.join(App.get_running_app().user_data_dir, "profile.txt")
        self.load_profile()
        super().__init__(**kwargs)

    def save_profile(self):
        toast("Profile Saved", 2.5)
        profile_string = self.profile_email + " " + self.profile_nickname
        with open(self.profile_data_file, "w") as outfile:
            outfile.write(profile_string)

    def load_profile(self):
        with open(self.profile_data_file, "r") as infile:
            profile_string = infile.read()
            items = profile_string.split()
            self.profile_email = items[0]
            self.profile_nickname = items[1]
            print(self.profile_email)
            print(self.profile_nickname)

    def update_status(self, *_):
        Save_Profile = False
        if self.open_progress == 0 and self.status == "closing_with_animation":
            if len(self.email.text):
                if (self.profile_email != self.email.text):
                    self.profile_email = self.email.text
                    Save_Profile = True
            else:
                print("Need a valid email")

            if len(self.nickname.text):
                if (self.profile_nickname != self.nickname.text):
                    self.profile_nickname = self.nickname.text
                    Save_Profile = True
            else:
                print("Need a valid nickname")

        elif self.open_progress == 1 and self.status =="opening_with_animation":
            self.email.text = self.profile_email
            self.nickname.text = self.profile_nickname

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