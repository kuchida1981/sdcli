import click

from . import commands, sdcli_context


@click.group()
@click.option("-h", "--url", type=str, default="http://127.0.0.1:7860", show_default=True)
@click.option("-f", "--format", type=click.Choice(["text", "csv", "json"]), default="text")
@sdcli_context.pass_context
def sdcli(context, url: str, format: str):
    context.init_context(url, format)


commands.init_cli(sdcli)
