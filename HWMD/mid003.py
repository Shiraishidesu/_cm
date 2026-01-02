import matplotlib.pyplot as plt
import random

def draw_stardust_fractal(iterations=50000):
    # 1. 定義三角形頂點 (維持一樣)
    vertices = [
        (0, 0),      # A: 紅
        (1, 0),      # B: 綠
        (0.5, 0.866) # C: 藍
    ]
    colors_map = ['red', 'green', 'blue']

    # 2. 初始化
    px, py = 0.5, 0.5
    x_points = []
    y_points = []
    point_colors = []

    print(f"正在生成星塵碎形，共 {iterations} 個點...")

    # 3. 渾沌遊戲迴圈
    for i in range(iterations):
        vertex_idx = random.randint(0, 2)
        vx, vy = vertices[vertex_idx]

        # --- 關鍵修改 ---
        # 為了讓圖形炸開，我們要移動得離頂點「更近」
        # 移動距離 = 總距離的 2/3 (約 0.666)
        # 這樣每個新的子圖形只會保留原本的 1/3 大小，彼此就會分開
        
        ratio = 2/3  # 移動比例
        
        # 公式：新點 = 舊點 + (向量差 * 比例)
        px = px + (vx - px) * ratio
        py = py + (vy - py) * ratio

        # 另一種等價寫法 (權重寫法):
        # px = (px + 2 * vx) / 3
        # py = (py + 2 * vy) / 3

        if i > 20:
            x_points.append(px)
            y_points.append(py)
            point_colors.append(colors_map[vertex_idx])

    # 4. 繪圖
    plt.figure(figsize=(10, 8), dpi=100)
    
    # s=0.1 讓點更細，星塵效果更細緻
    plt.scatter(x_points, y_points, c=point_colors, s=0.1)
    
    plt.title("Stardust Fractal (Moving 2/3 distance)")
    plt.axis('equal') # 保持比例，避免變形
    plt.axis('on')   # 關閉座標軸看起來更有藝術感
    plt.show()

if __name__ == "__main__":
    draw_stardust_fractal(60000)