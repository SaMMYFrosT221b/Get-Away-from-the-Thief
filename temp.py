import threading


def printit():
    threading.Timer(0.5, printit).start()
    print("Hello world")


printit()
