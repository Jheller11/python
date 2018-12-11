from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)
