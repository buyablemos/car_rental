from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from Manager import ManagerScreen
from Login_Screen import *
from User_Screen import UserScreen


class Car_rental(App):
    def build(self):
        self.screen_manager = ScreenManager()
        main_screen = MainScreen(name='main')
        self.screen_manager.add_widget(main_screen)
        login_screen = LoginScreen('user',name='login')
        self.screen_manager.add_widget(login_screen)
        login_screen_staff = LoginScreen('staff',name='staff')
        self.screen_manager.add_widget(login_screen_staff)
        register_screen = RegisterScreen(name='register')
        self.screen_manager.add_widget(register_screen)
        manager_screen = ManagerScreen(name='manager')
        self.screen_manager.add_widget(manager_screen)
        user_screen = UserScreen(name='user')
        self.screen_manager.add_widget(user_screen)

        return self.screen_manager

if __name__ == '__main__':
    Car_rental().run()
