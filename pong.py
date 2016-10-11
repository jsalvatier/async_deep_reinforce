# -*- coding: utf-8 -*-
from constants import ACTION_SIZE
from constants import USE_LSTM
from game_ac_network import GameACFFNetwork, GameACLSTMNetwork
from a3c_training_thread import ale_game_state

def make_pong_network(device):
    if USE_LSTM:
        return GameACLSTMNetwork(ACTION_SIZE, -1, device)
    else:
        return GameACFFNetwork(ACTION_SIZE, device)

def register_pong():
    from gym.envs.registration import register
    from gym_ple.ple_env import PLEEnv

    game = 'Pong'
    register(
        id='PLE-{}-v0'.format(game),
        entry_point='gym_ple:PLEEnv',
        kwargs={'game_name': game, 'display_screen':False},
        timestep_limit=10000,
        nondeterministic=False,
    )

register_pong()
    
def ple_pong(thread_index):
    from game_state_env import GameStateGymEnv
    import gym

    #env = gym.make('PLE-Pong-v0')
    env = gym.make('Pong-v0')
    return GameStateGymEnv(env)

def pong_game_function(thread_index):
    return ale_game_state(thread_index)
