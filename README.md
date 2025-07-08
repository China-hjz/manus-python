# Manus Replica - AI Agent 复刻版

这是一个使用Python复刻的Manus AI助手，包含核心功能架构、工具调用系统、任务规划和执行能力。

## 项目结构

```
manus_replica/
├── agent.py              # 核心Agent类
├── tool_registry.py      # 工具注册表
├── task_planner.py       # 任务规划器
├── context_manager.py    # 上下文管理器
├── tools.py              # 基础工具集
├── web_agent.py          # Web版本Agent
├── app.py                # Flask后端服务器
├── main.py               # 命令行版本入口
├── README.md             # 项目文档
└── manus-ui/             # React前端界面
    ├── src/
    │   ├── App.jsx       # 主应用组件
    │   └── ...
    ├── package.json
    └── ...
```

## 核心功能

### 1. Agent核心循环
- 接收用户输入
- 分析和思考
- 选择合适的工具
- 执行工具调用
- 处理观察结果
- 返回响应

### 2. 工具系统
- **文件操作**: 读取、写入、追加、替换文件内容
- **Shell执行**: 执行系统命令
- **消息通知**: 向用户发送通知
- **可扩展**: 支持注册新工具

### 3. 任务规划
- 任务分解和阶段管理
- 阶段推进逻辑
- 错误处理和重试机制

### 4. 用户界面
- **命令行界面**: 简单的交互式命令行
- **Web界面**: 现代化的React前端 + Flask后端

## 快速开始

### 命令行版本

```bash
cd manus_replica
python3.11 main.py
```

### Web版本

1. 启动后端服务器：
```bash
cd manus_replica
python3.11 app.py
```

2. 启动前端开发服务器：
```bash
cd manus_replica/manus-ui
npm run dev
```

3. 访问 http://localhost:5173

## 依赖要求

### Python依赖
- Python 3.11+
- Flask
- flask-cors

### 前端依赖
- Node.js 20+
- React
- Tailwind CSS
- shadcn/ui

## 使用示例

### 文件操作
发送包含"文件"关键词的消息，Agent会自动创建测试文件。

### Shell命令
发送包含"命令"或"shell"关键词的消息，Agent会执行测试命令。

## 架构设计

### 核心组件
1. **Agent Core**: 代理核心循环和执行引擎
2. **Tool Management**: 工具注册和调用系统
3. **Task Planning**: 任务规划和阶段管理
4. **Context Management**: 上下文和状态管理
5. **Communication Interface**: 用户交互界面

### 数据流
用户输入 → Agent分析 → 工具调用 → 结果处理 → 用户输出

## 扩展性

### 添加新工具
1. 在 `tools.py` 中定义新的工具函数
2. 在 `main.py` 或 `web_agent.py` 中注册工具
3. 工具函数应返回标准的JSON格式结果

### 自定义Agent行为
修改 `agent.py` 中的逻辑来自定义Agent的决策过程。

## 限制和改进方向

### 当前限制
- 简化的LLM模拟（硬编码逻辑）
- 基础的工具集
- 简单的任务规划

### 改进方向
- 集成真实的LLM API
- 扩展工具生态系统
- 增强任务规划能力
- 添加更多交互模式
- 支持插件系统

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

MIT License

