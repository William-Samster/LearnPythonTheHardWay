# this is the 43rd exercise of the book.
# it deals with OOPS

from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This Scene is not yet configured.")
        print("Subclass it and implement enter().")


class Death(Scene):

    def enter(self):
        print("You are so dead")
        return 'central_corridor'
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print("This is the message when you enter the corridor")
        print("You have three choises 1. Shoot,  2. Dodge, 3. Tell a joke ")

        action = input("> ")

        if action == "Shoot":
            return 'death'
        elif action == "Dodge":
            return 'death'
        elif action == "Tell a joke":
            return 'laser_weapon_armoury'
        else:
            print("Does not compute")
            return 'central_corridor'


class LazerWeapon(Scene):

    def enter(self):
        print("This is the message when you enter the Armoury")
        print("You have three choises 1. Shoot,  2. Dodge, 3. Tell a Joke ")

        action = input("> ")

        if action == "Shoot":
            return 'death'
        elif action == "Dodge":
            return 'death'
        elif action == "Tell a joke":
            return 'the_bridge'
        else:
            print("Does not compute")
            return 'laser_weapon_armoury'


class theBrige(Scene):

    def enter(self):
        print("This is the message when you enter the Bridge")
        print("You have three choises 1. Shoot,  2. Dodge, 3. Tell a Joke ")

        action = input("> ")

        if action == "Shoot":
            return 'death'
        elif action == "Dodge":
            return 'death'
        elif action == "Tell a joke":
            return 'escape_pod'
        else:
            print("Does not compute")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print("Congrats! You have reached the escape pod.")
        print("Please select the right Pod to escape.")
        print("1. Pod 1, 2. Pod 2, Pod 3")

        selection = input("> ")

        if selection == "Pod 1":
            return 'death'
        elif selection == "Pod 2":
            return 'finished'
        elif selection == "Pod 3":
            return 'death'
        else:
            print("escape_pod")


class Finished(Scene):

    def enter(self):
        print("You won! Good Job")
        return 'finished'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armoury': LazerWeapon(),
        'the_bridge': theBrige(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene.enter()


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
