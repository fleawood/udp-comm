import socket
import argparse
import json
import actions


def main(args):
    host = args.host
    port = args.port
    addr = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    BUF_SIZE = 1024

    action = actions.get_action(args.action, args.extra_args)
    data = json.dumps(action.to_data()).encode(encoding="UTF-8")

    s.settimeout(5)
    r_data = None
    try:
        s.sendto(data, addr)
        r_data = json.loads(s.recv(BUF_SIZE))
    except socket.timeout:
        print("Socket timeout")
    finally:
        s.close()

    if r_data == "OK":
        print("Succeed")
    else:
        print("Fail")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        default=""
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7777
    )
    parser.add_argument(
        "--action",
        type=str,
        choices=("tinyproxy", "ccproxy", "proxy"),
        default="tinyproxy"
    )
    parser.add_argument(
        "--extra_args",
        type=str,
        nargs='*',
        default=None
    )
    args = parser.parse_args()
    main(args)
