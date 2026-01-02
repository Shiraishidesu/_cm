import matplotlib.pyplot as plt
import random

def draw_sierpinski_variation(iterations=50000, divisor=3):
    vertices = [(0, 0), (1, 0), (0.5, 0.866)]
    colors_map = ['red', 'green', 'blue']
    px, py = 0.5, 0.5
    
    x_points, y_points, point_colors = [], [], []

    for i in range(iterations):
        vertex_idx = random.randint(0, 2)
        vx, vy = vertices[vertex_idx]

        # --- 關鍵修改 ---
        # 原本是: px = (px + vx) / 2  (這等於移動了 1/2 的距離)
        # 現在改為: 移動 1/divisor 的距離
        # 公式: 新點 = 舊點 + (向量差) / divisor
        px = px + (vx - px) / divisor
        py = py + (vy - py) / divisor
        
        if i > 20:
            x_points.append(px)
            y_points.append(py)
            point_colors.append(colors_map[vertex_idx])

    plt.figure(figsize=(10, 8), dpi=100)
    plt.scatter(x_points, y_points, c=point_colors, s=0.2)
    
    # 標題顯示目前的除數
    plt.title(f"Chaos Game with Division Factor = {divisor} (Move 1/{divisor})")
    plt.axis('on')
    plt.show()

# 執行：除以 3
if __name__ == "__main__":
    draw_sierpinski_variation(50000, divisor=3)