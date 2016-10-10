# -*- coding: utf-8 -*-
import numpy as np

class GameStateGymEnv(object):
  def __init__(self, env):
    self.env = env
    self.reset()


  def reset(self):
    x_t = self.env.reset()
    
    self.reward = 0
    self.terminal = False
    self.s_t = np.stack((x_t, x_t, x_t, x_t), axis = 2)
    
  def process(self, action):
    observation, r, done, _ = self.env.step(action)

    self.reward = r
    self.terminal = t
    self.s_t1 = np.append(self.s_t[:,:,1:], x_t1, axis = 2)    

  def update(self):
    self.s_t = self.s_t1
