from math import factorial
from decimal import *
from time import time
from logger import *

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

        work_data = self.calc_work_time(*args)
        self.work_data = work_data
        work_time = work_data[-1]

        print(str(work_time) + " seconds")
        self.logger.INFO(str("function {} called with arguments {} \n".format(
            self.function, args
        )))

        result = work_data[0:-1]
        return result

    def calc_work_time(self, *args):
        start_time = time()

        result = self.function(*args)

        finish_time = time()

        work_time = finish_time - start_time

        return [result, work_time]

class HTMLDecorator(DecoratorForVeryLongFunction):
    def __init__(self, function):
        self.function = function
        self.logger = MyLogger()
     
    def __call__(self, *args):
        work_data = super().__call__(*args)
        work_time = work_data[-1]

        with open("HTML_decorator.html","a") as file:
            message = "<html><body>{}</html></body>".format(str(work_time))
            file.write(message)
        
        result = self.work_data[0:-1]
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
