import matplotlib.pyplot as plt
import random

def draw_colored_sierpinski(iterations=50000):
    # 1. 定義三角形的三個頂點 (A, B, C)
    # A: 左下 (紅), B: 右下 (綠), C: 頂部 (藍)
    vertices = [
        (0, 0),      # Index 0: Vertex A
        (1, 0),      # Index 1: Vertex B
        (0.5, 0.866) # Index 2: Vertex C (0.866 約為 sqrt(3)/2)
    ]
    
    # 定義對應的顏色 (RGB)
    # 這裡使用字串或 hex 碼皆可，為了清楚分別用 Red, Green, Blue
    colors_map = ['red', 'green', 'blue']

    # 2. 初始化起點
    # 隨機選一個點作為起始點 (這裡直接從中心開始，之後會迅速收斂)
    px, py = 0.5, 0.5

    # 用來儲存所有點的座標與顏色
    x_points = []
    y_points = []
    point_colors = []

    print(f"開始計算 {iterations} 個點...")

    # 3. 渾沌遊戲 (Chaos Game) 迴圈
    for i in range(iterations):
        # 步驟 A: 隨機選擇一個頂點 (0, 1, 或 2)
        vertex_idx = random.randint(0, 2)
        vx, vy = vertices[vertex_idx]

        # 步驟 B: 移動到當前點與被選頂點的「中點」
        px = (px + vx) / 2
        py = (py + vy) / 2

        # 為了視覺效果，前 20 點通常不畫 (這是暖身期，讓點落入碎形軌道)
        if i > 20:
            x_points.append(px)
            y_points.append(py)
            # 步驟 C: 根據「被選中的頂點」決定顏色
            point_colors.append(colors_map[vertex_idx])

    # 4. 繪圖
    plt.figure(figsize=(10, 8), dpi=100)
    
    # 繪製散佈圖 (s=0.2 讓點非常細小，視覺效果更佳)
    plt.scatter(x_points, y_points, c=point_colors, s=0.2)
    
    plt.title("Sierpinski Triangle with Chaos Game & Color Mapping")
    plt.axis('on') # 座標軸開關
    plt.show()

# 執行函式
if __name__ == "__main__":
    draw_colored_sierpinski(50000)