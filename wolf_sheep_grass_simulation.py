import random

from actions.wolf_sheep_grass.die import Die
from actions.wolf_sheep_grass.eat_grass import EatGrass
from actions.wolf_sheep_grass.eat_sheep import EatSheep
from actions.wolf_sheep_grass.eight_way_random_walk import EightWayRandomWalk
from actions.wolf_sheep_grass.grass_grow import GrassGrow
from actions.wolf_sheep_grass.reproduce import Reproduce
from agents.wolf_sheep_grass.grass import Grass
from agents.wolf_sheep_grass.sheep import Sheep
from agents.wolf_sheep_grass.wolf import Wolf
import matplotlib.pyplot as plt
import time
from envs.cell import Cell
import numpy as np
from envs.env import Env

NUM_OF_TIME_STEPS = 500

ENV_NUMBER_OF_ROWS = 50
ENV_NUMBER_OF_COLS = 50
INITIAL_NUMBER_OF_SHEEP = 100
INITIAL_NUMBER_OF_WOLVES = 50
GREEN_GRASS_RATE = 0.5
GRASS_REGROWTH_TIME = 30

# wolf initial values
wolf_start_energy = 20
wolf_reproduction_rate = 0.05
wolf_gain_from_food = 20
wolf_lose_from_walk = 1

# sheep initial values
sheep_start_energy = 4
sheep_reproduction_rate = 0.04
sheep_gain_from_food = 4
sheep_lose_from_walk = 1

# grass initial values
grass_regrowth_time = 30

# create actions
reproduce = Reproduce()
die = Die()
eat_sheep = EatSheep()
eat_grass = EatGrass()
grass_grow = GrassGrow()
random_walk = EightWayRandomWalk()
#
wolf_actions = [random_walk, eat_sheep, die, reproduce]
sheep_actions = [random_walk, eat_grass, die, reproduce]
grass_actions = [grass_grow]

# create env, cells, grasses
env_cells = []
env_grass = []
for y in range(ENV_NUMBER_OF_ROWS):
    cells_row = []
    for x in range(ENV_NUMBER_OF_COLS):
        cell = Cell()
        cells_row.append(cell)
        # With probability of GREEN_GRASS_RATE the grass in this cell is green
        grass_green = random.random() > GREEN_GRASS_RATE
        grass = grass = Grass(x, y, grass_regrowth_time, grass_green, grass_actions)
        cell.add_agent(grass)
        env_grass.append(grass)
    env_cells.append(cells_row)
env = Env(env_grass, env_cells)
# create sheep
sheep_x_list = list(np.random.randint(0, ENV_NUMBER_OF_COLS, INITIAL_NUMBER_OF_SHEEP))
sheep_y_list = list(np.random.randint(0, ENV_NUMBER_OF_ROWS, INITIAL_NUMBER_OF_SHEEP))
sheep_positions = list(zip(sheep_x_list, sheep_y_list))
for sheep_position in sheep_positions:
    sheep = Sheep(sheep_position[0], sheep_position[1], sheep_start_energy, sheep_reproduction_rate,
                  sheep_gain_from_food, sheep_lose_from_walk, sheep_actions)
    env.add_agent(sheep)
# create wolves
wolves_x_list = list(np.random.randint(0, ENV_NUMBER_OF_COLS, INITIAL_NUMBER_OF_WOLVES))
wolves_y_list = list(np.random.randint(0, ENV_NUMBER_OF_ROWS, INITIAL_NUMBER_OF_WOLVES))
wolves_positions = list(zip(wolves_x_list, wolves_y_list))
for wolves_position in wolves_positions:
    wolf = Wolf(wolves_position[0], wolves_position[1], wolf_start_energy, wolf_reproduction_rate, wolf_gain_from_food,
                wolf_lose_from_walk, wolf_actions)
    env.add_agent(wolf)


#
def count_each_agent(agents):
    sheep_count = sum(map(lambda agent: isinstance(agent, Sheep), agents))
    wolf_count = sum(map(lambda agent: isinstance(agent, Wolf), agents))
    grass_count = sum(map(lambda agent: isinstance(agent, Grass), agents))
    return sheep_count, wolf_count, grass_count


def plot_number_of_agents(sheep_count_hist, wolf_count_hist, grass_count_hist):
    plt.xlabel('step')
    step_hist = range(1, len(sheep_count_hist) + 1)
    plt.clf()
    plt.plot(step_hist, sheep_count_hist, color='r', label='sheep')
    plt.plot(step_hist, wolf_count_hist, color='b', label='wolf')
    plt.plot(step_hist, grass_count_hist, 'g', label='grass')
    plt.draw()
    plt.legend(loc='upper right')
    plt.pause(0.0001)


sheep_count_history = []
wolf_count_history = []
grass_count_history = []
for i in range(NUM_OF_TIME_STEPS):
    # sheep-wolves-grass problem is asynchronous
    env.step(synchronous=False)
    #
    sheep_count, wolf_count, grass_count = count_each_agent(env.agents)
    sheep_count_history.append(sheep_count)
    wolf_count_history.append(wolf_count)
    grass_count_history.append(grass_count/4)
    plot_number_of_agents(sheep_count_history, wolf_count_history, grass_count_history)
