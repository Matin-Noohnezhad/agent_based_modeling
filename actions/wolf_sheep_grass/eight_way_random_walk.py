from actions.action import Action
from actions.action_utils import walk
import random


class EightWayRandomWalk(Action):

    def act(self, agent, env):
        x_move = random.randint(-1, 1)
        y_move = random.randint(-1, 1)
        walk(agent, env, x_move, y_move)
