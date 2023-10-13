import logging

ALLOWED_MODES = ("dirs", "desktop")


def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="myapp.log",
        filemode="w"
    )
    
