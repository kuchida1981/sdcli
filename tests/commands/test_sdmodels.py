from unittest import mock

from click.testing import CliRunner

from app import sdcli


def test_sdmodels():
    runner = CliRunner()
    with mock.patch("app.sdcli_context.SdcliContext.sdmodels", autospec=True):
        result = runner.invoke(sdcli, ["--format", "json", "sdmodels"])
        assert result.exit_code == 0
