# UnityDemo - 密室逃脱游戏

## 项目简介

这是一款第一人称解密逃出密室游戏,玩家在逃脱过程中意外触发无尽循环。本项目为7天GameJam开发作品,实现了基础玩法流程和核心交互系统。

## 技术栈

- **引擎**: Unity
- **语言**: C#
- **主要资源包**:
  - BasicBedroomPack-Mavi3D (场景资源)
  - AN Interactive Physical Door Pack (门交互系统)
  - TextMesh Pro (UI文本)
  - Unity Standard Assets (第一人称控制器)

## 核心功能

- 第一人称视角控制
- 物品收集与物品栏系统
- 场景切换与关卡管理
- 物品交互系统(门、抽屉、开关等)
- 玩家状态管理

## 文件结构
```
UnityDemo/
├── Assets/
│   ├── Scenes/                              # 场景文件
│   │   ├── SampleScene.unity                # 主场景
│   │   └── SampleScene/                     # 场景数据
│   │       └── NavMesh.asset                # 导航网格
│   │
│   ├── ScriptInDemo/                        # 游戏核心脚本
│   │   ├── Player_Controller_In_Demo.cs     # 玩家控制器
│   │   ├── InventorySystem.cs              # 物品栏系统
│   │   ├── PickupItem.cs                   # 物品拾取
│   │   ├── Game_UI_Scene_Changer.cs        # 场景切换
│   │   ├── DoorController.cs               # 门控制
│   │   ├── PlayerManager.cs                # 玩家管理器
│   │   ├── DrawerController.cs             # 抽屉控制器
│   │   ├── GlassDoorController.cs          # 玻璃门控制器
│   │   ├── GlassDoor.cs                    # 玻璃门脚本
│   │   ├── ItemSlot.cs                     # 物品槽
│   │   ├── ItemPickedUpEvent.cs            # 物品拾取事件
│   │   ├── SelectHighlight.cs              # 选中高亮
│   │   ├── PinCard.cs                      # 门卡
│   │   ├── PincardController.cs           # 门卡控制器
│   │   ├── End_Stone.cs                    # 结束石
│   │   ├── FlickeringLight.cs              # 闪烁灯光
│   │   ├── Lever_Spin.cs                   # 拉杆旋转
│   │   ├── Ladder_TO_Change_Scene.cs       # 梯子场景切换
│   │   ├── Log_Back.cs                     # 日志返回
│   │   ├── SceneToggle.cs                  # 场景切换
│   │   ├── SimpleSceneLoadHandler.cs      # 简单场景加载
│   │   ├── SpinHouse.cs                    # 房屋旋转
│   │   ├── Water_Uping.cs                  # 水位上升
│   │   └── readin.cs                       # 读取脚本
│   │
│   ├── UIScript/                            # UI脚本
│   │   ├── Player_say.cs                   # 玩家对话
│   │   ├── NpcTalk.cs                      # NPC对话
│   │   └── NpcTalk1.cs                     # NPC对话1
│   ├── Old Sea Port/                        # 旧海港资源
│   ├── Crystal_Mine/                        # 水晶矿资源
│   ├── Free Island Collection/              # 免费岛屿资源
│   ├── Fillefranz/                          # Fillefranz工具
│   ├── Vefects/                             # 特效资源
│   ├── asset_store/                         # 资源商店资源
│   ├── Editor/                              # 编辑器脚本
│   └── Scenes 1/                            # 备用场景
```

plainText

## 快速开始

### 环境要求

- Unity 2020.3 或更高版本
- Windows 操作系统

### 运行步骤

1. **下载项目**
   - 从网盘下载项目压缩包
   - 解压到本地目录

2. **打开项目**
   - 启动 Unity Hub
   - 点击"添加项目"
   - 选择解压后的 `UnityDemo` 文件夹
   - 等待 Unity 导入项目资源

3. **运行游戏**
   - 在 Unity 编辑器中打开 `Assets/Scenes/SampleScene.unity`
   - 点击顶部工具栏的播放按钮 (▶)
   - 按空格键开始游戏

### 游戏操作

- **WASD**: 移动
- **鼠标**: 视角控制
- **E**: 交互/拾取物品
- **空格**: 开始游戏/跳跃
- **数字键1-9**: 切换物品栏

## 游戏流程

1. 按空格键进入游戏世界
2. 探索密室环境,寻找线索和物品
3. 收集钥匙等关键道具
4. 解开门锁和机关,寻找出口
5. 逃脱过程中触发循环机制

## 项目亮点

- 完整的第一人称交互系统
- 模块化的物品栏系统
- 灵活的场景切换机制
- 可扩展的物品交互框架

## 注意事项

- 本项目为GameJam作品,暂未添加流程指引提示
- 建议结合代码注释理解游戏逻辑
- 核心脚本位于 `Assets/ScriptInDemo/` 目录

## 联系方式

如有疑问,请通过简历提供的联系方式联系。