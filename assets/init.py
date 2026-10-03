import os, platform
from win11toast import toast

def options():
    print("Testing")
    print("1. Send Message")
    print("2. Recieve Message")

    op = input("> ")
    if op == "1":
        msg = input(os.getlogin() + ": ")
        print("Message Sent: " + msg)
        options()
    elif op == "2":
        msg = input("otheruser: ")
        toast("@otheruser | KonsoleConnect", msg, audio={'silent': 'true'})
        options()

print("KonsoleConnect v0.0.1")
options()