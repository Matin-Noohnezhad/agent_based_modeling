import copy
import random

from actions.action import Action


class Reproduce(Action):

    def act(self, agent, env):
        if random.random() < agent.reproduction_rate:
            new_agent = copy.deepcopy(agent)
            env.add_agent(new_agent)
