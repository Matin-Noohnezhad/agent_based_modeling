import random


class Env:

    def __init__(self, agents, cells):
        self.agents = agents
        self.cells = cells

    def add_agent(self, agent):
        self.agents.append(agent)
        self.cells[agent.x][agent.y].add_agent(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)
        self.cells[agent.x][agent.y].remove_agent(agent)

    def step(self, synchronous):
        if synchronous:
            self.__perceive_step()
            self.__actions_step()
        else:
            self.__perceive_action_step()

    def __perceive_step(self):
        for agent in self.agents:
            agent.perceive(self)

    def __actions_step(self):
        for agent in self.agents:
            agent.act(self)

    def __perceive_action_step(self):
        # shuffle the agents so there is no priority for action of any agent against the other agents action
        random.shuffle(self.agents)
        for agent in self.agents:
            agent.perceive(self)
            agent.act(self)
