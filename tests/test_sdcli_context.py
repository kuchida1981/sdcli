import json
import unittest
from unittest import mock

from app import sdcli_context


def test_formatters_1():
    _formatters = {
        "json": lambda data: "hoge",
    }
    instance = mock.MagicMock(format="json")
    sdcli_context.formatters(_formatters)(lambda *args, **kwargs: "xxx")(instance)
    assert instance.out.call_args == mock.call("hoge")


def test_formatters_2():
    _formatters = {
    }
    instance = mock.MagicMock(format="json")
    sdcli_context.formatters(_formatters)(lambda *args, **kwargs: {"name": "xxx"})(instance)
    assert instance.out.call_args == mock.call(json.dumps({"name": "xxx"}))


class SdcliContextTests(unittest.TestCase):

    def setUp(self):
        self.context = sdcli_context.SdcliContext()
        self.context.format = "json"
        self.context.url = "http://xxx"

    @mock.patch("click.echo", autospec=True)
    def test_out(self, click_echo):
        self.context.out("hoge")
        assert click_echo.call_args == mock.call("hoge")

    @mock.patch("requests.post", autospec=True)
    def test_txt2img(self, post):
        post.return_value = mock.MagicMock(json=mock.MagicMock(return_value={}))
        assert self.context.txt2img() is None

    @mock.patch("requests.post", autospec=True)
    def test_pnginfo(self, post):
        self.context.format = "text"
        post.return_value = mock.MagicMock(
            json=mock.MagicMock(
                return_value={"info": "hogehoge"},
            ),
        )
        assert self.context.pnginfo() is None

    @mock.patch("requests.get", autospec=True)
    def test_samplers(self, post):
        self.context.format = "text"
        post.return_value = mock.MagicMock(
            json=mock.MagicMock(
                return_value=[{"name": "a"}, {"name": "b"}],
            ),
        )
        assert self.context.samplers() is None

    @mock.patch("requests.get", autospec=True)
    def test_sdmodels(self, post):
        self.context.format = "text"
        post.return_value = mock.MagicMock(
            json=mock.MagicMock(
                return_value=[{"title": "a"}, {"title": "b"}],
            ),
        )
        assert self.context.sdmodels() is None

    @mock.patch("requests.post", autospec=True)
    def test_change_options(self, post):
        self.context.format = "text"
        post.return_value = mock.MagicMock(
            json=mock.MagicMock(
                return_value={},
            ),
        )
        assert self.context.change_options() is None
