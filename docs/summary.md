# 总结与反思

## 所使用的 Git、Conda 命令与解释：

- `git init`：初始化本地 Git 仓库
- `git branch dev`：创建开发分支 dev
- `git checkout -b feature-plot`：创建功能分支并切换
- `git add` + `git commit`：提交代码变更
- `git merge`：合并功能分支到 dev
- `git push`：推送本地分支到远程
- `conda create -n task2-env python=3.10`：创建虚拟环境
- `conda activate task2-env`：激活环境
- `pip install matplotlib numpy`：安装依赖

## Anaconda 环境配置优点与难点：

优点：
- 易于管理不同项目的依赖环境
- 便于分享和重现项目

难点：
- 初次配置较复杂，需注意 Python 版本兼容性

## Git 分支管理经验：

- 使用 dev 和 feature 分支让开发更有条理
- 合并前先切回主分支可以避免冲突
- 每次提交添加清晰注释是个好习惯

## 遇到的问题及解决方式：

- 文件路径不对导致图片无法保存 ➝ 检查路径，统一在 `images/` 下输出
- 忘记切换分支就修改代码 ➝ 使用 `git status` 提前检查当前分支

---

_文档总结了整个任务的开发流程、环境设置、使用工具和遇到的问题。_
