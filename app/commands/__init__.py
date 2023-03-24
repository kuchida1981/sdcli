import click

from .options import change_options
from .pnginfo import pnginfo
from .samplers import samplers
from .sdmodels import sdmodels
from .txt2img import txt2img

commands = [txt2img, samplers, pnginfo, sdmodels, change_options]


def init_cli(cli: click.Group):
    for cmd in commands:
        cli.add_command(cmd)
