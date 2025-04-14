# 初始化中断次数计数器
breakpoint_hit_count = 0

def test_function():
    global breakpoint_hit_count
    # 假设在此处设置断点
    breakpoint_hit_count += 1
    result = 1 + 2
    return result
# define test
if __name__ == "__main__":
    for _ in range(5):
        test_function()
    print(f"断点命中次数: {breakpoint_hit_count}")