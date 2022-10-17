from actions.action import Action
from agents.wolf_sheep_grass.sheep import Sheep


class EatSheep(Action):

    def act(self, wolf, env):
        cell = env.cells[wolf.x][wolf.y]
        for sheep_candidate in cell.agents:
            if isinstance(sheep_candidate, Sheep):
                self.wolf_eat_sheep(wolf, sheep_candidate, env)
                break

    @staticmethod
    def wolf_eat_sheep(wolf, sheep, env):
        wolf.energy += wolf.gain_from_food
        env.remove_agent(sheep)
