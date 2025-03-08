from twilio.rest import Client  # Corrected import

# Your existing code here...

def send_message():
    # Twilio account credentials
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)  # Corrected Client import

    message = client.messages.create(
        body="Hello from Aiza!",
        from_='+1234567890',  # Your Twilio number
        to='+0987654321'      # Destination number
    )

    print(message.sid)

if __name__ == "__main__":
    send_message()