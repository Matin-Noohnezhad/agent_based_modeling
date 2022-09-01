def walk(agent, env, x_move, y_move):
    try:
        curr_cell = env.cells[agent.x][agent.y]
        # this line might throw an exception if index goes out of bound
        next_cell = env.cells[agent.x + x_move][agent.y + y_move]
        agent.x += x_move
        agent.y += y_move
        # move agent to the other cell
        curr_cell.remove_agent(agent)
        next_cell.add_agent(agent)
        # If agent didn't move it didn't lose energy
        if not (x_move == 0 and y_move == 0):
            # after walk decrease energy from agent
            # if line below throws an exception then the simulation doesn't have anything to do with energy
            agent.energy -= agent.lose_from_walk
    except:
        pass
        # next move will go out of environment, so we deny it.
