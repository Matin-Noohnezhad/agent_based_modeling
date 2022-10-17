class Agent:

    def __init__(self, x, y, actions):
        self.actions = actions
        self.x = x
        self.y = y

    def perceive(self, env):
        pass

    def act(self, env):
        for action in self.actions:
            action.act(self, env)
