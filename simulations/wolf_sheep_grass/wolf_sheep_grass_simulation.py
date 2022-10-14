import random

import matplotlib.pyplot as plt
import numpy as np

from actions.action import Action
from actions.wolf_sheep_grass.die import Die
from actions.wolf_sheep_grass.eat_grass import EatGrass
from actions.wolf_sheep_grass.eat_sheep import EatSheep
from actions.wolf_sheep_grass.eight_way_random_walk import EightWayRandomWalk
from actions.wolf_sheep_grass.grass_grow import GrassGrow
from actions.wolf_sheep_grass.reproduce import Reproduce
from agents.wolf_sheep_grass.grass import Grass
from agents.wolf_sheep_grass.sheep import Sheep
from agents.wolf_sheep_grass.wolf import Wolf
from envs.cell import Cell
from envs.env import Env
from simulations.simulation import Simulation
from . import config as cfg


class WolfSheepGrassSimulation(Simulation):

    def __init__(self):
        self.grass_actions: list[Action] = None
        self.sheep_actions: list[Action] = None
        self.wolf_actions: list[Action] = None
        self.initialize_actions()
        #
        self.env: Env = None
        self.create_environment_and_agents()

    def initialize_actions(self):
        reproduce = Reproduce()
        die = Die()
        eat_sheep = EatSheep()
        eat_grass = EatGrass()
        grass_grow = GrassGrow()
        random_walk = EightWayRandomWalk()
        #
        self.wolf_actions = [random_walk, eat_sheep, die, reproduce]
        self.sheep_actions = [random_walk, eat_grass, die, reproduce]
        self.grass_actions = [grass_grow]

    def create_environment_and_agents(self):
        self.create_env_cells_grasses()
        self.create_sheep()
        self.create_wolves()

    def create_env_cells_grasses(self):
        env_cells = []
        env_grass = []
        for y in range(cfg.ENV_NUMBER_OF_ROWS):
            cells_row = []
            for x in range(cfg.ENV_NUMBER_OF_COLS):
                cell = Cell()
                cells_row.append(cell)
                grass_green = random.random() > cfg.GREEN_GRASS_RATE
                grass = Grass(x, y, cfg.GRASS_REGROWTH_TIME, grass_green, self.grass_actions)
                cell.add_agent(grass)
                env_grass.append(grass)
            env_cells.append(cells_row)
        self.env = Env(env_grass, env_cells)

    def create_sheep(self):
        sheep_x_list = list(np.random.randint(0, cfg.ENV_NUMBER_OF_COLS, cfg.INITIAL_NUMBER_OF_SHEEP))
        sheep_y_list = list(np.random.randint(0, cfg.ENV_NUMBER_OF_ROWS, cfg.INITIAL_NUMBER_OF_SHEEP))
        sheep_positions = list(zip(sheep_x_list, sheep_y_list))
        for sheep_position in sheep_positions:
            sheep = Sheep(sheep_position[0], sheep_position[1], cfg.SHEEP_START_ENERGY, cfg.SHEEP_REPRODUCTION_RATE,
                          cfg.SHEEP_GAIN_FROM_FOOD, cfg.SHEEP_LOSE_FROM_WALK, self.sheep_actions)
            self.env.add_agent(sheep)

    def create_wolves(self):
        wolves_x_list = list(np.random.randint(0, cfg.ENV_NUMBER_OF_COLS, cfg.INITIAL_NUMBER_OF_WOLVES))
        wolves_y_list = list(np.random.randint(0, cfg.ENV_NUMBER_OF_ROWS, cfg.INITIAL_NUMBER_OF_WOLVES))
        wolves_positions = list(zip(wolves_x_list, wolves_y_list))
        for wolves_position in wolves_positions:
            wolf = Wolf(wolves_position[0], wolves_position[1], cfg.WOLF_START_ENERGY, cfg.WOLF_REPRODUCTION_RATE,
                        cfg.WOLF_GAIN_FROM_FOOD,
                        cfg.WOLF_LOSE_FROM_WALK, self.wolf_actions)
            self.env.add_agent(wolf)

    def run(self, num_of_time_steps: int):
        sheep_count_history: list[int] = []
        wolf_count_history: list[int] = []
        grass_count_history: list[int] = []
        for i in range(num_of_time_steps):
            # Note: sheep-wolves-grass problem is asynchronous
            self.env.step(synchronous=False)
            # plotting
            sheep_count, wolf_count, green_grass_count = self.__count_each_agent()
            print('sheep-wolf-green_grass')
            print(sheep_count, '-', wolf_count, '-', green_grass_count)
            sheep_count_history.append(sheep_count)
            wolf_count_history.append(wolf_count)
            grass_count_history.append(green_grass_count / 4)
            self.__plot_number_of_agents(sheep_count_history, wolf_count_history, grass_count_history)

    def __count_each_agent(self):
        sheep_count = sum(map(lambda agent: isinstance(agent, Sheep), self.env.agents))
        wolf_count = sum(map(lambda agent: isinstance(agent, Wolf), self.env.agents))
        green_grass_count = sum(map(lambda agent: (isinstance(agent, Grass) and agent.green), self.env.agents))
        return sheep_count, wolf_count, green_grass_count

    @staticmethod
    def __plot_number_of_agents(sheep_count_hist: list[int], wolf_count_hist: list[int], grass_count_hist: list[int]):
        plt.xlabel('step')
        step_hist = range(0, len(sheep_count_hist))
        plt.clf()
        plt.plot(step_hist, sheep_count_hist, color='r', label='sheep')
        plt.plot(step_hist, wolf_count_hist, color='b', label='wolf')
        plt.plot(step_hist, grass_count_hist, 'g', label='grass')
        plt.draw()
        plt.legend(loc='upper right')
        plt.pause(0.0001)
