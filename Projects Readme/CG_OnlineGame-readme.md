# CG_2DimensionOnlineGame

基于Socket框架的2D联机游戏项目，采用TCP协议实现房间系统和局内实时同步。

## 项目概述

- **架构**：客户端-服务器架构
- **网络协议**：TCP（可靠传输）+ UDP（预留）
- **数据格式**：JSON文本序列化
- **网络支持**：IPv4/IPv6双栈
- **同步模式**：状态同步（服务器权威）

## 项目结构
```
Assets/
├── Scripts/
│   ├── Client/                              # 客户端网络层
│   │   ├── NetworkManager.cs               # 网络连接管理
│   │   ├── NetworkRequestHandler.cs        # 网络请求处理器
│   │   ├── Room.cs                          # 房间数据模型
│   │   ├── RoomPanel.cs                     # 房间面板UI
│   │   ├── RoomUIItem.cs                   # 房间列表项UI
│   │   ├── InRoomPanel.cs                  # 房间内面板UI
│   │   ├── PlayerUIItem.cs                 # 玩家列表项UI
│   │   └── UIManager.cs                     # UI管理器
│   ├── GameIn_Controller/                   # 局内控制
│   │   ├── PlayerInitManager.cs            # 玩家初始化管理器
│   │   └── ThirdPersonCameraController.cs # 第三人称相机控制器
│   ├── GM/                                  # 游戏管理
│   │   └── GameManager.cs                  # 游戏管理器
│   └── NetworkMessage.cs                    # 网络消息定义与序列化
├── Socket_Server/                           # 服务端程序（.NET 8.0）
│   ├── GameServer.cs                       # 服务器主逻辑
│   ├── RoomManager.cs                      # 房间管理器
│   ├── RequestHandler.cs                   # 请求处理器
│   ├── Room.cs                             # 房间数据模型
│   ├── NetworkMessage.cs                   # 网络消息定义
│   ├── Program.cs                          # 程序入口
│   ├── GameServer.csproj                   # 项目配置文件
│   ├── AssemblyInfo.cs                     # 程序集信息
│   ├── StartServerAndUpdateDDNS.bat        # 启动脚本
│   └── bin/                                 # 编译输出目录
│       ├── Debug/
│       │   └── net8.0/
│       │       ├── GameServer.exe          # 调试版可执行文件
│       │       ├── GameServer.dll
│       │       └── GameServer.runtimeconfig.json
│       └── Release/
│           └── net8.0/
│               ├── GameServer.exe          # 发布版可执行文件
│               ├── GameServer.dll
│               └── GameServer.runtimeconfig.json
├── Scenes/                                 # Unity场景
│   ├── MainMenu.unity                      # 主菜单场景
│   ├── GameIn.unity                        # 游戏内场景
│   └── SampleScene.unity                   # 示例场景
├── Prefabs/                                # 预制体
│   ├── GameIn/                             # 游戏内预制体
│   │   ├── PlayerCharacter.prefab          # 玩家角色预制体
│   │   ├── PlayerInitManager.prefab        # 玩家初始化管理器预制体
│   │   └── fire/                           # 火球相关预制体
│   │       ├── Ball.prefab                  # 火球预制体
│   │       └── fire_pos.prefab              # 火球位置预制体
│   ├── Manager/                            # 管理器预制体
│   │   ├── ===GM===.prefab                  # 游戏管理器预制体
│   │   ├── Networck_Client.prefab           # 网络客户端预制体
│   │   └── UIManager.prefab                 # UI管理器预制体
│   └── UI/                                 # UI预制体
│       ├── MenuRoomPanel.prefab             # 菜单房间面板
│       ├── RoomInPanel.prefab               # 房间内面板
│       ├── RoomItem.prefab                  # 房间列表项
│       └── PlayerItem.prefab                # 玩家列表项
├── Plugins/                                # 插件
│   └── IngameDebugConsole/                 # 游戏内调试控制台
│       ├── Prefabs/
│       │   ├── DebugLogItem.prefab
│       │   └── CommandSuggestion.prefab
│       ├── Scripts/
│       │   ├── Attributes/
│       │   │   ├── ConsoleAttribute.cs
│       │   │   ├── ConsoleMethodAttribute.cs
│       │   │   └── ConsoleCustomTypeParserAttribute.cs
│       │   ├── DebugLogConsole.cs
│       │   ├── DebugLogManager.cs
│       │   ├── DebugLogItem.cs
│       │   ├── DebugLogPopup.cs
│       │   ├── DebugLogRecycledListView.cs
│       │   └── CircularBuffer.cs
│       ├── Sprites/                         # 调试控制台精灵图
│       ├── Editor/                          # 编辑器脚本
│       ├── Android/                         # Android平台支持
│       └── WebGL/                           # WebGL平台支持
├── Material/                               # 材质资源
│   ├── BasePlane.mat                       # 基础平面材质
│   ├── ball.mat                            # 球体材质
│   └── fire_pos.mat                        # 火球位置材质
├── Introduction/                           # 项目文档
│   ├── Past_Socket_Client.md               # 客户端开发记录
│   ├── Past_Socket_Server.md               # 服务端开发记录
│   └── Update_Log.md                       # 更新日志
└── Log_Analyse/                            # 日志分析
    ├── Player_in.log                       # 本地客户端日志
    └── Player_other.log                    # 其他客户端日志
```

