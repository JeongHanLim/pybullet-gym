from pybulletgym.envs.roboschool.robots.locomotors.walker_base import WalkerBase
from pybulletgym.envs.roboschool.robots.robot_bases import MJCFBasedRobot


class Hopper(WalkerBase, MJCFBasedRobot):
    foot_list = ["foot"]

    def __init__(self,**kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, power=0.75)
        MJCFBasedRobot.__init__(self, "hopper.xml", "torso", action_dim=3, obs_dim=15)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.jdict.keys()):
            self.jdict[data].power_coef = 200


    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()  # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]
