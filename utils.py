import matplotlib.pyplot as plt

from agents.wolf_sheep_grass.grass import Grass
from agents.wolf_sheep_grass.sheep import Sheep
from agents.wolf_sheep_grass.wolf import Wolf


def count_each_agent(agents):
    sheep_count = sum(map(lambda agent: isinstance(agent, Sheep), agents))
    wolf_count = sum(map(lambda agent: isinstance(agent, Wolf), agents))
    green_grass_count = sum(map(lambda agent: (isinstance(agent, Grass) and agent.green), agents))
    return sheep_count, wolf_count, green_grass_count


def plot_number_of_agents(sheep_count_hist, wolf_count_hist, grass_count_hist):
    plt.xlabel('step')
    step_hist = range(0, len(sheep_count_hist))
    plt.clf()
    plt.plot(step_hist, sheep_count_hist, color='r', label='sheep')
    plt.plot(step_hist, wolf_count_hist, color='b', label='wolf')
    plt.plot(step_hist, grass_count_hist, 'g', label='grass')
    plt.draw()
    plt.legend(loc='upper right')
    plt.pause(0.0001)