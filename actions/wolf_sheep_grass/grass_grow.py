import copy
import random

from actions.action import Action


class GrassGrow(Action):

    def act(self, grass, env):
        if not grass.green:
            grass.time_to_grow -= 1
            if grass.time_to_grow == 0:
                grass.green = True
                grass.time_to_grow = grass.regrowth_time
