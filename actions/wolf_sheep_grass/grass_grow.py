from actions.action import Action


class GrassGrow(Action):

    def act(self, grass, env):
        if not grass.green:
            grass.time_to_grow -= 1
            self.grow_grass_if_needed(grass)

    @staticmethod
    def grow_grass_if_needed(grass):
        if grass.time_to_grow <= 0:
            grass.green = True
            grass.time_to_grow = grass.regrowth_time
