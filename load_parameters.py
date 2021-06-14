import json


def load_hyperparameters(env):
    path = "hyperparameter/"+str(env)+".json"
    with open(path, "r") as f:
        hyperparmas = json.load(f)
    return hyperparmas


# Test Code
if __name__ == "__main__":
    env = "HalfCheetahPyBulletEnv-v0"
    hyper = load_hyperparameters(env)
    print(hyper)