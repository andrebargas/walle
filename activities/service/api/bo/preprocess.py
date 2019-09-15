
def preprocessmessage(message):
    n_message = message.encode().hex().split("0")
    return n_message[1:]