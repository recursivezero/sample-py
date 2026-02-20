from sample.utils.constants import PORT


def main():
    """Entry point for CLI dev command."""
    from sample.api.main import start

    print(f"🚀 Starting Sample app on port {PORT}...\n")
    start()


if __name__ == "__main__":
    main()
