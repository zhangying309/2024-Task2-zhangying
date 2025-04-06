import numpy as np
import matplotlib.pyplot as plt

# 你的学号
student_id = 120243505078

# 将学号的某个部分作为相位偏移量
phase_shift = student_id % 360  # 确保相位在 0 到 360 之间

# 生成数据
x = np.linspace(0, 10, 100)
y = np.sin(x + np.radians(phase_shift))  # 根据相位偏移调整正弦波

# 创建图形
plt.plot(x, y)

# 添加标题和标签
plt.title(f'正弦波折线图 - 相位偏移: {phase_shift}°')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')

# 保存图像到 images 文件夹
plt.savefig('images/sine_wave_plot.png')

# 显示图形
plt.show()
