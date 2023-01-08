from math import factorial
from decimal import *
from time import time
from MyLogger import *

class AlterBehavior(type):

    def __call__(*args):
        return True


# передавать объект в аргмент, а не bool
class DecoratorForVeryLongFunction:
    def __init__(self, function):
        self.function = function
        self.logger = MyLogger()
        self.status = None
     
    def __call__(self, *args):
        self.logger.config()
        start_time = time()

        result = self.function(args[0][0])

        finish_time = time()
        work_time = finish_time - start_time

        print(str(work_time) + " seconds")
        self.logger.INFO(str("function {} called with arguments {} \n".format(
            self.function, args
        )))
        
        if self.status == True:
            return (finish_time,result)
        else:
            return result

class HTMLDecorator:
    def __init__(self, function):
        self.function = function
        self.logger = MyLogger()
     
    def __call__(self, *args):
        
        self.logger.config()

        if isinstance(self.function, DecoratorForVeryLongFunction):
            # result = self.function(*args,**kwargs)
            result = self.function.__call__(args, AlterBehavior.__call__())

            with open("HTML_decorator.html","a") as file:
                message = "<html><body>{}</html></body>".format(result)
                file.write(message)
            
            self.logger.INFO(str("{}: function {} called with arguments {} \n".format(
                localtime(int(result)),
                args[0], args[1:]
            )))

            # return all function results
            return result
            
        else:
            
            start_time = time()
            result = self.function(*args)

            finish_time = time()
            work_time = finish_time - start_time

            with open("HTML_decorator.html","a") as file:
                message = "<html><body>{}</html></body>".format(str(finish_time))
                file.write(message)

            print(str(work_time) + " seconds")
            self.logger.INFO(str("{}: function {} called with arguments {} \n".format(
                localtime(finish_time),
                args[0],
                args[1:]
            )))
            return result


@HTMLDecorator
@DecoratorForVeryLongFunction
def veryLongFunction(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi

print(veryLongFunction(500))
