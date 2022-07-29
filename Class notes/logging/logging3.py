# how to store input from user
import logging
logging.basicConfig(filename='test1.log',level=logging.INFO,format='%(asctime)s %(name)s %(levelname)s %(message)s')

def divide(a,b):
    logging.info('the number entered by user is %s and %s ' ,a,b)
    try:
        logging.info('We are in function')
        div = a/b
        logging.info('We have completed the operation')
        logging.info("the result is %s ",div)
        return div
    except Exception as e:
        logging.exception(e)
print(divide(3,4))

print(divide(4,0))


