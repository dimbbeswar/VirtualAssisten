import logging

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s %(lineno)d} %(filename)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)