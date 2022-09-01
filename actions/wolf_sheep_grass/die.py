from actions.action import Action


class Die(Action):

    def act(self, agent, env):
        if agent.energy < 0:
            env.remove_agent(agent)
