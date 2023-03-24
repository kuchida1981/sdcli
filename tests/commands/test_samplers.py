from unittest import mock

from click.testing import CliRunner

from app import sdcli


def test_sampler():
    runner = CliRunner()
    with mock.patch("app.sdcli_context.SdcliContext.samplers", autospec=True):
        result = runner.invoke(sdcli, ["--format", "json", "samplers"])
        assert result.exit_code == 0
