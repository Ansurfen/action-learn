import time

# 获取当前时间戳（单位为秒）
timestamp = time.time()

# 将时间戳转换为本地时间的字符串形式
local_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

print(f"当前时间戳为：{int(timestamp)}")
print(f"当前时间为：{local_time_str}")