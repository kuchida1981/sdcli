import click

from .. import sdcli_context


@click.command(name="change-options")
@sdcli_context.pass_context
@click.option("--sd-model-checkpoint", "sd_model_checkpoint", type=str)
def change_options(context, **kwargs):
    context.change_options(**kwargs)
