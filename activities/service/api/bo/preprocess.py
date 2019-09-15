
def preprocessmessage(message):
    print(message)
    n_message = message.encode().hex()
    print(n_message)
    return n_message[1:]