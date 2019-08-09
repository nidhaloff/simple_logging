import logging.config


def create_logger(name, path='logging.ini'):
	logging.config.fileConfig(path, disable_existing_loggers=False)
	logger = logging.getLogger(name)
	return logger


