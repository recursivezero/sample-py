import click
from . import __version__


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the Sample version and exit.")
@click.pass_context
def cli(ctx, version):
    """Sample command-line tools."""
    if version:
        click.echo(__version__)
        ctx.exit()


@cli.command()
def dev():
    """Run the Sample Streamlit app."""
    from sample.__main__ import main

    main()


@cli.command()
def api():
    """Run the Sample FastAPI backend."""
    from api.fast_api import start

    start()
