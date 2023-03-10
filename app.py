import schedule
import time
import requests

def job():
    url = "https://www.imddoctors.com/science/ekx/szjsqf/1280"  # 这里替换为您需要访问的URL
    response = requests.get(url)
    print(response.status_code)  # 打印访问结果

# 每天的8:00执行一次任务
schedule.every().day.at("15:08").do(job)

# 定时任务主循环
while True:
    schedule.run_pending()
    time.sleep(1)
