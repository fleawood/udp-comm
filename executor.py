import os


class Executor(object):
    def __init__(self, opts=None):
        if opts is None:
            opts = dict()
        self.opts = opts

    def _get_func(self, type):
        return {
            "proxy": self.proxy,
        }[type]

    def proxy(self, **kwargs):
        all_args = {**kwargs, **self.opts}
        proxy_args = ("host", "port", "proxy_script", "sh")

        host, port, proxy_script, sh = [all_args[k] for k in proxy_args]

        message_header = "#!/bin/{0}\n\n".format(sh)
        message_footer = "export http_proxy=$addr\n" \
                         "export https_proxy=$addr\n" \
                         "unset addr\n"

        os.makedirs(os.path.dirname(proxy_script), 0o755, exist_ok=True)
        with open(proxy_script, "w") as f:
            message = message_header + "addr=http://{0}:{1}\n".format(host, port) + message_footer
            f.write(message)

    def process_data(self, data, host):
        type, args = data
        args["host"] = host

        func = self._get_func(type)
        func(**args, **self.opts)
