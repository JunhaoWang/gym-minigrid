from gym_minigrid.minigrid import *
from gym_minigrid.register import register

import itertools as itt


class CrossingAddictEnv(MiniGridEnv):
    """
    Environment with wall or lava obstacles, sparse reward.
    """

    def __init__(self, size=9, obstacle_type=Lava, goal_x = None):
        self.obstacle_type = obstacle_type
        self.goal_x = goal_x
        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=False,
            seed=None
        )

    def _gen_grid(self, width, height):
        assert width % 2 == 1 and height % 2 == 1  # odd size

        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place the agent in the top-left corner
        self.start_pos = (1, 1)
        self.start_dir = 0

        for i in range(1,width-1):
            self.grid.set(i, height//2, Lava())

        # Place a goal square in the bottom-right corner
        if self.goal_x is None :
            self.grid.set(width - 2, height - 2, Goal())
        else :
            self.grid.set(self.goal_x, height//2, Goal())

        self.grid.set(width//2, height // 2, None)

        self.mission = (
            "avoid the lava and get to the green goal square"
            if self.obstacle_type == Lava
            else "find the opening and get to the green goal square"
        )

class LavaCrossingAgentEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9)

class LavaCrossingAddict1Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=1)

class LavaCrossingAddict2Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=2)

class LavaCrossingAddict3Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=3)

class LavaCrossingAddict5Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=5)

class LavaCrossingAddict6Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=6)

class LavaCrossingAddict7Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9, goal_x=7)


register(
    id='MiniGrid-LavaCrossingAgent-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgentEnv'
)

register(
    id='MiniGrid-LavaCrossingAddict1-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict1Env'
)

register(
    id='MiniGrid-LavaCrossingAddict2-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict2Env'
)

register(
    id='MiniGrid-LavaCrossingAddict3-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict3Env'
)

register(
    id='MiniGrid-LavaCrossingAddict5-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict5Env'
)

register(
    id='MiniGrid-LavaCrossingAddict6-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict6Env'
)

register(
    id='MiniGrid-LavaCrossingAddict7-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddict7Env'
)