from actions.action import Action
from agents.wolf_sheep_grass.grass import Grass


class EatGrass(Action):

    def act(self, sheep, env):
        cell = env.cells[sheep.x][sheep.y]
        for grass_candidate in cell.agents:
            if isinstance(grass_candidate, Grass):
                grass = grass_candidate
                if grass.green:
                    # sheep eats the grass
                    sheep.energy += sheep.gain_from_food
                    grass.green = False
                    grass.time_to_grow = grass.regrowth_time
                break
