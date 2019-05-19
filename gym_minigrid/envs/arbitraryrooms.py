#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import numpy as np

## not considering surrounding wall becasue such is stupid
# 0: None, 1: wall, 2: lava, 3: goal
defaultArbitraryRoom = np.array(
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
)

class ArbitraryRoomsEnv(MiniGridEnv):
    """
    Classic arbitrary rooms gridworld environment given a surrounding-wall-removed numpy map.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, agent_pos=None, goal_pos=None, simplemap=defaultArbitraryRoom, maxsteps=100):
        self._map = simplemap
        if agent_pos is None:
            agent_pos = (1,1)
        if goal_pos is None:
            goal_pos = (self._map.shape[0], self._map.shape[1])
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        super().__init__(grid_size=np.max([self._map.shape[0], self._map.shape[1]]), max_steps=maxsteps)

    def _gen_grid(self, width, height):
        # bullshit
        width = self.width
        height = self.height

        # Create the grid
        self.grid = Grid(width, height)

        # self.grid.wall_rect(0, 0, width, height)

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

        if self._goal_default_pos is not None:
            goal = Goal()
            self.grid.set(*self._goal_default_pos, goal)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info


register(
    id='MiniGrid-ArbitraryRooms-v0',
    entry_point='gym_minigrid.envs:ArbitraryRoomsEnv'
)