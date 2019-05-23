#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import numpy as np
from .supergridrooms import defaultAgentPose

## not considering surrounding wall becasue such is stupid
# 0: None, 1: wall, 2: lava, 3: goal

from .jesuitrooms import room_size

defaultArbitraryRoom = np.array(
    [
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    ]
)

defaultArbitraryRoom = defaultArbitraryRoom.T

defaultArbitraryRoom1 = np.array(
    [
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)

defaultArbitraryRoom1 = defaultArbitraryRoom1.T

defaultArbitraryRoom2 = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)

defaultArbitraryRoom2 = defaultArbitraryRoom2.T

defaultArbitraryRoom3 = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)

defaultArbitraryRoom3 = defaultArbitraryRoom3.T


class SupergridRoomsAddictEnv(MiniGridEnv):
    """
    Classic arbitrary rooms gridworld environment given a surrounding-wall-removed numpy map.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, agent_pos=defaultAgentPose, simplemap=defaultArbitraryRoom, maxsteps=100):
        self._map = simplemap
        if agent_pos is None:
            agent_pos = (1,1)

        self._agent_default_pos = agent_pos

        super().__init__(width=self._map.shape[0] + 2, height= self._map.shape[1] + 2, max_steps=maxsteps)

    def _gen_grid(self, width, height):
        # bullshit
        width = self.width
        height = self.height

        # Create the grid
        self.grid = Grid(width, height)

        self.grid.wall_rect(0, 0, width, height)

        # Create other shit
        for row_idx, row in enumerate(self._map):
            row_idx_actual = row_idx + 1
            for col_idx, val in enumerate(row):
                col_idx_actual = col_idx + 1
                if val == 0:
                    self.grid.set(row_idx_actual, col_idx_actual, None)
                elif val == 1:
                    self.grid.set(row_idx_actual, col_idx_actual, Wall())
                elif val == 2:
                    self.grid.set(row_idx_actual, col_idx_actual, Lava())
                elif val == 3:
                    self.grid.set(row_idx_actual, col_idx_actual, Goal())
                else:
                    raise Exception('map is wrong')


        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.start_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.start_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()


        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info


class SupergridRoomsAddict1Env(SupergridRoomsAddictEnv):
    def __init__(self):
        super().__init__(simplemap=defaultArbitraryRoom1)

class SupergridRoomsAddict2Env(SupergridRoomsAddictEnv):
    def __init__(self):
        super().__init__(simplemap=defaultArbitraryRoom2)

class SupergridRoomsAddict3Env(SupergridRoomsAddictEnv):
    def __init__(self):
        super().__init__(simplemap=defaultArbitraryRoom3)


register(
    id='MiniGrid-SupergridRoomsAddict1Env-v0',
    entry_point='gym_minigrid.envs:SupergridRoomsAddict1Env'
)

register(
    id='MiniGrid-SupergridRoomsAddict2Env-v0',
    entry_point='gym_minigrid.envs:SupergridRoomsAddict2Env'
)

register(
    id='MiniGrid-SupergridRoomsAddict3Env-v0',
    entry_point='gym_minigrid.envs:SupergridRoomsAddict3Env'
)
