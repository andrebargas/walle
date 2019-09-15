import base64


def preprocessmessage(message):
    print(message)
    n_message = base64.b64decode(message).decode("utf-8")
    n_message = n_message.encode().hex()
    print(n_message)
    return n_message[1:]