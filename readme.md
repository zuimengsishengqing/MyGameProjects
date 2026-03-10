# Dynamic Dancer

音乐节奏融合地图移动玩法的3D游戏项目

## 项目简介

Dynamic Dancer 是一款创新的节奏游戏，将传统音乐节奏玩法与地图移动机制相结合。玩家需要在音乐节拍上完成节奏判定，同时在动态生成的地图上进行移动和探索。

## 核心玩法

- **音乐节奏系统**：基于音乐节拍的Note判定，支持多种判定等级
- **地图移动机制**：动态生成的地图包含多种地块类型（基础地块、障碍地块、移动地块、终点地块）
- **关卡系统**：支持多个自定义关卡，每个关卡包含独立的地图和谱面
- **评分系统**：实时评分和历史最高分记录

## 技术特点

### 游戏架构
- **单例模式**：GameManager全局管理游戏状态和场景切换
- **UI系统**：基于Panel的UI管理框架，支持动态界面切换
- **数据持久化**：JSON格式存储地图数据、谱面数据和玩家成绩

### 核心模块
- **地图编辑器**：可视化编辑器，支持创建和测试自定义地图
- **谱面编辑器**：实时录制和编辑音乐节奏谱面
- **节奏判定系统**：精确的时机判定算法
- **玩家移动系统**：基于地块类型的移动逻辑

### 技术栈
- **Unity引擎**：核心游戏引擎
- **C#**：主要开发语言
- **Unity Input System**：输入管理
- **JSON序列化**：数据存储

## 项目结构

```
Assets/
├── Script/                          # 核心脚本目录
│   ├── GameControll/               # 游戏全局控制
│   │   └── GameManager.cs          # 游戏管理器（单例模式），管理场景切换、游戏状态
│   ├── GameIn/                     # 游戏内逻辑
│   │   ├── MapLoader.cs            # 地图加载器，从JSON加载地图数据并生成场景
│   │   └── PlayerHealth.cs         # 玩家生命值系统
│   ├── Map_Player/                 # 地图编辑器和玩家控制
│   │   ├── MapEditorManager.cs     # 地图编辑器管理器，处理地块编辑和保存
│   │   ├── MoveLandController.cs   # 移动地块控制器
│   │   └── PlayerMovement.cs       # 玩家移动控制，处理地块间的移动逻辑
│   ├── MusicTypeMaker/             # 谱面编辑器和节奏判定
│   │   ├── SimpleChartRecorder.cs  # 简易谱面录制器
│   │   ├── NoteMover.cs            # 音符移动控制
│   │   ├── EffectFadeOut.cs        # 特效淡出效果
│   │   ├── RhythmGamePlayer.cs     # 节奏游戏播放器，管理音乐和谱面
│   │   └── JudgmentSystem.cs       # 判定系统，处理音符判定和评分
│   ├── UI/                         # UI系统
│   │   ├── UIManager.cs            # UI管理器（单例模式），管理所有UI面板切换
│   │   ├── UIPanel.cs              # UI面板基类
│   │   ├── GameSettingsData.cs     # 游戏设置数据
│   │   ├── LevelItemUI.cs          # 关卡列表项UI组件
│   │   └── Panels/                 # 各功能面板
│   │       ├── MainMenuPanel.cs    # 主菜单面板
│   │       ├── GameModePanel.cs    # 游戏模式选择面板
│   │       ├── LevelBrowserPanel.cs # 关卡浏览面板
│   │       ├── LevelChoicePanel.cs # 关卡选择面板
│   │       ├── OnlineHallPanel.cs  # 在线大厅面板
│   │       ├── SettingsPanel.cs    # 设置面板
│   │       └── FinalScoreRatingPanel.cs # 最终评分面板
│   └── Level_Broswer/              # 关卡浏览和管理
│       ├── LevelData.cs            # 关卡数据结构
│       └── LevelManager.cs         # 关卡管理器
├── MapSaving/                      # 地图数据存储
│   ├── Test_Map/                   # 测试地图
│   └── level_*/                    # 各关卡地图数据（JSON格式）
├── MusicTypeSaving/                # 谱面数据存储
│   ├── Test_Level/                 # 测试关卡谱面
│   └── level_*/                    # 各关卡谱面数据（JSON格式）
├── HistoryScoreSaving/             # 历史成绩存储
│   └── Level_Mode/                 # 各关卡历史最高分（JSON格式）
├── Material/                       # 材质资源
│   ├── Map_Material/               # 地图材质（基础地块、障碍地块、移动地块、终点地块）
│   └── player/                     # 玩家材质（正常状态、受伤状态）
└── Personal/                       # 个人资源文件
    ├── Light/                      # Light主题资源
    │   └── Music/                  # 音乐文件
    └── ZuiMeng/                    # ZuiMeng主题资源
        ├── Image/                  # 图片资源
        ├── Music/                  # 音乐文件
        └── Prefab/                 # 预制体
            ├── GameControl/        # 游戏控制预制体
            ├── Gamein/             # 游戏内预制体
            ├── Map/                # 地图预制体
            └── MusicTypeMaker/     # 谱面编辑器预制体
```



## 如何使用

### 运行项目

1. **环境要求**
   - Unity 6或更高版本
   - Windows 操作系统

2. **打开项目**
   - 使用Unity Hub打开项目文件夹
   - 等待Unity完成项目初始化

3. **运行游戏**
    手机包体：
   - Dynamic Dancer\Build路径下，直接找到apk，在手机安装即可游玩。
   Unity 编辑器内：
   - 打开 `Menu` 场景
   - 点击Unity编辑器顶部的播放按钮


### 游戏操作

- **主菜单**：选择游戏模式（单人模式、在线模式），目前只有GameChoice - level mode - Demo Level
- **关卡选择**：浏览并选择要游玩的关卡
- **游戏内**：
  - 移动：WASD 或 方向键
  - 节奏判定：在Note到达判定圈时按下对应四个按钮，可以向对应方向移动，编辑器（电脑内）可以qwas四个方向按键移动。

### 编辑器使用

#### 地图编辑器
1. 进入 `EditorScene` 场景
2. 使用工具栏选择地块类型
3. 在场景中点击放置地块
4. 保存地图数据

#### 谱面编辑器
1. 进入 `ChartEditorScene` 场景
2. 选择音乐文件
3. 播放音乐并录制节奏
4. 调整Note位置和时间
5. 保存谱面数据

## 开发状态

- 当前版本：开发中
- 已完成功能：
  - 基础游戏循环
  - demo关卡
  - 地图编辑器
  - 谱面编辑器
  - 评分系统
  - UI系统
- 待开发功能：
  - 在线多人模式
  - 更多音乐曲目
  - 成就系统

## 项目亮点

- 创新的节奏+地图玩法融合
- 完整的编辑器工具链
- 模块化的代码架构
- 良好的扩展性设计

## 联系方式
宁尚哲 
1114651650@qq.com
本项目为Golden Eggs兼职开发项目。

---

**注意**：本项目处于开发阶段，部分功能可能存在bug或未完成。