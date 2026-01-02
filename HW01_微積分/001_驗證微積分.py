import math

# 1. 定義數值積分 (計算 0 到 x 的面積)
# 使用梯形法 (Trapezoidal Rule) 來近似積分
def integral(f, a, b, n=1000):
    if a == b: return 0
    h = (b - a) / n  # 切分成 n 個小寬度
    total = 0.5 * (f(a) + f(b)) # 頭尾
    for i in range(1, n):
        total += f(a + i * h) # 中間的點
    return total * h

# 2. 定義數值微分 (計算在 x 點的斜率)
# 使用中心差分法 (Central Difference) 來獲得比前後差分更高的精確度
def df(g, x, h=1e-5):
    # g 是函數 (在這裡 g 會是積分函數 F(x))
    # 斜率 ≈ (y2 - y1) / (x2 - x1)
    return (g(x + h) - g(x - h)) / (2 * h)

# 3. 測試函數 (例如 f(t) = t^2)
def my_function(t):
    return t**2

# 4. 驗證定理
def verify_theorem(f, x):
    # 定義累積函數 F(x) = ∫(0 to x) f(t) dt
    # 注意：這裡用 lambda 創造一個動態函數，輸入是 t (這裡的 x)，輸出是積分值
    F = lambda t: integral(f, 0, t)
    
    # 計算等式左邊 (LHS)：對積分結果 F 進行微分
    lhs = df(F, x)
    
    # 計算等式右邊 (RHS)：原本的函數 f(x)
    rhs = f(x)
    
    print(f"在 x={x} 時:")
    print(f"  左式 (d/dx ∫f(t)dt) ≈ {lhs:.6f}")
    print(f"  右式 (f(x))        = {rhs:.6f}")
    
    # 驗證：判斷兩者是否足夠接近 (容許誤差 1e-3)
    # 浮點數運算會有微小誤差，不能直接用 ==
    assert math.isclose(lhs, rhs, rel_tol=1e-3), "驗證失敗！誤差過大"
    print("  ✅ 驗證成功！定理成立。\n")

# --- 執行測試 ---
print("--- 測試函數 f(t) = t^2 ---")
verify_theorem(my_function, x=2.0)  # 預期接近 4
verify_theorem(my_function, x=5.0)  # 預期接近 25

print("--- 測試函數 f(t) = sin(t) ---")
verify_theorem(math.sin, x=1.0)     # 預期接近 sin(1)