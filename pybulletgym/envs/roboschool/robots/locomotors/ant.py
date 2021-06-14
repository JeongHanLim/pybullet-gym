from pybulletgym.envs.roboschool.robots.locomotors.walker_base import WalkerBase
from pybulletgym.envs.roboschool.robots.robot_bases import MJCFBasedRobot


class Ant(WalkerBase, MJCFBasedRobot):
    foot_list = ['front_left_foot', 'front_right_foot', 'left_back_foot', 'right_back_foot']

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, power=2.5)
        MJCFBasedRobot.__init__(self, "ant.xml", "torso", action_dim=8, obs_dim=28)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.26 else -1  # 0.25 is central sphere rad, die if it scrapes the ground

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.jdict.keys()):
            self.jdict[data].power_coef = 150


    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()  # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]
