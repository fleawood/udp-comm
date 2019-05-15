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
python3 client.py
```

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

If you want to run `server.py`, you also need `executor.py`, and if you want to run `client.py`, you also need `actions.py`.
