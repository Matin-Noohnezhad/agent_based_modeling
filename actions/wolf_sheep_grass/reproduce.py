import copy
import random

from actions.action import Action


class Reproduce(Action):

    def act(self, agent, env):
        rnd = random.random()
        if rnd < agent.reproduction_rate:
            new_agent = copy.deepcopy(agent)
            env.add_agent(new_agent)
