import requests
import schedule
import time

def main():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '8061103235',
    'message': 'Hello world',
    'key': 'textbelt',
})
    print(resp.json())

schedule.every().day.at("10:30").do(main)

schedule.every(10).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)