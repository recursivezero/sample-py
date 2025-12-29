import logging
from pathlib import Path
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

__version__ = "0.1.0"
PORT = 8000


def main():
    print("🏷️ Sample version:", __version__)
    logging.info("Starting static HTML server...")

    sample_dir = Path(__file__).resolve().parent.parent

    if "site-packages" in str(sample_dir):
        root = sample_dir
        logging.info("Running from wheel")
    else:
        root = sample_dir.parent
        logging.info("Running in dev mode")

    logging.info(f"Serving from root: {root}")

    os.chdir(root)

    with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"🌐 Open http://localhost:{PORT}/templates/index.html")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
