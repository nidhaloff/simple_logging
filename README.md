# PETP_logging

A standard Logging Format or rather Definition was needed for all the PETP Services, The Team defined the Format for the specific logs 
and how the logs should be used. here is a Description of how the PETP_logging Module should be used.

**Description:**

The PETP_logging uses the built in python logging Module so no need to install external stuff. also the best Practice is accomplished when using
an extra Configuration file for all the definitions of logs, handlers and Formatters to maintain consistency. so in the Repository a Configuration
File logging.ini can be found which describe how should the logging be within the PETP Project.

> The Config File include a Definition of loggers, handlers and  formatters as you can see when you open the logging.ini File
> The file must contain sections called [loggers], [handlers] and [formatters] which identify by name the entities of each type which
> are defined in the file. For each such entity, there is a separate section which identifies how that entity is configured. 
> Thus, for a logger named ***custom*** in the [loggers] section, the relevant configuration details are held in a section [logger_custom].
> Similarly, a handler called ***console*** in the [handlers] section will have its configuration held in a section called [handler_console],
> while a formatter called ***standard_format*** in the [formatters] section will have its configuration specified in a section called [formatter_standard_format]. 
> The ***root*** logger configuration must be specified in a section called [logger_root].

so to wrap it up, we have in the default configuration 2 loggers, 1 handler and 1 Format:

| Loggers | handlers | Formatters|
| ------ | ------ | ------ |
| root | console |  standard_format |
| custom | console |  standard_format |

this means our root and custom logger use the same default parameters which are a console handler which is a handler responsible to log
statements to the console. there are other types of handler for example a FileHandler to write statements to a file or EmailHandler etc...
but for our PETP only the consoleHandler is needed for now. maybe we will extend the Functionality later but for now a console log will do the Job.

**HOW_TO_USE**

the Simplest way to use the PETP_logging in my point of vue is when you copy the logging.ini and the logs.py locally in your Project.
then you ll have to import the create_logger function in the logs.py in every Module of your Project and simply call the function
create_logger to create a custom logger for that Module. The function take a name and a Path as Parameters. The best Practice is that
the Name should be set to the __name__ special variable which will be set to the module name at run name and this way every logger will be set
to a meaningfull name from your Project, However the Developer can also define a name when it makes Sense for him to do that.
Now the Path Variable is the Path of the Configuration file in your Project, you can look in this Repository I uploaded some Tests to test
and show the Functionality and the way to use the PETP_logging.

another way to use the PETP_logging is to copy the Configuration File in your Project and call this in every Module:
```
logging.config.fileConfig(path_to_config_file, disable_existing_loggers=False) # here you call the configurations
your_logger = logging.getLogger(__name__)   # here is the creation of your custom module logger

your_logger.info("logger created")
```
and then you can easily use your_logger object to log whatever you want inside the Project.

**Important**


| Level | Numeric Value |
| ------ | ------ |
| CRITICAL | 50 |
| ERROR | 40 | 
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 | 
>  Note that the logging module have 5 Levels and there is a good reason why they are called "Levels"

you can set your custom logger to log any level you want, in our default logger in the Config File the handler ist set to log INFO level
but it's important to notice that not only info levels will be logged rather all the Levels above too.
for example let's take the object your_logger from the previous declaration. The logger ist set to the logging level INFO that means 
you can log with it the info, warning, error and critical statements but you can't log the debug statements. similarly, if you
set your logger to the logging level ERROR then you will only log the error and critical statement and you ll not be able
to log the other ones below that level. 
so the default in the Config File is set to INFO but let's say you want for debugging purposes to include debug statements in your code.
you can override the value of the logging Level whenever you want inside your Project. this Code will do the Job:

`self.logger.setLevel(logging.DEBUG)    # this will override the INFO value in the Config File and then you can log also debug statements in your code`

> Note: the default value was INFO and not DEBUG because DEBUG will print all the automated statements which will be printed from RabbitMQ
> and that's annoying to see many logs than the essential ones. that's why the default value was INFO and not DEBUG but as described here,
> the value can be ovveriden, so every Developer should be able to customize his Logger as he wants.




