#! /usr/bin/env python
# -*- coding: utf-8 -*-

from event_manager import *
from time_controller import TimeController

def main():
    event_manager = EventManager()
    event_manager.test()
    time_controller = TimeController(event_manager)
    time_controller.run()


if __name__ == "__main__":
    main()