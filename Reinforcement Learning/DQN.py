import random
import numpy as np
import collections
import torch
import torch.nn as nn
import torch.nn.functional as F

class ReplayBuffer:
    """经验回放池"""
    def __init__(self, capacity):
        # 初始化经验回放池
        self.buffer = collections.deque(maxlen=capacity)

    def add(self, state, action, reward, next_state, done):
        """TODO: 向缓冲区添加一个transition"""
        # 参数说明：
        # state: 当前状态
        # action: 执行的动作
        # reward: 获得的奖励
        # next_state: 下一个状态
        # done: 是否终止
        self.buffer.append((state, action, reward, next_state, done))
        pass

    def sample(self, batch_size):
        """TODO: 从缓冲区中采样一个批量的transition"""
        """HINT: 使用random.sample()采样, 通过zip(*)将数据解包"""
        # 返回格式说明：
        # states, actions, rewards, next_states, dones
        transition = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*transition)
        return np.array(states), actions, rewards, np.array(next_states),dones
        pass

    def size(self):
        """TODO: 返回当前缓冲区中的数据数量"""
        return len(self.buffer)
        pass


class Qnet(nn.Module):
    """Q网络定义(默认只有一层隐藏层,大家可以根据需求修改)"""
    def __init__(self, state_dim, hidden_dim, action_dim):
        super(Qnet, self).__init__()
        """TODO: 构建网络层"""
        # 输入层到隐藏层的线性层
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        # 隐藏层到输出层的线性层
        self.fc2 = nn.Linear(hidden_dim, action_dim)
        
        
        
    def forward(self, x):
        """TODO: 前向传播过程"""
        # ReLU作为激活函数：
        x = F.relu(self.fc1(x))
        return self.fc2(x)
        pass


class DQN:
    """DQN算法主体"""
    def __init__(self, state_dim, hidden_dim, action_dim, learning_rate, gamma,
                 epsilon, target_update, device):
        """TODO: 初始化Q网络和目标网络"""
        self.qnet = Qnet(state_dim, hidden_dim, action_dim).to(device)
        self.targetnet = Qnet(state_dim, hidden_dim, action_dim).to(device)
        """TODO: 初始化优化器(Adam etc.)"""
        self.optimizer = torch.optim.Adam(self.qnet.parameters(), lr=learning_rate)
        """TODO: 设置算法参数"""
        self.gamma = gamma
        self.epsilon = epsilon
        self.target_update = target_update #更新频率
        self.action_dim = action_dim
        self.count = 0
        self.learning_rate = learning_rate## 学习率,手动输入值设定计算？
        self.device = device
        
        # 参数：折扣因子 探索概率 目标网络更新频率 动作维度 计数器(用于定期更新目标网络) 计算设备

    def take_action(self, state):
        """TODO: epsilon-贪婪策略选择动作"""
        """HINT: .argmax().item()返回tensor中最大值的索引, 并转换为Python整数"""
        # 输入说明：
        # state: numpy数组格式的观测状态(HINT:使用torch.from_numpy转化为张量)
        # 返回说明：
        # action: 动作值
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.action_dim)
        else:      
            #state = torch.tensor([state], dtype=torch.float).to(self.device)
            state = torch.from_numpy(state).to(self.device)
            # state: numpy数组格式的观测状态(HINT:使用torch.from_numpy转化为张量)
            #state = torch.from_numpy(state).float().unsqueeze(0).to(self.device)
            action = self.qnet(state).argmax().item()
        return action
        pass

    def update(self, transition_dict):
        """TODO: 网络更新"""
        # 需要完成的操作：
        # 1. 从transition_dict中提取数据并转换为张量(注意size)
        # 2. 计算当前Q值(HINT: 使用.gather())
        # 3. 计算目标Q值(TD误差目标)
        # 4. 计算损失(HINT: 使用均方误差F.mse_loss)
        # 5. 梯度清零,反向传播,参数更新
        # 6. 定期更新目标网络
        
        # 参数说明：
        # transition_dict: 包含多个transition的字典
        
        # 1. 从transition_dict中提取数据并转换为张量(注意size)
        states = torch.tensor(transition_dict['states'], dtype=torch.float).to(self.device)
        actions = torch.tensor(transition_dict['actions'], dtype=torch.int64).view(-1, 1).to(self.device)# 注意actions是整数索引,需要转换为张量并添加额外维度
        rewards = torch.tensor(transition_dict['rewards'], dtype=torch.float).view(-1, 1).to(self.device)
        nextstates = torch.tensor(transition_dict['next_states'], dtype=torch.float).to(self.device)
        dones = torch.tensor(transition_dict['dones'], dtype=torch.float).view(-1, 1).to(self.device)
        # 2. 计算当前Q值(HINT: 使用.gather())
        q_value = self.qnet(states).gather(1, actions)# 计算当前Q值
        # 3. 计算目标Q值(TD误差目标)
        q_next_maxvalue = self.targetnet(nextstates).max(1)[0].view(-1,1)# 计算目标Q值
        td_target = rewards + (1-dones) * self.gamma * q_next_maxvalue# TD误差（1-dones)* (q_next_maxvalue - q_value)?  s+1时候不存在Q_{i+1}，故乘以因子：(1-dones) 
        # 4. 计算损失(HINT: 使用均方误差F.mse_loss)
        loss = F.mse_loss(td_target, q_value)# 均方差计算损失
        # 5. 梯度清零,反向传播,参数更新
        self.optimizer.zero_grad()# 梯度清零，直接调用优化器方法
        loss.backward()# 反向传播，调用损失的backward方法，不用自己写...
        self.optimizer.step()#  参数更新，也是直接调用优化器方法就行
        self.count += 1  #计数器更新
        # 6. 定期更新目标网络
        if self.count % self.target_update == 0:
            self.targetnet.load_state_dict(self.qnet.state_dict())# 定期更新目标网络
        
        
        pass