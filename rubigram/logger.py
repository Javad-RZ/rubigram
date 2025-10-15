import logging
import sys


class RubigramFormatter(logging.Formatter):
    def format(self, record):
        module_name = record.name
        log_time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        level = record.levelname.upper().ljust(5)
        message = record.getMessage()
        return f"{log_time} | {level} | {module_name} | {message}"


logger = logging.getLogger("rubigram")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(RubigramFormatter())
    logger.addHandler(handler)