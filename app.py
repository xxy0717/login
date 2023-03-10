import schedule
import time
import requests
from pytz import timezone

def job():
    url = "https://www.example.com"  # 这里替换为您需要访问的URL
    response = requests.get(url)
    print(response.status_code)  # 打印访问结果

beijing_tz = timezone("Asia/Shanghai")  # 设置时区为北京时间
schedule.every().day.at("15:20").do(job).tzinfo(beijing_tz)  # 在北京时间15:20执行任务

# 定时任务主循环
while True:
    schedule.run_pending()
    time.sleep(1)
