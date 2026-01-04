import cmath

def root3(a, b, c, d):
    """
    求解三次多項式 ax^3 + bx^2 + cx + d = 0 的根
    包含實數根與複數根
    """
    # 檢查是否為三次方程式
    if a == 0:
        return "係數 a 不能為 0"

    # --- 第一步：簡化方程式 ---
    # 目標是將 x = t - b/(3a) 代入，消除二次項，
    # 得到形式為 t^3 + pt + q = 0 的方程式
    
    p = (3*a*c - b**2) / (3 * a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27 * a**3)

    # --- 第二步：計算判別式與中間變數 ---
    # Delta = (q/2)^2 + (p/3)^3
    delta = (q/2)**2 + (p/3)**3
    
    # 計算平方根 (使用 cmath 處理複數情況)
    sqrt_delta = cmath.sqrt(delta)
    
    # 計算 U (卡爾丹公式中的一個變數)
    # U = (-q/2 + sqrt_delta)^(1/3)
    # 注意：Python 的複數 **(1/3) 會傳回主值(Principal value)
    U_term = -q/2 + sqrt_delta
    U = U_term ** (1/3)

    # 計算 V
    # 根據韋達定理與卡爾丹公式，必須滿足 U * V = -p/3
    # 我們不直接計算 V = (-q/2 - sqrt_delta)^(1/3)，
    # 因為那樣可能會選錯複數的「分支」，導致配對錯誤。
    # 用 V = -p / (3U) 來計算會更穩健。
    
    if U == 0:
        V = 0
    else:
        V = -p / (3 * U)

    # --- 第三步：求解 t 的三個根 ---
    # 三個根分別為:
    # t1 = U + V
    # t2 = w*U + w^2*V
    # t3 = w^2*U + w*V
    # 其中 w 是三次單位根 (-1 + sqrt(3)i) / 2
    
    w = complex(-0.5, (3**0.5)/2)
    w2 = w * w

    t1 = U + V
    t2 = U * w + V * w2
    t3 = U * w2 + V * w

    # --- 第四步：還原回 x ---
    # x = t - b/(3a)
    offset = b / (3 * a)
    
    x1 = t1 - offset
    x2 = t2 - offset
    x3 = t3 - offset

    return x1, x2, x3

# --- 測試範例 ---
if __name__ == "__main__":
    # 範例 1: x^3 - 6x^2 + 11x - 6 = 0 (根應該是 1, 2, 3)
    print("範例 1 (根為 1, 2, 3):")
    roots = root3(1, -6, 11, -6)
    for r in roots:
        print(f"{r:.2f}") # 格式化輸出，保留兩位小數

    print("-" * 20)

    # 範例 2: x^3 - 1 = 0 (根為 1 和兩個複數根)
    print("範例 2 (x^3 - 1 = 0):")
    roots = root3(1, 0, 0, -1)
    for r in roots:
        print(f"{r:.2f}")