from pybulletgym.envs.roboschool.robots.locomotors.walker_base import WalkerBase
from pybulletgym.envs.roboschool.robots.robot_bases import MJCFBasedRobot


class Walker2D(WalkerBase, MJCFBasedRobot):
    foot_list = ["foot", "foot_left"]

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']

        WalkerBase.__init__(self, power=0.40)
        MJCFBasedRobot.__init__(self, "walker2d.xml", "torso", action_dim=6, obs_dim=22)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)


    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print() # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]
