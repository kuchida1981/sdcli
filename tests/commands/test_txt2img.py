from unittest import mock

from click.testing import CliRunner

from app import sdcli


def test_txt2img():
    runner = CliRunner()
    with mock.patch("app.sdcli_context.SdcliContext.txt2img", autospec=True):
        result = runner.invoke(sdcli, ["--format", "json", "txt2img"])
        assert result.exit_code == 0
