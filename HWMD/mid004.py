import matplotlib.pyplot as plt
import random

def draw_barnsley_fern(iterations=100000):
    # 初始座標
    x, y = 0, 0
    
    x_points = []
    y_points = []
    colors = []

    print(f"正在生長巴恩斯利蕨，共 {iterations} 個細胞...")

    for i in range(iterations):
        # 生成一個 0 到 100 的隨機數，用來決定要走哪一條規則
        # 這是「加權隨機」，因為大自然的生長不是均等的
        r = random.uniform(0, 100)

        # 暫存舊的 x, y (因為計算新 y 時需要用到舊 x)
        x_old, y_old = x, y

        # --- 規則 1: 莖 (Stem) ---
        # 機率 1%
        # 數學：把點壓扁到 y 軸上，並不往上長
        if r < 1:
            x = 0
            y = 0.16 * y_old
            color = 'yellow' # 根部

        # --- 規則 2: 主葉生長 (Successive Leaflets) ---
        # 機率 85%
        # 數學：稍微縮小，並向上推，讓蕨類長高
        elif r < 86:
            x = 0.85 * x_old + 0.04 * y_old
            y = -0.04 * x_old + 0.85 * y_old + 1.6
            color = 'green'  # 主體

        # --- 規則 3: 左側葉片 (Left Leaflet) ---
        # 機率 7%
        # 數學：縮小並向左旋轉
        elif r < 93:
            x = 0.20 * x_old - 0.26 * y_old
            y = 0.23 * x_old + 0.22 * y_old + 1.6
            color = 'red'    # 左葉

        # --- 規則 4: 右側葉片 (Right Leaflet) ---
        # 機率 7% (剩餘的機率)
        # 數學：縮小並向右旋轉
        else:
            x = -0.15 * x_old + 0.28 * y_old
            y = 0.26 * x_old + 0.24 * y_old + 0.44
            color = 'blue'   # 右葉

        # 存入座標 (前幾個點通常會亂跳，可以選擇忽略，這裡全部畫出來也無妨)
        x_points.append(x)
        y_points.append(y)
        colors.append(color)

    # 繪圖
    plt.figure(figsize=(8, 10), dpi=100)
    # 背景設為黑色，對比度更高
    plt.style.use('dark_background') 
    
    plt.scatter(x_points, y_points, c=colors, s=0.2, alpha=0.6)
    
    plt.title("Barnsley Fern (IFS with Color Mapping)")
    plt.axis('on')
    plt.show()

if __name__ == "__main__":
    draw_barnsley_fern(100000)