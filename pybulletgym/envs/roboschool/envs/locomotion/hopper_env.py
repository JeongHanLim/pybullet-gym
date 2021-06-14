from pybulletgym.envs.roboschool.envs.locomotion.walker_base_env import WalkerBaseBulletEnv
from pybulletgym.envs.roboschool.robots.locomotors import Hopper


class HopperBulletEnv(WalkerBaseBulletEnv):
    def __init__(self,**kwargs):
        self.robot = Hopper(**kwargs)
        WalkerBaseBulletEnv.__init__(self, self.robot)

    def update_power(self, hyperparams):
        self.robot.update_power(hyperparams)