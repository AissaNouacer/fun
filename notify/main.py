import notify2
import time


def notify_me():
    notify2.init("hello from notify me")
    notty = notify2.Notification("Welcome Lahsen M")
    notty.set_urgency(notify2.URGENCY_NORMAL)
    # timeout for the notification
    notty.set_timeout(3000)
    notty.show()
    time.sleep(5)



if __name__ == "__main__":
    notify_me()
