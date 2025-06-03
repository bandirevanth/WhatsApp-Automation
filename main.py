from twillo.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+1234567890', #replace with your Twilio WhatsApp number & Ensure the number is in the format 'whatsapp:+1234567890'
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID:{message.sid}")
    except Exception as e:
        print(f"Failed to send message. An error occurred: {e}")


name = input("Enter the recipient's name: ")
recipient_number = input("Enter the recipient's WhatsApp number (with country code): ")
message_body = input(f"Enter the message to be sent to {name}: ")

date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM, 24-hour format): ")

# TIME LOGIC
schedule_datetime = datetime.strptime(f"{date_str} {time_str}" , "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_diff = schedule_datetime - current_datetime
delay_seconds = time_diff.total_seconds()

if delay_seconds <= 0:
    print("The scheduled time is in the past. Please enter a future date and time: ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

time.sleep(delay_seconds)
send_whatsapp_message(recipient_number, message_body)
