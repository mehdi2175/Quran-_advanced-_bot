# ارسال آیه روزانه
from apscheduler.schedulers.background import BackgroundScheduler

def send_daily_ayah():
    print("ارسال آیه روزانه به کاربران")

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_ayah, 'interval', hours=24)
scheduler.start()