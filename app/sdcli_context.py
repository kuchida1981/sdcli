import json

import click
import requests

defaults_formetters = {
    "json": lambda data: json.dumps(data),
    "text": lambda data: "OK",
}


def formatters(formatters):
    def _output(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            instance = args[0]
            format_type = instance.format
            format = formatters.get(format_type) or defaults_formetters[format_type]
            instance.out(format(data))
            return
        return wrapper
    return _output


class SdcliContext(object):

    def __init__(self):
        pass

    def init_context(self, url, format):
        self.url = url
        self.format = format

    def out(self, value):
        click.echo(value)

    @formatters({})
    def txt2img(self, **kw):
        path = "/sdapi/v1/txt2img"
        response = requests.post(self.url + path, json=kw)
        response.raise_for_status()
        return response.json()

    @formatters(
        {
            "text": lambda item: item["info"],
        }
    )
    def pnginfo(self, **kw):
        path = "/sdapi/v1/png-info"
        response = requests.post(self.url + path, json=kw)
        response.raise_for_status()
        return response.json()

    @formatters(
        {
            "text": lambda items: "\n".join(map(lambda item: item["name"], items)),
        },
    )
    def samplers(self, **kw):
        path = "/sdapi/v1/samplers"
        response = requests.get(self.url + path)
        response.raise_for_status()
        return response.json()

    @formatters(
        {
            "text": lambda items: "\n".join(map(lambda item: item["title"], items)),
        },
    )
    def sdmodels(self, **kw):
        path = "/sdapi/v1/sd-models"
        response = requests.get(self.url + path)
        response.raise_for_status()
        return response.json()

    @formatters(
        {
        }
    )
    def change_options(self, **kw):
        path = "/sdapi/v1/options"
        response = requests.post(self.url + path, json=kw)
        response.raise_for_status()
        return response.json()


pass_context = click.make_pass_decorator(SdcliContext, ensure=True)
