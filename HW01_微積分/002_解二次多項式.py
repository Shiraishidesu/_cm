import cmath

def root2(a, b, c):
    """
    求解 ax^2 + bx + c = 0 的根，包含複數根。
    """
    if a == 0:
        raise ValueError("係數 a 不能為 0 (這不是二次方程式)")

    # 計算判別式開根號 (b^2 - 4ac)
    # cmath.sqrt 能夠處理負數，產生複數結果
    sqrt_delta = cmath.sqrt(b**2 - 4 * a * c)

    # 套用公式求解
    root1 = (-b + sqrt_delta) / (2 * a)
    root2 = (-b - sqrt_delta) / (2 * a)

    return root1, root2

# --- 主程式驗證區 ---

# 測試案例 1: 有實數根 (x^2 - 3x + 2 = 0, 根為 1, 2)
# 測試案例 2: 有複數根 (x^2 + 2x + 5 = 0, 根為 -1+2j, -1-2j)
test_cases = [
    (1, -3, 2), 
    (1, 2, 5)   
]

print(f"{'方程式':<20} | {'根 1':<25} | {'根 2':<25} | {'驗證結果'}")
print("-" * 85)

for a, b, c in test_cases:
    # 1. 呼叫函數求解
    r1, r2 = root2(a, b, c)
    
    # 2. 將根代回原方程式 f(x) 計算結果
    val1 = a * (r1**2) + b * r1 + c
    val2 = a * (r2**2) + b * r2 + c
    
    # 3. 驗證是否接近 0
    # 注意: 比較對象是 0 時，必須設定 abs_tol (絕對容許誤差)，
    # 因為 0 不能作為相對誤差的基準。
    check1 = cmath.isclose(val1, 0, abs_tol=1e-9)
    check2 = cmath.isclose(val2, 0, abs_tol=1e-9)
    
    # 顯示結果
    eq_str = f"{a}x^2 + {b}x + {c}"
    valid_str = "通過" if check1 and check2 else "失敗"
    
    # 格式化輸出複數，讓閱讀更容易
    print(f"{eq_str:<20} | {str(r1):<25} | {str(r2):<25} | {valid_str}")
    
    # 額外顯示代回後的殘差值 (Debug用)
    # print(f"   代回誤差: r1->{val1:.2e}, r2->{val2:.2e}")
    