# sample/__main__.py

import logging
import subprocess
import sys
from pathlib import Path

from . import __version__


def main(port: int = 8501):
    """
    Entrypoint for the Streamlit 'dev' app.
    """
    print("🏷️ Sample version:", __version__)
    logging.info("Starting sample dev script...")

    Sample_dir = Path(__file__).resolve().parent
    dev_root = Sample_dir.parent
    wheel_root = Sample_dir.parent

    if "site-packages" in str(Sample_dir):
        if str(wheel_root) not in sys.path:
            sys.path.append(str(wheel_root))
            logging.info(f"Added wheel root to sys.path: {wheel_root}")
    else:
        if str(dev_root) not in sys.path:
            sys.path.append(str(dev_root))
            logging.info(f"Added dev src root to sys.path: {dev_root}")

    streamlit_app_path = Sample_dir / "streamlit_app.py"
    logging.info(f"Streamlit app path: {streamlit_app_path}")

    if not streamlit_app_path.exists():
        logging.error(f"Streamlit app not found at: {streamlit_app_path}")
        return

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
            str(port),
        ],
        check=True,
    )


if __name__ == "__main__":
    main(port=8501)
