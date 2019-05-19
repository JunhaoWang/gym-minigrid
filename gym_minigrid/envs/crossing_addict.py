from gym_minigrid.minigrid import *
from gym_minigrid.register import register

import itertools as itt


class CrossingAddictEnv(MiniGridEnv):
    """
    Environment with wall or lava obstacles, sparse reward.
    """

    def __init__(self, size=9, obstacle_type=Lava, goal_x = None, opening_size = 1, opening_x = None):
        self.obstacle_type = obstacle_type
        self.goal_x = goal_x
        self.opening_size = opening_size
        self.opening_x = opening_x
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
        elif self.goal_x == 'Random' :
            self.place_obj(Goal(), top=(1, height//2 + 1), size=(width - 2, height//2 - 1))
        elif self.goal_x == 'RandomLava' and self.opening_x is None:
            self.place_obj(Goal(), top=(1, height//2), size=(4, 1))
            self.place_obj(Goal(), top=(width//2 + 3, height // 2), size=(width // 2 - 4, 1))
        elif self.goal_x == 'RandomLava' and self.opening_x is not None:
            self.place_obj(Goal(), top=(1, height//2), size=(11, 1))
        else:
            self.grid.set(self.goal_x, height//2, Goal())



        for i in range(self.opening_size):
            if self.opening_x is not None :
                self.grid.set(self.opening_x + i, height // 2, None)
            else :
                self.grid.set(width//2+i, height // 2, None)

        self.mission = (
            "avoid the lava and get to the green goal square"
            if self.obstacle_type == Lava
            else "find the opening and get to the green goal square"
        )

class LavaCrossingAgentEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=9)

class LavaCrossingAgentO8S15Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2, goal_x = 'RandomLava')

class LavaCrossingAgentO12S15Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2, opening_x=12, goal_x= 'RandomLava')

class LavaCrossingAddictO8S15Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2)

class LavaCrossingAddictO12S15Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2, opening_x=12)

class LavaCrossingAddictO8S15RandomGoalEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2, goal_x= 'Random')

class LavaCrossingAddictO12S15RandomGoalEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, opening_size=2, opening_x=12, goal_x= 'Random')



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





class LavaCrossingAgent1Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=1, opening_size=2)

class LavaCrossingAgent2Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=2, opening_size=2)

class LavaCrossingAgent3Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=3, opening_size=2)

class LavaCrossingAgent4Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=4, opening_size=2)

class LavaCrossingAgent10Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=10, opening_size=2)

class LavaCrossingAgent11Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=11, opening_size=2)

class LavaCrossingAgent12Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=12, opening_size=2)

class LavaCrossingAgent13Env(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=13, opening_size=2)


####opening on the right
class LavaCrossingAgent1RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=1, opening_x=12, opening_size=2)

class LavaCrossingAgent2RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=2, opening_x=12, opening_size=2)

class LavaCrossingAgent4RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=4, opening_x=12, opening_size=2)

class LavaCrossingAgent5RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=5, opening_x=12, opening_size=2)

class LavaCrossingAgent7RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=7, opening_x=12, opening_size=2)

class LavaCrossingAgent9RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=9, opening_x=12, opening_size=2)

class LavaCrossingAgent10RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=10, opening_x=12, opening_size=2)

class LavaCrossingAgent8RightEnv(CrossingAddictEnv):
    def __init__(self):
        super().__init__(size=15, goal_x=8, opening_x=12, opening_size=2)





register(
    id='MiniGrid-LavaCrossingAgent-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgentEnv'
)

register(
    id='MiniGrid-LavaCrossingAgentO8S15-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgentO8S15Env'
)

register(
    id='MiniGrid-LavaCrossingAgentO12S15-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgentO12S15Env'
)

register(
    id='MiniGrid-LavaCrossingAddictO8S15-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddictO8S15Env'
)

register(
    id='MiniGrid-LavaCrossingAddictO12S15-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddictO12S15Env'
)

register(
    id='MiniGrid-LavaCrossingAddictO8S15RandomGoal-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddictO8S15RandomGoalEnv'
)

register(
    id='MiniGrid-LavaCrossingAddictO12S15RandomGoal-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAddictO12S15RandomGoalEnv'
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


#####
register(
    id='MiniGrid-LavaCrossingAgent1-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent1Env'
)

register(
    id='MiniGrid-LavaCrossingAgent2-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent2Env'
)

register(
    id='MiniGrid-LavaCrossingAgent3-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent3Env'
)

register(
    id='MiniGrid-LavaCrossingAgent4-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent5Env'
)

register(
    id='MiniGrid-LavaCrossingAgent10-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent10Env'
)

register(
    id='MiniGrid-LavaCrossingAgent11-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent11Env'
)

register(
    id='MiniGrid-LavaCrossingAgent12-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent12Env'
)

register(
    id='MiniGrid-LavaCrossingAgent13-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent13Env'
)

#########
register(
    id='MiniGrid-LavaCrossingAgent1Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent1RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent2Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent2RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent4Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent4RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent5Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent5RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent7Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent7RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent8Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent8RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent9Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent9RightEnv'
)

register(
    id='MiniGrid-LavaCrossingAgent10Right-v0',
    entry_point='gym_minigrid.envs:LavaCrossingAgent10RightEnv'
)