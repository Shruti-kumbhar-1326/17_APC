class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification")


# Create objects
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

# Runtime Polymorphism
for notification in notifications:
    notification.send()