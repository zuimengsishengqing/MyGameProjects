# 《非暴露测试》- Meta类游戏项目

## 项目概述

《非暴露测试》是一款创新的Meta类游戏，玩家从2D场景开始游玩，意外卡bug进入3D世界进行探索。本项目采用Unity引擎开发，融合了2D与3D双重视角，包含多样化的小游戏系统和沉浸式交互体验。

**角色定位**：TapTap聚光灯开发项目 - 副程序

## 技术栈

- **游戏引擎**：Unity 2021+
- **编程语言**：C#
- **UI框架**：Unity UGUI、TextMeshPro
- **3D相机系统**：Cinemachine
- **音频系统**：Unity Audio Mixer、3D空间音效
- **渲染管线**：Universal Render Pipeline (URP)
- **插件库**：
  - PlayMaker（可视化状态机）
  - DOTween（动画系统）
  - Odin Inspector（开发工具）
  - UniTask（异步任务管理）

## 项目结构
```
MangoClub/
├── Assets/
│   ├── Folder_Dreamer/              # 核心代码贡献目录
│   │   ├── Script/                  # 游戏脚本
│   │   │   ├── Num_table/           # 数字计算游戏模块
│   │   │   │   └── NumberGame.cs    # 数字运算逻辑实现
│   │   │   ├── Memory_Cards/        # 记忆卡牌游戏模块
│   │   │   │   └── Memory_Cards_Game.cs  # 卡片匹配逻辑实现
│   │   │   ├── Reaction_Game_Awake/ # 反应测试游戏模块
│   │   │   │   └── Reaction_Game.cs # 反应点击逻辑实现
│   │   │   ├── Tap_Response_Game/   # 点击响应游戏模块
│   │   │   │   └── Tap_Response_Game.cs  # Windows弹窗模拟逻辑
│   │   │   ├── Virus_UI/            # 病毒UI效果模块
│   │   │   │   └── Virus_Controller.cs   # 病毒特效控制逻辑
│   │   │   └── Tri3D/               # 3D世界交互系统模块
│   │   ├── Prefabs/                 # 游戏预制体
│   │   ├── 3DWorld_Test.unity       # 3D探索场景
│   │   └── Computer_UI.unity        # 2D计算机界面场景
│   ├── Scripts/                     # 全局管理脚本
│   │   ├── GameManager.cs           # 游戏全局管理器
│   │   └── App.cs                   # 应用程序状态管理
│   └── Scenes/                      # 其他场景文件
└── ProjectSettings/                 # 项目配置
```

plainText

## 核心功能模块

### 1. 多样化小游戏系统

#### 数字计算游戏 (NumberGame)
- 实现动态难度调整机制，根据玩家进度自动提升题目复杂度
- 支持多种运算符组合（加、减、乘）
- 使用栈算法实现表达式优先级计算
- 实时反馈与分数系统

#### 记忆卡牌游戏 (Memory_Cards_Game)
- 动态生成卡牌网格，支持4-12张卡牌自适应布局
- 实现随机洗牌算法确保每次游戏体验不同
- 卡牌匹配逻辑与状态管理系统
- 视觉反馈与音效联动

#### 反应测试游戏 (Reaction_Game)
- 多行随机区域生成系统
- 光标移动与点击判定机制
- 基于玩家表现的难度动态调整
- 精确的时间控制与动画同步

#### 点击响应游戏 (Tap_Response_Game)
- 进度条控制系统
- 动态窗口生成与按钮交互
- 多级难度递进设计

### 2. 3D场景交互系统

- **玩家控制**：第一人称视角探索，支持WASD移动与鼠标视角控制
- **场景加载**：异步场景加载机制，实现2D到3D的无缝切换
- **门禁系统**：交互式门禁控制，触发特定事件
- **3D音效**：基于位置的空间音效系统

### 3. UI交互框架

- **病毒UI效果**：模拟系统崩溃的视觉特效
- **屏幕遮挡**：动态屏幕遮挡与颜色渐变
- **光标控制**：自定义光标样式与加载状态
- **设置系统**：完整的游戏设置界面（音量、画质等）

### 4. 游戏状态管理

- **全局状态管理**：通过App类实现跨场景数据共享
- **进度追踪**：记录玩家完成的游戏数量与难度等级
- **数据持久化**：保存玩家进度与游戏状态

## 个人技术贡献

### 核心代码实现

1. **模块化架构设计**
   - 设计独立的小游戏模块，每个游戏拥有独立的Awake、Start、Update生命周期
   - 实现统一的接口规范，便于扩展新游戏类型
   - 采用事件驱动模式，降低模块间耦合度

2. **性能优化**
   - 使用对象池技术优化UI元素生成
   - 异步加载场景与资源，减少卡顿
   - 优化算法复杂度，确保游戏流畅运行

3. **用户体验提升**
   - 实现平滑的动画过渡效果
   - 精心设计的视觉反馈系统
   - 完善的音效与背景音乐管理

4. **技术难点解决**
   - 实现数学表达式的优先级计算
   - 解决多场景数据同步问题
   - 优化随机算法确保游戏公平性

### 代码质量

- 遵循SOLID设计原则
- 代码注释清晰，便于维护
- 采用面向对象编程思想
- 实现完整的错误处理机制

## 项目成果

- 成功开发5个独立小游戏模块
- 实现2D与3D场景无缝切换
- 构建完整的游戏状态管理系统
- 优化游戏性能，帧率稳定在60FPS以上
- 提供沉浸式的游戏体验

## 如何使用

### 环境要求

- Unity 2021.3 或更高版本
- Windows 10/11 操作系统
- 至少 8GB RAM
- 支持DirectX 11的显卡

### 运行步骤

1. **打开项目**
   - 使用Unity Hub打开项目根目录
   - 等待Unity完成项目索引

2. **打开场景**
   - 进入 `Assets/Folder_Dreamer/` 目录
   - 双击打开 `Computer_UI.unity`（2D起始场景）
   - 或打开 `3DWorld_Test.unity`（3D探索场景）

3. **运行游戏**
   - 点击Unity编辑器顶部的"Play"按钮
   - 或使用快捷键 `Ctrl + P`

4. **打包发布**
   - 进入 `File > Build Settings`
   - 选择目标平台（Windows、Mac等）
   - 点击"Build"生成可执行文件

### 推荐游玩流程

1. 从 `Computer_UI` 场景开始，体验2D小游戏
2. 完成小游戏后触发bug，进入3D世界
3. 在3D世界中探索，触发各种事件
4. 体验完整的游戏流程

## 代码亮点

### 动态难度系统

```csharp
// 根据玩家完成的游戏数量动态调整难度
if (App.Ist.countAllGame == 0) {
    // 简单模式
} else if (App.Ist.countAllGame == 1) {
    // 中等模式
} else if (App.Ist.countAllGame >= 2) {
    // 困难模式
}
```

### 表达式计算算法

```csharp
// 使用栈实现数学表达式优先级计算
private int CalculateExpressionWithPriority(string expression) {
    // 实现乘法优先于加减法的计算逻辑
}
```

### 异步场景加载

```csharp
// 使用协程实现平滑的场景切换
IEnumerator LoadSceneAsync(string sceneName) {
    AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(sceneName);
    while (!asyncLoad.isDone) {
        // 显示加载进度
        yield return null;
    }
}
```

## 联系方式

如有任何问题或建议，欢迎通过以下方式联系：

- 邮箱：[您的邮箱]
- GitHub：[您的GitHub地址]
- TapTap：[您的TapTap主页]

---

**注**：本项目已打包上传至网盘，如需完整项目文件请联系获取。