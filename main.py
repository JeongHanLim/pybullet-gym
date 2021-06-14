import gym
from time import sleep
from load_parameters import load_hyperparameters
import random
from stable_baselines.sac.policies import MlpPolicy
from stable_baselines import SAC
import numpy as np
import pybulletgym

env_name = 'AntPyBulletEnv-v0'
#env_list = [AntPyBulletEnv-v0	,HalfCheetahPyBulletEnv-v0, Walker2DPyBulletEnv-v0, HopperPyBulletEnv-v0]

hyperparam = load_hyperparameters(env_name)
env = gym.make(env_name, hyper = hyperparam)

model = SAC(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=30000, log_interval=10)
# model.save("test")

episode = 0
rewards = []
for i in range(1000):
    state = env.reset()
    reward_episode = 0
    episode +=1
    while True:
        #action, _ = model.predict(state)
        action = env.action_space.sample()
        ns, rw, done, info = env.step(action)
        reward_episode+=rw
        if done == True:
            rewards.append(reward_episode)
            break
        hyperparam.update({}) #FIXME : SOMETHING HYPERPARAMETER HERE
        env.update_power(hyperparam)

print(np.mean(rewards))
print(np.std(rewards))

