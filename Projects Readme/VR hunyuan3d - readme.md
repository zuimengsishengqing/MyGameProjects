# VR融合创作平台 - 远程语音生3D系统

## 项目概述

这是一个基于Unity XR的VR创作平台，集成腾讯混元3D（Hunyuan3D）模型，支持远程VR环境中的语音实时生成3D模型。项目采用客户端-服务器架构，通过IPv6网络实现跨地域协作。

## 核心功能

- **语音转3D**：在VR环境中通过语音描述实时生成3D模型
- **远程协作**：基于IPv6的客户端-服务器架构，支持远程访问
- **模型生成**：集成Hunyuan3D大模型，支持多种生成风格
- **纹理生成**：自动生成模型纹理贴图（法线、金属度、粗糙度等）
- **实时交互**：Unity VR环境中的实时模型预览和交互

## 项目结构

```
XR_homeworkZip/
├── Server/                                    # 服务端代码
│   └── hunyuan3d_ipv6_server.py              # Python服务器（FastAPI + IPv6）
├── VR Integrated Creation Platform/         # Unity VR客户端项目
│   ├── Assets/                              # Unity资源目录
│   │   ├── Script/                          # 核心脚本目录
│   │   │   ├── Remote_3D/                   # 远程3D生成模块
│   │   │   │   ├── remote_Hunyuan3d.cs     # 混元3D服务器通信
│   │   │   │   ├── SpeechUIController.cs   # 语音UI控制器
│   │   │   │   ├── AudioManager.cs          # 音频管理器
│   │   │   │   └── SimpleTranslationManager.cs # 简单翻译管理器
│   │   │   ├── UI/                         # 用户界面模块
│   │   │   │   ├── UIPanelController.cs    # UI面板控制器
│   │   │   │   └── MessageShow.cs          # 消息显示
│   │   │   ├── RuntimeSave/                # 运行时保存模块
│   │   │   │   ├── CubeAutoSaveLogic.cs    # 立方体自动保存逻辑
│   │   │   │   ├── CubeDataSpawnManager.cs # 立方体数据生成管理器
│   │   │   │   └── ObjPathComponent.cs     # 对象路径组件
│   │   │   ├── ObjControll/                # 对象控制模块
│   │   │   │   └── SelectedObj_Controller.cs # 选中对象控制器
│   │   │   ├── RayPaint/                   # 射线绘制模块
│   │   │   │   ├── ControllerRayVisual_OVERRIDE.cs
│   │   │   │   └── RayInteractorCursorVisual_OVERRIDE.cs
│   │   │   ├── Generated_Obj/               # 生成对象模块
│   │   │   │   └── Generated_Obj_JS.cs     # 生成对象JavaScript桥接
│   │   │   ├── User_Controller.cs          # 用户控制器
│   │   │   ├── MoveControll_VR_1.cs        # VR移动控制
│   │   │   ├── RayInteractor_OVERRIDE.cs   # 射线交互器重写
│   │   │   ├── RayInteractable_OVERRIDE.cs # 射线可交互对象重写
│   │   │   ├── DistanceGrabInteractor_OVERRIDE.cs
│   │   │   └── DistanceGrabInteractable_OVERRIDE.cs
│   │   ├── Scenes/                         # 场景文件
│   │   │   └── SampleScene.unity          # 主场景
│   ├── Assembly-CSharp.csproj              # 主程序集项目文件
│   ├── XR low.sln                          # Unity解决方案
│   └── RuntimeActionBindings.json          # XR动作绑定配置
├── AR融合创作平台.pptx                      # 项目演示文稿
└── Matrix宁尚哲.pptx                        # 个人简历演示

```

## 技术栈

### 服务端
- **Python 3.8+**
- **FastAPI** - Web框架
- **Uvicorn** - ASGI服务器
- **Pydantic** - 数据验证
- **IPv6/DDNS** - 动态域名解析

### 客户端
- **Unity 2022+**
- **XR Interaction Toolkit** - VR交互
- **C#** - 核心逻辑
- **Carter Games Save Manager** - 数据管理

## 快速开始

### 环境要求

**服务端：**
- Python 3.8 或更高版本
- Conda环境管理器
- Hunyuan3D模型环境（联系作者获取）

**客户端：**
- Unity 2022.3 或更高版本
- VR设备（Oculus Quest、HTC Vive等）
- Windows 10/11

### 服务端部署

1. **安装依赖**
```bash
pip install fastapi uvicorn pydantic
```

2. **配置Conda环境**
```bash
conda create -n hunyuan3d python=3.8
conda activate hunyuan3d
# 安装Hunyuan3D相关依赖（联系作者获取）
```

3. **启动服务器**
```bash
cd Server
python hunyuan3d_ipv6_server.py
```

服务器将在 `http://[::]:18082` 启动，支持IPv6访问

### 客户端使用

1. **打开Unity项目**
   - 使用Unity 2022.3或更高版本打开 `VR Integrated Creation Platform` 文件夹

2. **配置服务器地址**
   - 在Unity编辑器中找到服务器配置脚本
   - 设置服务器地址：`ai.hunyuan3dvrconnect.dynv6.net:18082`

3. **构建并运行**
   - 选择目标VR平台（如Oculus Quest）
   - 点击 `File > Build Settings` 构建应用
   - 在VR设备上安装并运行

4. **使用流程**
   - 在VR环境中进入创作场景
   - 使用麦克风输入语音描述（如"生成一只可爱的卡通猫"）
   - 等待服务器生成3D模型
   - 在VR环境中查看和交互生成的模型

## API接口

服务端提供以下主要接口：

- `GET /` - 服务状态信息
- `GET /status` - 服务器健康状态
- `POST /test-connectivity` - 连通性测试
- `POST /generate-from-text` - 文本生成3D模型
- `GET /files/list` - 获取生成文件列表
- `GET /files/download-all` - 下载所有生成文件


## 项目亮点

1. **创新交互方式**：将语音识别与3D生成结合，提供直观的VR创作体验
2. **网络架构**：基于IPv6的远程访问，支持跨地域协作
3. **实时生成**：集成大模型实现快速3D模型生成
4. **完整流程**：从语音输入到模型生成、纹理贴图的全流程自动化

## 注意事项

- Hunyuan3D模型文件较大，未包含在本项目中，如需完整功能请联系作者
- 确保网络环境支持IPv6访问
- 首次运行需要下载Unity XR相关插件
- VR设备需满足最低性能要求

## 联系方式

**开发者**：宁尚哲  
**邮箱**：1114651650@qq.com  
**项目说明**：本作品为个人VR课程大作业项目，展示VR、AI、网络编程等综合能力

## 演示资料

- [AR融合创作平台.pptx](./AR融合创作平台.pptx) - 项目功能演示
- [Matrix宁尚哲.pptx](./Matrix宁尚哲.pptx) - 个人简历与项目介绍

---

**感谢您的阅读！**