import os
from logger.logger import Applogs

log = Applogs('logger\logs\project.logs', 'DEBUG')
log.getlogger(__file__)

log.debug("debug logged")
log.info("info logged")
log.warning("warning logged")
log.critical("critical logged")