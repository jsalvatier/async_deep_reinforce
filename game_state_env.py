# -*- coding: utf-8 -*-
import numpy as np

def normalize_dic(dic):
  return {
    "fruit_x": dic['fruit_x']/50.-.6,
    "fruit_y": dic['fruit_y']/50.-.5,
    "player_x": dic['player_x']/50.-.5,
    "player_vel": dic['player_vel']/3.
  }

def state_to_array(prev_dic, dic):
  prev_dic_norm = normalize_dic(prev_dic)
  dic_norm = normalize_dic(dic)
  vs = [
    dic_norm["fruit_x"],
    dic_norm["fruit_y"],
    dic_norm["player_x"],
    dic_norm["player_vel"],
    dic_norm["fruit_x"] - dic_norm["player_x"], #,
    # dic_norm["player_vel"] - prev_dic_norm["player_vel"]
  ]
  return np.array(vs)

class GameStateGymEnv(object):
  def __init__(self, env):
    self.env = env
    self.reset()


  def reset(self):
    x_t = self.env.reset()
    dic = self.env.game_state.game.getGameState()
    self.prev_dic = dic

    self.order = dic.keys()
    self.order.sort()
    
    x_t = state_to_array(dic, dic)
    
    self.reward = 0
    self.terminal = False
    self.s_t = np.stack((x_t,))
    return self.s_t
    
  def process(self, action):
    _, r, done, _ = self.env.step(action)
    dic = self.env.game_state.game.getGameState()
    x_t = state_to_array(self.prev_dic, dic)  # self.prev_dic,
    self.prev_dic = dic
    
    self.reward = r
    self.terminal = done

    self.s_t1 = np.stack((x_t,))
    return self.s_t1

  def update(self):
    self.s_t = self.s_t1
