import math
import cmath
import numpy as np  # 僅用於生成測試數據與比較，不參與傅立葉運算

# 1. 定義 DFT (正轉換)
def dft(x):
    """
    輸入: x (時域訊號，列表或陣列)
    輸出: X (頻域訊號，複數列表)
    """
    N = len(x)
    X = []
    
    # 對每一個頻率 k 進行計算
    for k in range(N):
        sum_val = 0
        for n in range(N):
            # 歐拉公式部分: e^(-j * 2pi * k * n / N)
            exponent = -1j * 2 * math.pi * k * n / N
            sum_val += x[n] * cmath.exp(exponent)
        X.append(sum_val)
        
    return X

# 2. 定義 IDFT (逆轉換)
def idft(X):
    """
    輸入: X (頻域訊號，複數列表)
    輸出: x (時域訊號，複數列表)
    """
    N = len(X)
    x = []
    
    # 對每一個時間點 n 進行計算
    for n in range(N):
        sum_val = 0
        for k in range(N):
            # 逆轉換指數為正: e^(j * 2pi * k * n / N)
            exponent = 1j * 2 * math.pi * k * n / N
            sum_val += X[k] * cmath.exp(exponent)
        # 記得除以 N
        x.append(sum_val / N)
        
    return x

# 3. 驗證函數
def verify_transform():
    print("=== 傅立葉轉換驗證 ===")
    
    # 建立一個簡單的測試訊號 (例如：由兩個弦波組成的訊號)
    N = 8  # 樣本數
    t = np.arange(N)
    # 訊號 f: 頻率為 1 的波 + 頻率為 3 的波
    f = np.sin(2 * np.pi * 1 * t / N) + 0.5 * np.cos(2 * np.pi * 3 * t / N)
    
    print(f"1. 原始訊號 f (前4個數值):\n   {f[:4]}...")
    
    # 執行 DFT
    F = dft(f)
    print(f"\n2. 正轉換後的頻譜 F (前4個數值):\n   {[round(val.real, 2) + round(val.imag, 2)*1j for val in F[:4]]}...")
    
    # 執行 IDFT
    f_restored = idft(F)
    
    # 由於浮點數運算誤差，轉換回來通常會有極小的虛部 (如 1e-16j)，我們取實部比較
    f_restored_real = [val.real for val in f_restored]
    
    print(f"\n3. 逆轉換回來的訊號 f_restored (前4個數值):\n   {np.array(f_restored_real)[:4]}...")
    
    # 驗證是否相等 (使用 numpy 的 allclose 來容許微小的浮點誤差)
    is_same = np.allclose(f, f_restored_real)
    
    print("\n=== 驗證結果 ===")
    if is_same:
        print("✅ 成功！逆轉換回來的訊號與原始訊號一致。")
    else:
        print("❌ 失敗，數值不一致。")

# 執行驗證
if __name__ == "__main__":
    verify_transform()