import gym
import random
import torch
import numpy as np
from DQN import Qnet
from tqdm import tqdm
from train import epsilon, hidden_dim, env_name, _seed, device

""""TODO: 参数设置"""
# 网络隐藏层维度(必须与训练时一致)
#hidden_dim = 1
# 环境名称(需与训练环境匹配)
#env_name = 'CartPole-v1' # 'Acrobot-v1' 'MountainCar-v0'
env = gym.make(env_name, render_mode="human")
# 随机种子(建议与训练时相同)
#_seed = 1553
random.seed(_seed)
np.random.seed(_seed)
torch.manual_seed(_seed)
# 模型路径
model_path = './checkpoint/20250513_182531/model.pth'
state_dict = torch.load(model_path)
# 计算设备
#device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu") # 选择计算设备(默认使用GPU)

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

"""TODO: Q网络初始化"""
# 需要完成的操作：
# 1. 创建网络实例
# 2. 加载模型参数(HINT: 使用load_state_dict)
# 3. 设置为评估模式
def Qnet_init():
    qnet = Qnet(state_dim, hidden_dim, action_dim)
    qnet.load_state_dict(state_dict)
    qnet.eval()
    return qnet

qnet = Qnet_init() # 初始化Q网络

"""TODO: 实现策略函数(HINT: 与DQN中的take_action类似)"""
def policy(state):
    # 输入说明：
    # state: 状态值
    # 返回说明：
    # action: 动作值
    if np.random.random() < epsilon:
        action = np.random.randint(action_dim)
        
    else:
        state = torch.tensor([state], dtype=torch.float).to(device)
        action = qnet(state).argmax().item()
    return action
    pass

"""TODO: 实现环境交互逻辑"""
state, _ = env.reset(seed=_seed)
done = False

num_episodes = 10
success_num = 0
for i_episode in tqdm(range(num_episodes), desc="Episodes"):
        # 1. 重置环境并获取初始状态,初始化done为False
        # 2. 进入循环,与环境交互,直到done为True
        # 3. 在循环中，根据当前状态选择动作

        state, _ = env.reset(seed=_seed)
        done = False
        #类比train.py里面的while not done:
        while not done:
            action = policy(state)
            next_state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            # 4. 渲染环境(HINT: 使用env.render())
            env.render()
            if done == True:
                break
            state = next_state      
            
        if terminated:
            if env_name == 'Acrobot-v1' or env_name == 'MountainCar-v0':
                success_num += 1
        if truncated:
            if env_name == 'CartPole-v1':
                success_num += 1

print(f"Success rate: {success_num / num_episodes:.2%}")


