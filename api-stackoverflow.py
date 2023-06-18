import json
from pprint import pprint
import requests
from datetime import date, time, datetime, timedelta
# import pytz

# timezone = pytz.timezone("Africa/Abidjan")
to_date = int(datetime.now().timestamp())
from_date = int(datetime.combine(date.today() - timedelta(days=2), time.min).timestamp())

url = "https://api.stackexchange.com/2.3/questions"
params = {
    "fromdate": from_date,
    "todate	" : to_date,
    "order" : "desc",
    "sort" : "creation",
    "tagged" : "python",
    "site" : "stackoverflow"
}

response = requests.get(url, params=params)
# pprint(response.json())
questions_list = response.json()["items"]
print(f"Всего вопросов: {len(questions_list)}")
for question in questions_list:
    print(question["title"])