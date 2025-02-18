from pybulletgym.envs.roboschool.robots.locomotors.walker_base import WalkerBase
from pybulletgym.envs.roboschool.robots.robot_bases import MJCFBasedRobot
import numpy as np

import time

class HalfCheetah(WalkerBase, MJCFBasedRobot):
    foot_list = ["ffoot", "fshin", "fthigh",  "bfoot", "bshin", "bthigh"]  # track these contacts with ground

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, power=0.90)
        MJCFBasedRobot.__init__(self, "half_cheetah.xml", "torso", action_dim=6, obs_dim=26)

    def alive_bonus(self, z, pitch):
        return +1 if np.abs(pitch) < 1.0 and not self.feet_contact[1] and not self.feet_contact[2] and not self.feet_contact[4] and not self.feet_contact[5] else -1
    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        self.jdict["bthigh"].power_coef = 120.0
        self.jdict["bshin"].power_coef = 90.0
        self.jdict["bfoot"].power_coef = 60.0
        self.jdict["fthigh"].power_coef = 140.0
        self.jdict["fshin"].power_coef = 60.0
        self.jdict["ffoot"].power_coef = 30.0


    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print() # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]

