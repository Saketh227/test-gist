# Why do we need logging?

# load data from multiple sources-----> Merge these data ----> filter data-----> store in a database

# due to glitch in program there will be a problem.

# To know where problem has occured in the above process

# '''instead of print which is used to check everytime inside a console ,
#        say if we want to check after few days we store data in logging file'''


import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is my very first code for logging")
logging.info("hope this can be easy")
logging.warning('this will try to load a warning message')
logging.error("this is a error message for system")


l=[1,2,3,4,5,6]
for i in l:
    if i ==2:
        logging.info(i)
        logging.warning('This is a warning for user that they have found out 2 in list')

logging.shutdown()
# types of logging
# total:5
# log level=debuug # 10
# log level=INFO # 20
# log level=warning # 30
# log level =error # 40
# log level = critical # 50

# when to use which level
# There is a hierarchy and we need to follow this
