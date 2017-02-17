from datetime import datetime
startTime = datetime.now()


import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log.log',
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)


print datetime.now() - startTime



#Google python using logging from another file
#http://stackoverflow.com/questions/17035077/python-logging-to-multiple-log-files-from-different-classes
#Google python logging library example
#https://docs.python.org/2/howto/logging.html
#http://stackoverflow.com/questions/9321741/printing-to-screen-and-writing-to-a-file-at-the-same-time
