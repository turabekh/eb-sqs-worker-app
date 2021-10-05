import logging 

logger = logging.getLogger() 



def log_error(message, method=""):
    logger.error(f"ERROR | METHOD: {method}  | message: {message}")

def log_info(message, method=""):
    logger.info(f"INFO | METHOD: {method} | message: {message}")