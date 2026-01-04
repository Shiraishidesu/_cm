import math
from decimal import Decimal, getcontext
# 計算一公平銅板，連續投擲 10000 次，全部得到正面的機率。
def calculate_coin_probability(n_flips):
    # 1. 設定精度
    # 0.5^10000 大約是 10^-3010，所以我們需要設定足夠的位數
    # 我們設定 3100 位數以確保精確度
    getcontext().prec = 3100
    
    # 2. 定義基本機率 (使用字串初始化 Decimal 以避免浮點數誤差)
    p = Decimal('0.5')
    
    # 3. 計算 p 的 n 次方
    result = p ** n_flips
    
    return result

def calculate_log_probability(n_flips):
    # 使用對數計算數量級 (Log-space)
    # log10(0.5^10000) = 10000 * log10(0.5)
    log_val = n_flips * math.log10(0.5)
    return log_val

# --- 主程式 ---
n = 10000

# 方法一：一般浮點數計算 (會失敗)
try:
    naive_result = 0.5 ** n
    print(f"一般計算 (float): {naive_result} (這是下溢造成的錯誤結果)")
except Exception as e:
    print(e)

print("-" * 30)

# 方法二：對數估算 (快速得知數量級)
log_result = calculate_log_probability(n)
print(f"對數估算: 10 的 {log_result:.2f} 次方")
print(f"這表示小數點後大約有 {abs(int(log_result))} 個零")

print("-" * 30)

# 方法三：高精度計算 (準確結果)
precise_result = calculate_coin_probability(n)

# 格式化輸出科學記號
# format 字串中的 'e' 代表科學記號
print(f"高精度計算結果 (科學記號):")
print(f"{precise_result:.5e}")