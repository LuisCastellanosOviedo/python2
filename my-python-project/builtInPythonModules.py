import os
import logging

print(os.name)


logger = logging.getLogger("MAIN")
logger.error("Error in the app")
