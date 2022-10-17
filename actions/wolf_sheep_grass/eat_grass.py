from actions.action import Action
from agents.wolf_sheep_grass.grass import Grass


class EatGrass(Action):

    def act(self, sheep, env):
        cell = env.cells[sheep.x][sheep.y]
        for grass_candidate in cell.agents:
            if isinstance(grass_candidate, Grass):
                self.sheep_eat_grass(sheep, grass_candidate)
                break

    @staticmethod
    def sheep_eat_grass(sheep, grass):
        if grass.green:
            sheep.energy += sheep.gain_from_food
            grass.green = False
            grass.time_to_grow = grass.regrowth_time
