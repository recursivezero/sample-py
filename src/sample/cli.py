import click

from . import __version__


@click.group(
    invoke_without_command=True,
    help="""
Sample command-line tools.

To configure MongoDB support, install with:

    pip install sample[mongo]
""",
)
@click.option("--version", is_flag=True, help="Show the Sample version and exit.")
@click.pass_context
def cli(ctx, version):
    if version:
        click.echo(__version__)
        ctx.exit()


@cli.command(help="Run the Sample Streamlit app.")
@click.option(
    "--port", default=8501, show_default=True, help="Port to run the Streamlit app on."
)
def dev(port: int):
    from sample.__main__ import main

    main(port)


@cli.command(help="Run the Sample FastAPI backend.")
@click.option(
    "--port",
    default=5000,
    show_default=True,
    help="Port to run the FastAPI backend on.",
)
def api(port: int):
    from sample.api.fast_api import start

    start(port)
