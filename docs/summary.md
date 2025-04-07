# 总结与反思

## 一、所使用的 Git、Conda 命令及解释

### Git 命令

- `git init`：初始化 Git 仓库。
- `git branch dev`：创建名为 dev 的新分支。
- `git checkout dev`：切换到 dev 分支。
- `git checkout -b feature-plot`：新建并切换到 feature-plot 分支。
- `git add .`：将所有修改添加到暂存区。
- `git commit -m "说明"`：提交更改并写入说明。
- `git merge 分支名`：将指定分支合并到当前分支。
- `git push origin 分支名`：将分支推送到远程仓库。

### Conda 命令

- `conda create -n plot-env python=3.9`：创建名为 plot-env 的新环境。
- `conda activate plot-env`：激活环境。
- `conda install matplotlib`：安装绘图库 matplotlib。

---

## 二、Anaconda 环境配置的优点与难点

**优点：**
- 多环境管理灵活，便于不同项目之间隔离依赖。
- 包管理方便，支持 pip 和 conda 安装。

**难点：**
- 安装包时可能出现依赖冲突或镜像下载慢。
- 有时需要配置环境变量或清理缓存来解决安装问题。

---

## 三、Git 分支管理中的经验

- 建立 dev 分支作为开发主线，功能分支 feature-plot 单独开发，结构清晰。
- 合并前先测试无误，避免带入 bug。
- 每次提交都写清楚说明，方便回溯。
- 使用 `git status`、`git log` 等命令辅助检查。

---

## 四、部署过程中遇到的问题及解决方案

| 问题 | 解决方案 |
|------|----------|
| `matplotlib` 未安装导致运行失败 | 使用 `conda install matplotlib` 成功安装 |
| GitHub 推送失败 | 添加 SSH key 到 GitHub，重新验证成功 |
| 图像路径错误导致未保存成功 | 检查并确保 `images/` 文件夹存在，路径正确 |

---

## 五、项目说明和部署步骤（已写入 README.md）

详见 [README.md](../README.md)，包含项目结构说明、环境配置、运行方式和分支管理流程。

---

## 六、推送记录

所有更改已按如下顺序推送至 GitHub：

```bash
git add .
git commit -m "完成总结与 README 文档"
git push origin dev
