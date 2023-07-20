#!/usr/bin/python3
"""Pygame demo, boiler play code"""
import pygame
import circle
import json
from time import sleep
import game_pad

class Main:
    """Main class. This contains the main game code"""
    def __init__(self, settings):
        """Init system"""
        # make the window
        pygame.init()
        self.settings = settings
        scale = define_window_size(settings["window"]["size"])
        self.window = pygame.display.set_mode(scale)
        surface = pygame.Surface(scale)
        print(f"Scale: {scale}")
        self.window.fill(settings["window"]["background"])
        # name the window
        pygame.display.set_caption("Pygame Demo Shooter")
        # set global vars
        self.running = True
        radius = round(scale[1] / 2)
        print(f"Radius: {radius}")
        spacer = int((scale[0] - (radius * 4)) / 4)
        left_offset = [radius + spacer,  round(scale[1] / 2)]
        right_offset = [(radius * 3) + spacer + 30,  round(scale[1] / 2)]
        # create player
        self.circles = {"left": circle.Circle(radius, settings["left"],
                                              left_offset,
                                              settings["window"]["background"],
                                              surface),
                        "right": circle.Circle(radius, settings["right"],
                                               right_offset,
                                               settings["window"]["background"],
                                               surface)}

    def run(self):
        """Main loop"""
        js = pygame.joystick.Joystick(0)
        gamepad = game_pad.GamePad(js)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.JOYBUTTONDOWN:
                    print(gamepad.get_button(event))
                elif event.type == pygame.JOYAXISMOTION:
                    gamepad.update_joystick(event)
            if not self.running:
                break
            """
            Joysticks are reporting that all the way right is 0 degrees
            Going all the way left is 180, slightly up is -179 degrees,
            slightly down is 179

            Need to figure out a way to remedy this so we get an even 360 degrees
            the whole way around
            """
            print(f"Left joystick at: {gamepad.get_joystick_location('left', formatting=True)}")
            print(f"Right joystick at: {gamepad.get_joystick_location('right', formatting=True)}")
            self.window.fill(self.settings["window"]["background"])
            self.circles["left"].update(gamepad.get_joystick_location("left", False),
                                        self.window)
            self.circles["right"].update(gamepad.get_joystick_location("right", False),
                                         self.window)
            self.draw()
            sleep(0.07)

    def draw(self):
        """Update display function"""
        #  self.window.fill(self.settings["window"]["background"])
        #  for each in self.circles:
            #  self.circles[each].draw(self.window)
        pygame.display.flip()


def define_window_size(scale):
    """take window scale and convert it to width and height"""
    if not pygame.display.get_init():
        pygame.display.init()
    res = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    output = [None, None]
    if scale in (1, "100%"):
        output = [res[0], round(res[1] / 2)]
    elif scale in (0.5, "50%"):
        output = [round(res[0] / 2), round(res[1] / 2)]
    elif scale in (0.6, "60%"):
        output = [round(2 * (res[0] / 3)), round(res[1] / 2)]
    elif scale in (0.3, "30%"):
        output = [round(res[0] / 3), round(res[1] / 3)]
    if output == [None, None]:
        return define_window_size(0.6)
    return output


def main():
    """Main function"""
    with open("settings.json", "r") as file:
        settings = json.load(file)
    Main(settings).run()


if __name__ == "__main__":
    main()
