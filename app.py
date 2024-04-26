from credentials import mobile_number
import requests
import schedule
import time
def send_message():
    resp  = requests.post('https://textbelt.com/text',{
        'phone' : mobile_number,
        'message' : 'Good Moring Ahmed, python a day keep the doctor away',
        'key' : 'textbelt'
    })
    print(resp.json())

schedule.every().day.at('08:00').do(send_message)



while True: 
    schedule.run_pending()
    time.sleep(1)