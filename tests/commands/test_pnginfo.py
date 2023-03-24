from unittest import mock

from click.testing import CliRunner

from app import sdcli


def test_pnginfo():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("hoge.png", "wb") as f:
            f.write(b"hello")

        with mock.patch("app.sdcli_context.SdcliContext.pnginfo", autospec=True):
            result = runner.invoke(sdcli, ["--format", "json", "pnginfo", "hoge.png"])
            assert result.exit_code == 0
