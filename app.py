import schedule
import time
import requests
from datetime import datetime
import pytz

def job():
    url = "https://www.example.com"  # 这里替换为您需要访问的URL
    response = requests.get(url)
    print(response.status_code)  # 打印访问结果

beijing_tz = pytz.timezone("Asia/Shanghai")  # 设置时区为北京时间

# 计算当前时间在指定时区下的下一个执行时间
def get_next_execution_time(hour, minute, tz):
    now = datetime.now(tz)
    target_time = datetime(now.year, now.month, now.day, hour, minute, tzinfo=tz)
    if now > target_time:
        target_time += timedelta(days=1)
    return target_time

next_execution_time = get_next_execution_time(15, 20, beijing_tz)
schedule.every().day.at(next_execution_time.strftime("%H:%M")).do(job)

# 定时任务主循环
while True:
    schedule.run_pending()
    time.sleep(1)
