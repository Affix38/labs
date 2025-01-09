import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start_week = (datetime.now() - timedelta(6)).strftime('%Y%m%d')

reply = requests.get(f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_week}&end={today}&valcode=usd&json")
reply_json = json.loads(reply.text)

output_dict = {}
for item in reply_json:
    output_dict[item['exchangedate']] = item['rate']
print(output_dict)

fig, ax = plt.subplots()
plt.plot(output_dict.keys(), output_dict.values())
plt.show()