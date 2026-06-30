import logging

logging.basicConfig(

    
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]

)

logger=logging.getLogger('ArithmethicApp')

def add(a,b):
    result=a+b
    logger.debug(f"Adding{a}+{b}={result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"substraction {a}-{b}={result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"multiply {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"divide {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error('division by zero is error')
        return None 

add(15,10)
sub(15,10)
mul(15,10)
divide(20,0)
