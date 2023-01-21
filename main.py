import requests
import create_amount_per_category
import create_amount_per_day
from dotenv import load_dotenv 
import datetime
import calendar
import os

def is_end_of_month(date: datetime.date) -> bool:
    end_of_month = calendar.monthrange(date.year, date.month)[1]
    return end_of_month == date.day

def create_monthly_report():
    create_amount_per_day.create()
    create_amount_per_category.create()

    image_day = open('amount_per_day.png', 'rb')
    image_caregory = open('amount_per_category.png', 'rb')

    data = {'content': '月次レポートをお届けします。'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, json=data)

    files = { 'param_name': ('amount_per_day.jpg', image_day, 'image/jpeg') }
    data = {'another_key': 'another_value'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, files=files, data=data)

    files = { 'param_name': ('amount_per_category.jpg', image_caregory, 'image/jpeg') }
    data = {'another_key': 'another_value'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, files=files, data=data)

load_dotenv()

DISCORD_MONTHLY_WEBHOOKS_URL = os.getenv('DISCORD_MONTHLY_WEBHOOKS_URL')
DISCORD_DAILY_WEBHOOKS_URL = os.getenv('DISCORD_DAILY_WEBHOOKS_URL')

if is_end_of_month(datetime.date.today()):
    create_monthly_report()
else:
    data = {'content': '日次レポートをお届けします。'}
    r = requests.post(DISCORD_DAILY_WEBHOOKS_URL, json=data)
    
