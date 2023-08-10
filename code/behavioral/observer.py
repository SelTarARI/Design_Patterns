class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


# Example usage
class EmailNotification(Observer):
    def update(self, message):
        print("Sending email notification:", message)


class SMSNotification(Observer):
    def update(self, message):
        print("Sending SMS notification:", message)


subject = Subject()
email_observer = EmailNotification()
sms_observer = SMSNotification()

subject.attach(email_observer)
subject.attach(sms_observer)

subject.notify("Hello, subscribers!")

subject.detach(email_observer)

subject.notify("Important announcement!")
