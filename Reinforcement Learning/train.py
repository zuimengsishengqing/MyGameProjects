import gym
import random
import torch
import numpy as np
from DQN import DQN, ReplayBuffer
from tqdm import tqdm
import matplotlib.pyplot as plt
from datetime import datetime
import os

"""TODO: 超参数设置区域"""
# -------------------------------
# 学习率
lr = 0.0005
# 总训练回合数
num_episodes = 1000
# 网络隐藏层维度(默认只有一层隐藏层,大家可以根据需求修改)
hidden_dim = 256
# 折扣因子
gamma = 0.99
# 探索率
epsilon = 0.05
# 目标网络更新频率
target_update = 50 
# 经验回放池容量
buffer_size = 10000
# 开始训练的最小数据量
minimal_size = 1000
# 批大小
batch_size = 256
# 随机种子(建议固定以复现结果)
_seed = 1553
random.seed(_seed)
np.random.seed(_seed)
torch.manual_seed(_seed)
# -------------------------------

"""TODO: 选择计算设备"""
device =  torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu") # 选择计算设备(默认使用GPU)

"""TODO: 环境初始化"""
env_name = 'Acrobot-v1'  # 选择环境('CartPole-v1', 'MountainCar-v0', 'Acrobot-v1')
env = gym.make(env_name)

"""TODO: 创建经验回放池实例"""
replay_buffer = ReplayBuffer(buffer_size)

"""确定状态和动作空间维度"""
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

if __name__ == "__main__":
    """"TODO: 创建DQN网络实例"""
    agent = DQN(state_dim, hidden_dim, action_dim, lr, gamma, epsilon, target_update, device)

    return_list = []
    for i_episode in (t := tqdm(range(num_episodes), desc="Episodes")):
        """"TODO: 训练主循环"""
        # 需要完成的操作：
        # 1. 重置环境并获取初始状态(HINT: 使用env.reset()),初始化done为False
        # 2. 进入循环,与环境交互,直到done为True
        # 3. 在循环中，根据当前状态选择动作
        # 4. 将经验存入经验回放池
        # 5. 如果经验回放池中的数据量大于等于minimal_size，则开始更新网络
        # 6. 将回合奖励加入return_list
        epi_rsum = 0
        agent.seed = i_episode
        state, _ = env.reset(seed=agent.seed)
        done = False
        while not done:
            action = agent.take_action(state)
            next_state, reward, term, trun, _ = env.step(action)
            done = term or trun #前项为真， 返回前项的值；前项为假，返回后项的值
            replay_buffer.add(state, action, reward, next_state, done)
            state = next_state
            if replay_buffer.size() >= minimal_size:
                b_s,b_a,b_r,b_ns,b_d = replay_buffer.sample(batch_size)
                transition_dict = {'states': b_s, 'actions': b_a, 'next_states': b_ns, 'rewards': b_r, 'dones': b_d}
                agent.update(transition_dict)
                #agent.update(b_s, b_a, b_r, b_ns, b_d) #update 输入
                
            epi_rsum += reward
            
            if done:
                break
            state = next_state
        t.set_postfix(total_reward=epi_rsum)
        return_list.append(epi_rsum)
        
        '''
        epi_rsum = 0
        agent.seed = i_episode
        env.reset(agent.seed)
        done = False
        # 2. 进入循环,与环境交互,直到done为True
        # 3. 在循环中，根据当前状态选择动作
        while not done:
            state = env.state
            action = agent.take_action(state) 
        # 4. 将经验存入经验回放池
            replay_buffer.add(state, action, reward, next_state, done)
            
            next_state, reward, done, _, _ = env.step(action)
        # 5. 如果经验回放池中的数据量大于等于minimal_size，则开始更新网络
            if replay_buffer.size() >= minimal_size:
                b_s,b_a,b_r,b_ns,b_d = replay_buffer.sample(batch_size)
                agent.update(b_s, b_a, b_r, b_ns, b_d)
                
        # 6. 将回合奖励加入return_list
            return_list.append(epi_rsum)
            '''


    """训练结果保存"""
    # -------------------------------
    # 获取当前时间戳
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 创建 checkpoint 下以 timestamp 为名称的子文件夹
    subfolder = os.path.join("checkpoint", timestamp)
    os.makedirs(subfolder, exist_ok=True)

    # 保存模型到子文件夹中
    filepath = os.path.join(subfolder, "model.pth")
    torch.save(agent.qnet.state_dict(), filepath) #我写的方法是qnet！

    # 绘制并保存图片到子文件夹中
    episodes_list = list(range(len(return_list)))
    plt.plot(episodes_list, return_list)
    plt.xlabel('Episodes')
    plt.ylabel('Returns')
    plt.title('DQN on {}'.format(env_name))
    plt.savefig(os.path.join(subfolder, "rewards.png"))
    plt.show()

    # -------------------------------
