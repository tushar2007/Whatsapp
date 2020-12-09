from twilio.rest import Client
import os
import time
import schedule



def send_msg():
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    client.messages.create(
        from_='whatsapp:+14155238886',
        body='Good Morning Tushar',
        to='whatsapp:+919959686272'
    )
schedule.every().day.at("07:30").do(send_msg)
while True:
    schedule.run_pending()
    print("sent!")
    

