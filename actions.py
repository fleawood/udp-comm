class Action(object):
    def to_data(self, *args, **kwargs):
        raise NotImplementedError


class Proxy(Action):
    def __init__(self, port):
        self.port = port

    def to_data(self):
        return ["proxy", {"port": self.port}]


TinyProxy = Proxy(port=8888)
CCProxy = Proxy(port=808)


def get_action(type, args):
    if type == "tinyproxy":
        return TinyProxy
    elif type == "ccproxy":
        return CCProxy
    elif type == "proxy":
        return Proxy(port=int(args[0]))

