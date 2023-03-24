import click

from .. import sdcli_context


@click.command()
@sdcli_context.pass_context
def sdmodels(context, **kwargs):
    context.sdmodels(**kwargs)
