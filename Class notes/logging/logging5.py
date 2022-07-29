import logging

logging.basicConfig(filename='test3.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

try:
    logging.info('I am trying to read a file')
    with open('saketh.txt','r'):
        logging.info('It has read the file succesfully','r')

except Exception as e:
    logging.critical('This is a situaton for us')
    logging.error(e)
    logging.exception(e)