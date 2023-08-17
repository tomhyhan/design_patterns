from abc import ABC, abstractmethod

# Abstract Product
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete Products
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")

# Abstract Creator
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

# Concrete Creators
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

def main():
    email_factory = EmailNotificationFactory()
    sms_factory = SMSNotificationFactory()

    email_notification = email_factory.create_notification()
    sms_notification = sms_factory.create_notification()

    email_notification.send("Hello via email!")
    sms_notification.send("Hello via SMS!")

if __name__ == "__main__":
    main()
