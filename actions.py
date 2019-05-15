class Action(object):
    def to_data(self, *args, **kwargs):
        raise NotImplementedError


class Proxy(Action):
    def __init__(self, port):
        self.port = port

    def to_data(self, port):
        return ["proxy", {"port": port}]


TinyProxy = Proxy(port=8888)
CCProxy = Proxy(port=808)


def get_action(type, args):
    return {
        "tinyproxy": TinyProxy,
        "ccproxy": CCProxy,
        "proxy": Proxy(port=int(args[0])),
    }[type]
