# what about hierarchy

# debug
# info
# warning
# error
# critical


# if we use any level ,then in log file we get the mentiond level and the levels below it as mentioned above

import logging
logging.basicConfig(filename='test2.log',level=logging.CRITICAL,format='%(asctime)s %(name)s %(levelname)s %(message)s')

def divide(a,b):
    logging.info('the number entered by user is %s and %s ' ,a,b)
    try:
        logging.info('We are in function')
        div = a/b
        logging.info('We have completed the operation')
        logging.info("the result is %s ",div)
        return div
    except Exception as e:
        logging.warning(e)
print(divide(3,4))
print(divide(4,0))


logging.info('---------------------------------------------------------------')
logging.shutdown()


