class Cell:

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def x(self):
        return self.agents[0].x

    def y(self):
        return self.agents[0].y

