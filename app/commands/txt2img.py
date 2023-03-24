import json

import click

from .. import sdcli_context


@click.command()
@click.argument("file", required=False, type=click.File("r"), nargs=1)
@click.option("--prompt", "prompt", type=str)
@click.option("--negative-prompt", "negative_prompt", type=str)
@click.option("--batch-size", "batch_size", type=int, default=1, show_default=True)
@click.option("--batch-count", "n_iter", type=int, default=1, show_default=True)
@click.option("--seed", "seed", type=int, default=-1, show_default=True)
@click.option("--steps", "steps", type=int, default=20, show_default=True)
@click.option("--cfg-scale", "cfg_scale", type=int, default=7, show_default=True)
@click.option("--restore-faces/--no-restore-faces", "restore_faces", default=True, show_default=True)
@click.option("--sampler-index", "sampler_index", type=str, default="Euler a", show_default=True)
@click.option("--save-images/--no-save-images", "save_images", default=True, show_default=True)
@sdcli_context.pass_context
def txt2img(context, file, **kwargs):
    context.txt2img(**(json.load(file) if file is not None else kwargs))
