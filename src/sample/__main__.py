# sample/__main__.py

from . import __version__
import sys
import logging
import subprocess
from pathlib import Path
import click

logging.basicConfig(level=logging.INFO)


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the Threadzip version and exit.")
@click.pass_context
def cli(ctx, version):
    """Threadzip command-line tools."""
    if version:
        click.echo(__version__)
        ctx.exit()


@cli.command()
def dev():
    """Run the Threadzip Streamlit app."""
    main()


@cli.command()
def api():
    """Run the Threadzip FastAPI backend."""
    from api.fast_api import start

    start()


def main():
    """
    Entrypoint for the Streamlit 'dev' app.
    """
    print("🏷️ Threadzip version:", __version__)
    logging.info("Starting sample dev script...")

    # Paths
    threadzip_dir = Path(__file__).resolve().parent
    dev_root = threadzip_dir.parent  # src/
    wheel_root = threadzip_dir.parent  # same in wheel

    # Add correct root to sys.path
    if "site-packages" in str(threadzip_dir):  # running from wheel
        if str(wheel_root) not in sys.path:
            sys.path.append(str(wheel_root))
            logging.info(f"Added wheel root to sys.path: {wheel_root}")
    else:  # dev mode
        if str(dev_root) not in sys.path:
            sys.path.append(str(dev_root))
            logging.info(f"Added dev src root to sys.path: {dev_root}")

    # Locate streamlit_app.py
    streamlit_app_path = threadzip_dir / "streamlit_app.py"
    logging.info(f"Streamlit app path: {streamlit_app_path}")

    if not streamlit_app_path.exists():
        logging.error(f"Streamlit app not found at: {streamlit_app_path}")
        return

    # Run Streamlit app
    python_path = sys.executable
    logging.info(f"Using Python executable: {python_path}")

    subprocess.run(
        [
            python_path,
            "-m",
            "streamlit",
            "run",
            str(streamlit_app_path.resolve()),
            "--server.port",
            "8501",
        ],
        check=True,
    )


if __name__ == "__main__":
    cli()
