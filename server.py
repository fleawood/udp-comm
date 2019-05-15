import socket
import json
import executor
from time import ctime

import argparse
import os


class Server(object):
    BUF_SIZE = 1024
    ok_message = json.dumps("OK").encode(encoding="UTF-8")

    def __init__(self, host, port, opts=None):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((host, port))
        self.executor = executor.Executor(opts)

    def process(self):
        data, addr = self.s.recvfrom(self.BUF_SIZE)
        host, port = socket.getnameinfo(addr, socket.NI_NUMERICHOST)

        data = json.loads(data)

        self.executor.process_data(data, host)

        self.log(host, port)
        self.s.sendto(Server.ok_message, addr)

    def log(self, host, port):
        print("[{0}] From {1}:{2}".format(ctime(), host, port))

    def close(self):
        self.s.close()


def main(args):
    host = ""
    port = args.port
    proxy_script = args.proxy_script
    sh = args.sh

    server = Server(host, port, opts=dict(
        proxy_script=proxy_script,
        sh=sh,
    ))

    while True:
        try:
            server.process()
        except KeyboardInterrupt:
            server.close()
            print("See you next time.")
            exit(0)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        default=7777
    )
    parser.add_argument(
        "--proxy_script",
        type=str,
        default=os.path.expanduser("~/script/proxy.sh")
    )
    parser.add_argument(
        "--sh",
        type=str,
        default="zsh"
    )
    args = parser.parse_args()
    main(args)
