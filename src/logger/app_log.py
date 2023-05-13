import logging.config
import os
from logging.handlers import RotatingFileHandler

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
log_path = os.path.join(root, "logs", "my_log.log")
try:
    file_handler = RotatingFileHandler(log_path, maxBytes=2000, backupCount=10)
except FileNotFoundError:
    os.makedirs(os.path.dirname(log_path))
    file_handler = RotatingFileHandler(log_path, maxBytes=2000, backupCount=10)

file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class AppLog:
    @classmethod
    def debug(cls, msg=None, exc_info=True):
        logging.debug(msg, exc_info=exc_info)

    @classmethod
    def error(cls, msg=None, exc_info=None):
        if not exc_info:
            logging.error(msg)
            return

        _, _, exc_traceback = exc_info
        f_locals = exc_traceback.tb_frame.f_locals if exc_traceback else None
        f_locals_str = cls.pretty(f_locals) if f_locals else None
        logging.error("%s\n %s", msg, f_locals_str, exc_info=exc_info)

    @classmethod
    def pretty(cls, data):
        """
        Pretty representation
        :param data:
        :return:
        """
        text = ""
        if isinstance(data, dict):
            for key, value in data.items():
                text += f"{key}: {value}\n"
        elif isinstance(data, list):
            for item in data:
                text += f"{item}\n"
        return text
