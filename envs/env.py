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
        if synchronous:  # synchronous update
            # perceive step
            for agent in self.agents:
                agent.perceive(self)
            # actions step
            for agent in self.agents:
                agent.action(self)
        else:  # asynchronous update
            # shuffle the agents so there is no priority for action of any agent against the other agents action
            random.shuffle(self.agents)
            for agent in self.agents:
                # perceive and action in the same step for each agent
                agent.action(self)
