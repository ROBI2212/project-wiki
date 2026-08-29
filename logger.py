import logging
import datetime

logger = logging.getLogger(__name__)
date = datetime.datetime.now()

# FUNCTION TO FORMAT A DATE FOR LOG ENTRIES
def logging_date():
    return (f'{date.strftime("%d")} {date.strftime("%B")} {date.strftime("%Y")} {date.strftime("%X")}')

# LOG CONFIG
logging.basicConfig(filename='project-wiki.log', encoding='utf-8', level=logging.INFO)
logger.info(f' {logging_date()} | Moduł logów załączony prawidłowo.')