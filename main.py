import os
import time
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp_number = f"whatsapp:{os.getenv('TWILIO_WHATSAPP_NUMBER')}"

# Validate credentials
if not all([account_sid, auth_token, from_whatsapp_number]):
    print("Twilio credentials are missing in the .env file.")
    exit(1)

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_=from_whatsapp_number,
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"\n✅ Message sent successfully!\nSID: {message.sid}")
    except Exception as e:
        print(f"\n❌ Failed to send message. Error: {e}")

def main():
    name = input("Recipient's name: ")
    recipient_number = input("WhatsApp number with country code (e.g., +91XXXXXXXXXX): ")
    message_body = input(f"Enter the message for {name}: ")

    date_str = input("Date to send message (YYYY-MM-DD): ")
    time_str = input("Time to send (HH:MM, 24-hour format): ")

    try:
        schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        delay_seconds = (schedule_datetime - now).total_seconds()

        if delay_seconds <= 0:
            print("The scheduled time is in the past. Please choose a future time.")
            return

        print(f"\n🕒 Message scheduled to be sent to {name} at {schedule_datetime.strftime('%Y-%m-%d %H:%M:%S')}.\n")
        time.sleep(delay_seconds)

        send_whatsapp_message(recipient_number, message_body)

    except ValueError:
        print("Invalid date/time format. Please use YYYY-MM-DD and HH:MM (24-hour).")

if __name__ == "__main__":
    main()
