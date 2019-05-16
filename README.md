# udp-comm

Simple UDP server and client for communication

## Requirements

- Python 3.6 (maybe incompatible with Python 2)

## Usage

On where you want to receive messages, run

```zsh
python3 server.py
```

On where you want to send messages, run

```zsh
# Suppose server address is 1.2.3.4
python3 client.py --host 1.2.3.4
```

Default listening port is 7777, you can change it to whatever you like. Do not forget to change it in both server and client.

Make sure server is running before sending messages from client, or nothing will happen.

Specify the arguments to make client send specific message to server. For example,

```zsh
python3 client.py --action ccproxy
```

## Support Actions

- tinyproxy
- ccproxy
- proxy(also specify --extra_args `port`)

Maybe add other action in the future.

## Notice

- Server part need `server.py` and `executor.py`
- Client part need `client.py` and `actions.py`
