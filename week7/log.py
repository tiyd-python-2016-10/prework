import logging

#logging.basicConfig(filename='example.log',level=logging.DEBUG)

#logging.warning('Watch out!') # will print a message to the console
#logging.info('I told you so') # will not print anything

#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

FORMAT = '%(levelname)s: %(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, filename='example.log')
d = {'clientip': '192.168.0.1', 'user': 'foobar'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
