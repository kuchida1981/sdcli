from unittest import mock

from click.testing import CliRunner

from app import sdcli


def test_change_options():
    runner = CliRunner()
    with mock.patch("app.sdcli_context.SdcliContext.change_options", autospec=True):
        result = runner.invoke(
            sdcli,
            [
                "--format",
                "json",
                "change-options",
                "--sd-model-checkpoint",
                "xxx",
            ],
        )
        assert result.exit_code == 0
