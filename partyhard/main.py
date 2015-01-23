#! /usr/bin/env python
# -*- coding: utf-8 -*-

from event_manager import *
from time_controller import TimeController
from game_view import GameView
import pygame

def main():

    pygame.init()

    event_manager = EventManager()
    event_manager.test()

    game_view = GameView(event_manager)

    time_controller = TimeController(event_manager)

    time_controller.run()


if __name__ == "__main__":
    main()