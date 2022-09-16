from colorama import Fore, init
from os import system
from pynput.keyboard import Listener, Key
from .fonsoleoption import fonsoleOption

init()

class fonsoleMenu:

    def __init__(self, title: str, options: list[fonsoleOption]):
        self.listener = None
        for x in range(len(options)):

            if not isinstance(options[x], fonsoleOption): raise TypeError(
                f"Options type Error! Should be <class 'fonsoleOptions'> instead of {type(options[x])}")
            options[x].index = x

        self.title = title
        self.choosed = 0
        self.options = options

    def show(self):
        print(f"{Fore.WHITE}{self.title}")
        for _ in self.options:
            print(f"{Fore.WHITE}   {_.name}") if self.options.index(_) != self.choosed else print(f"{Fore.CYAN}>   {_.name}{Fore.WHITE}")

    def update(self):
        system('cls')
        self.show()

    def on_press(self, key):
        if key == Key.down:
            self.move_down()
        elif key == Key.up:
            self.move_up()
        elif key == Key.enter:
            self.confirm()

    @staticmethod
    def on_release(key):
        if key == Key.esc:
            return False

    def start(self):
        self.show()
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.listener = listener
            self.listener.join()
            return self.confirm()

    def move_up(self):
        if self.choosed == 0:
            self.choosed = len(self.options)-1
        else:
            self.choosed -= 1

        self.update()

    def move_down(self):
        if self.choosed == len(self.options)-1:
            self.choosed = 0
        else:
            self.choosed += 1

        self.update()

    def confirm(self) -> fonsoleOption:
        self.listener.stop()
        return self.options[self.choosed]
