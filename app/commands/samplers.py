import click

from .. import sdcli_context


@click.command()
@sdcli_context.pass_context
def samplers(context, **kwargs):
    context.samplers(**kwargs)
