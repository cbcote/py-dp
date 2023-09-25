class MessageHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_message(self, message):
        pass

class EmailHandler(MessageHandler):
    def handle_message(self, message):
        if message.startswith("Email:"):
            print("EmailHandler: Handling email message.")
        elif self.next_handler is not None:
            print("EmailHandler: Message is not an email. Passing to the next handler.")
            self.next_handler.handle_message(message)
        else:
            print("EmailHandler: Message is not an email and no further handlers available.")

class SMSHandler(MessageHandler):
    def handle_message(self, message):
        if message.startswith("SMS:"):
            print("SMSHandler: Handling SMS message.")
        elif self.next_handler is not None:
            print("SMSHandler: Message is not an SMS. Passing to the next handler.")
            self.next_handler.handle_message(message)
        else:
            print("SMSHandler: Message is not an SMS and no further handlers available.")

class TwitterHandler(MessageHandler):
    def handle_message(self, message):
        if message.startswith("Twitter:"):
            print("TwitterHandler: Handling Twitter message.")
        elif self.next_handler is not None:
            print("TwitterHandler: Message is not a Twitter message. Passing to the next handler.")
            self.next_handler.handle_message(message)
        else:
            print("TwitterHandler: Message is not a Twitter message and no further handlers available.")

# Create a chain of message handlers
email_handler = EmailHandler()
sms_handler = SMSHandler()
twitter_handler = TwitterHandler()

email_handler.set_next_handler(sms_handler)
sms_handler.set_next_handler(twitter_handler)

# Handle messages
messages = [
    "Email: Hello, this is an email.",
    "SMS: This is an SMS message.",
    "Twitter: Tweeting something cool!",
    "WhatsApp: This is not a supported message type."
]

for message in messages:
    print("Handling message:")
    email_handler.handle_message(message)
    print("---")
