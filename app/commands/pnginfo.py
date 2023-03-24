import base64

import click

from .. import sdcli_context


@click.command()
@sdcli_context.pass_context
@click.argument("image", type=click.File("rb"), required=True, nargs=1)
def pnginfo(context, image, **kwargs):
    context.pnginfo(image=base64.b64encode(image.read()).decode("utf8"), **kwargs)
