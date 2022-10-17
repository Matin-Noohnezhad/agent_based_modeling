def walk(agent, env, x_move, y_move):
    try:
        curr_cell = env.cells[agent.x][agent.y]
        __validate_next_move(agent, env, x_move, y_move)
        next_cell = env.cells[agent.x + x_move][agent.y + y_move]
        __change_agent_cell(agent, curr_cell, next_cell)
        if __is_agent_moved(x_move, y_move):
            # Note: if line below throws an AttributeError then the simulation doesn't have anything to do with energy
            agent.decrease_energy_from_walk()
    except (IndexError, AttributeError):
        pass


def __validate_next_move(agent, env, x_move, y_move):
    # check if the next move is out of environment, then raise IndexError.
    if (agent.x + x_move) < 0 or (agent.x + x_move) >= len(env.cells):
        raise IndexError
    if (agent.y + y_move) < 0 or (agent.y + y_move) >= len(env.cells[0]):
        raise IndexError


def __is_agent_moved(x_move, y_move):
    return not (x_move == 0 and y_move == 0)


def __change_agent_cell(agent, curr_cell, next_cell):
    agent.x = next_cell.x()
    agent.y = next_cell.y()
    curr_cell.remove_agent(agent)
    next_cell.add_agent(agent)
