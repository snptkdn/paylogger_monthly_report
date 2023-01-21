import requests
import create_amount_per_category
import create_amount_per_day
from dotenv import load_dotenv 
import os

load_dotenv()

DISCORD_MONTHLY_WEBHOOKS_URL = os.getenv('DISCORD_MONTHLY_WEBHOOKS_URL')

def create_monthly_report():
    create_amount_per_day.create()
    create_amount_per_category.create()

    image_day = open('amount_per_day.png', 'rb')
    image_caregory = open('amount_per_category.png', 'rb')

    data = {'content': 'Here, Its Stats!'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, json=data)

    files = { 'param_name': ('amount_per_day.jpg', image_day, 'image/jpeg') }
    data = {'another_key': 'another_value'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, files=files, data=data)

    files = { 'param_name': ('amount_per_category.jpg', image_caregory, 'image/jpeg') }
    data = {'another_key': 'another_value'}
    r = requests.post(DISCORD_MONTHLY_WEBHOOKS_URL, files=files, data=data)
