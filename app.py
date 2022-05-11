import os
from logger.logger import Applogs

log = Applogs('logger\logs\projectlogs.log', 'DEBUG')
log.getlogger(__file__)

log.debug("debug logged")
log.info("info logged")
log.warning("warning logged")
log.critical("critical logged")