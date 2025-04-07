# 2024-Task2-zhangying
# 任务二：功能开发与分支管理实践

本项目通过 Git 分支管理与 Python 可视化功能开发的结合，完成了从分支创建到合并、代码实现到环境配置的一系列操作，旨在掌握协作开发与项目规范管理的核心流程。

---

##  项目结构说明
2024-Task2-你的名字/
├── src/
│ └── plot.py
├── images/
│ └── 全部截图.png
├── docs/
│ └── summary.md
├── environment.yml
├── README.md
└── .gitignore

---

## 🧪 功能说明

使用 Python 生成并保存正弦波图像，展示基本的 `matplotlib` 使用方法及功能模块的封装，具体代码请见 `src/plot.py`。

---

## 🛠️ 分支管理流程（Git）

本项目主要使用以下分支：

- `main`：主分支，存放最终稳定版本。
- `dev`：开发分支，用于日常开发。
- `feature-plot`：功能分支，实现绘图功能。

### 🧾 操作命令：

```bash
git init                          # 初始化 Git 仓库
git branch dev                   # 创建开发分支
git checkout -b feature-plot     # 创建功能分支并切换
git add .                        # 添加变更
git commit -m "提交信息"         # 提交修改
git checkout dev
git merge feature-plot           # 合并功能分支到 dev
git checkout main
git merge dev                    # 合并开发分支到主分支
git push origin main             # 推送到远程主分支

