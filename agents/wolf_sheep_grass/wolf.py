from agents.agent import Agent


class Wolf(Agent):

    def __init__(self, x, y, energy, reproduction_rate, gain_from_food, lose_from_walk, actions):
        super().__init__(x, y, actions)
        self.energy = energy
        self.reproduction_rate = reproduction_rate
        self.gain_from_food = gain_from_food
        self.lose_from_walk = lose_from_walk
        self.actions = actions

    def decrease_energy_from_walk(self):
        self.energy -= self.lose_from_walk
