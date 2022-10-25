import gym
import highway_env
from matplotlib import pyplot as plt
#%matplotlib inline

env = gym.make('highway-v0')
env.config["lanes_count"] = 2
#env.configure({
#    "action": {
#        "type": "ContinuousAction"
#    },
#    "policy_frequency": 15
#})
env.reset()
for _ in range(100):
    action = env.action_type.actions_indexes["IDLE"]
    obs, reward, done, truncated, info = env.step(action)
    env.render()

plt.imshow(env.render(mode="rgb_array"))
plt.show()