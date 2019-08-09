from logs import create_logger


class TestLogging:
	def __init__(self):
		self.logger = create_logger(__name__, path="../logging.ini")  # this will create a logger object with the default module name


	def first_test(self):
		try:
			file = open('wtf_log', 'r').read()
			self.logger.info("file opened successfully")
		except Exception as e:
			self.logger.exception(f"Critical Error occured => args: {e.args}", exc_info=True) # exc_info set to true will log the Description of the Exception

	def second_test(self, *args):
		try:
			if type(args[0]) == str:
				self.logger.info(f"log the string argument for debugging purposes") # info msg
			elif type(args[0]) == int:
				self.logger.warning(f"this function should receive a string and not integer")   # warning msg

		except Exception as e:
			self.logger.exception(f"we can also log only the arguments of the exception"
			                      f"args => {e.args}", exc_info=False)  # exc_info set to False will not log a full Description of the Exception, only the args will be logged
	def third_test(self):
		self.logger.info("the statement below is a debug statement and thus it will not be logged")
		self.logger.debug("the level is set to INFO which is above the DEBUG level that's why this will never be printed")

test = TestLogging()
#test.second_test("ss")   # should logs an info log
#test.second_test(11) # should log a warning
#test.second_test()   # should log an Exception
#test.first_test()   # should log an Exception with a full Description
test.third_test()  # only the info log will be logged