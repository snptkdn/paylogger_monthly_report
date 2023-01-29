import requests
import datetime
import calendar
import math
import datetime as dt

def append_fields(fields, name, value, inline=False):
    fields.append(
        {
            "name":name,
            "value":value,
            "inline":inline
        }
    )

def append_categories(per_category, fields):
    per_category = dict(
        sorted(
            per_category.items(),
            key = lambda category : category[1],
            reverse=True
        )
    )

    [
        append_fields(fields, key, value, inline=True)
        for key, value in per_category.items()
    ] 
    

def get_daily_data():
    today  = dt.datetime.today()
    per_day = requests.get(
        'http://34.127.13.199:8000/log/per_day?year={}&month={}'
        .format(
            today.year,
            today.month
        )
    ).json()
    per_category = requests.get(
        'http://34.127.13.199:8000/log/per_category?year={}&month={}'
        .format(
            today.year,
            today.month
        )
    ).json()
    total_str = requests.get(
        'http://34.127.13.199:8000/log/total?year={}&month={}'
        .format(
            today.year,
            today.month
        )
    ).json()

    total = int(total_str)
    today_str = today.strftime('%Y-%m-%d')
    today_amount_str = per_day[today_str]
    today_amount = int(today_amount_str)
    end_of_month = calendar.monthrange(today.year, today.month)[1]
    amount_end = math.floor(total * (end_of_month / today.day))

    fields = []
    append_fields(fields, "今日の使用量",     "{}円".format(today_amount))
    append_fields(fields, "今月の合計量",     "{}円".format(total))
    append_fields(fields, "月末の予測使用量", "{}円".format(amount_end))
    append_categories(per_category, fields)

    return {
        'content': '日次レポートをお届けします。',
        "embeds": [
            {
                "fields": fields
            }
        ]
    }
