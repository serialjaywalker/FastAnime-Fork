import click

from .. import __version__
from ..libs.anime_provider.allanime.constants import SERVERS_AVAILABLE
from ..Utility.data import anilist_sort_normalizer
from .commands.anilist import anilist
from .commands.config import configure
from .commands.download import download
from .commands.search import search
from .config import Config

commands = {
    "search": search,
    "download": download,
    "anilist": anilist,
    "config": configure,
}


@click.group(commands=commands, invoke_without_command=True)
@click.version_option(__version__, "--version")
@click.option(
    "-s",
    "--server",
    type=click.Choice(SERVERS_AVAILABLE, case_sensitive=False),
)
@click.option("-h", "--hist", type=bool)
@click.option("-q", "--quality", type=int)
@click.option("-t-t", "--translation_type")
@click.option("-a-n", "--auto-next", type=bool)
@click.option(
    "-s-b",
    "--sort-by",
    type=click.Choice(anilist_sort_normalizer.keys()),  # pyright: ignore
)
@click.option("-d", "--downloads-dir", type=click.Path())
@click.pass_context
def run_cli(
    ctx: click.Context,
    server,
    hist,
    translation_type,
    quality,
    auto_next,
    sort_by,
    downloads_dir,
):
    ctx.obj = Config()
    if server:
        ctx.obj.server = server
    if hist:
        ctx.obj.continue_from_history = hist
    if quality:
        ctx.obj.quality = quality
    if auto_next:
        ctx.obj.auto_next = auto_next
    if sort_by:
        ctx.obj.sort_by = sort_by
    if downloads_dir:
        ctx.obj.downloads_dir = downloads_dir
    if translation_type:
        ctx.obj.translation_type = translation_type