plainText

## 核心功能

### 1. 房间系统
- 创建房间、加入房间、离开房间
- 房间列表实时同步
- 玩家列表更新
- 房主开始游戏

### 2. 局内同步
- 玩家初始化位置分配
- 实时位置同步（TCP）
- 场景切换协调
- 玩家状态管理

### 3. 网络特性
- 自动重连机制
- 消息队列处理（线程安全）
- 自定义JSON序列化器
- 多消息分离处理

## 快速开始

### 环境要求
- Unity 2020.3+
- .NET 8.0 SDK
- Windows系统

### 运行步骤

#### 1. 启动服务器
```bash
cd Assets/Socket_Server
dotnet run
```
或直接运行编译后的exe文件：
Assets/Socket_Server/bin/Debug/net8.0/GameServer.exe



服务器默认监听：
- TCP端口：6666
- UDP端口：6667

#### 2. 启动客户端
1. 打开Unity项目
2. 打开 `MainMenu.unity` 场景
3. 点击Play运行

客户端会自动连接到服务器（域名：gameconnection.dynv6.net）

### 游戏流程
1. **主菜单**：查看房间列表
2. **创建/加入房间**：输入房间名和玩家名
3. **房间内**：等待其他玩家加入
4. **开始游戏**：房主点击"开始游戏"
5. **局内对战**：实时位置同步

## 技术亮点

### 网络架构
- **双栈支持**：优先使用IPv6，兼容IPv4
- **线程安全**：使用ConcurrentQueue处理跨线程消息
- **消息分离**：自动处理TCP粘包问题（多JSON消息分离）

### 同步机制
- **状态同步**：客户端发送移动请求，服务器验证后广播
- **初始化协调**：服务器等待所有客户端完成场景切换后才开始同步
- **位置分配**：预设4个初始位置点，按需分配

### 代码设计
- **单例模式**：关键管理器使用单例
- **事件驱动**：使用委托和事件解耦模块
- **自定义序列化**：不依赖第三方库，手写JSON解析器

## 配置说明

### 服务器配置
编辑 `Assets/Socket_Server/Program.cs`：
```csharp
GameServer.Instance.Start(tcpPort: 6666, udpPort: 6667);
```

### 客户端配置
编辑 `Assets/Scripts/Client/NetworkManager.cs`：
```csharp
public string domain = "gameconnection.dynv6.net";  // 服务器域名
public int tcpPort = 6666;                          // TCP端口
public int udpPort = 6667;                          // UDP端口
```

## 日志分析

### 客户端日志
- Unity编辑器：Console窗口
- 打包后：`%USERPROFILE%/AppData/LocalLow/公司名/产品名/Player.log`

### 服务器日志
控制台输出，包含：
- 客户端连接/断开
- 消息收发记录
- 房间状态变化
- 错误信息

## 已知问题与优化方向

### 当前问题
1. TCP粘包处理需要进一步优化
2. 缺少碰撞检测的服务端验证
3. 未满员房间是否允许进入待完善

### 计划优化
1. 引入UDP传输高频消息（位置同步）
2. 实现插值平滑算法
3. 添加心跳检测和超时处理
4. 完善反作弊机制

## 学习资源

项目包含详细的技术文档：
- `Assets/Introduction/Past_Socket_Client.md` - 客户端开发记录
- `Assets/Introduction/Past_Socket_Server.md` - 服务端开发记录
- `Assets/Introduction/Update_Log.md` - 更新日志和需求分析

## 作者说明

本项目为学习Socket网络编程和Unity联机游戏开发的实践项目，持续优化中。

---

**注意**：本项目为学习项目，生产环境使用需进行安全加固和性能优化。