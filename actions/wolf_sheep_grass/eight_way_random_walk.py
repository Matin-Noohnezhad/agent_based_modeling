from actions.action import Action
from actions.action_utils import walk
import random


class EightWayRandomWalk(Action):

    def act(self, agent, env):
        # 1 or 0 or -1
        x_move = round(random.random() * 2) - 1
        # 1 or 0 or -1
        y_move = round(random.random() * 2) - 1
        #
        walk(agent, env, x_move, y_move)
