# -*- coding: utf-8 -*-
import numpy as np

class GameStateGymEnv(object):
  def __init__(self, env):
    self.env = env
    self.reset()


  def reset(self):
    x_t = self.env.reset()
    dic = self.env.game_state.game.getGameState()

    self.order = dic.keys()
    self.order.sort()

    x_t = np.array([dic[key] for key in self.order])/50.
    
    self.reward = 0
    self.terminal = False
    self.s_t = np.stack((x_t, x_t, x_t, x_t))
    
  def process(self, action):
    _, r, done, _ = self.env.step(action)
    dic = self.env.game_state.game.getGameState()
    x_t = np.array([dic[key] for key in self.order])/50.

    self.reward = r
    self.terminal = done
    self.s_t1 = np.append(self.s_t[1:,:], x_t[None,:], axis=0)    

  def update(self):
    self.s_t = self.s_t1
