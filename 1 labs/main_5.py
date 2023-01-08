import functools
import datetime as dt
import time

def time_decorator(func):
    
    def time_exec_func(*args,**kwargs):
        print(f"Your function: {func}")
        start = time.perf_counter()
        result = func(*args,**kwargs)
        result_time = time.perf_counter() - start
        print(f"runtime: {result_time:.4f}")
        return result

    return time_exec_func

@time_decorator
def hello_word():
    print("Hello World!!!")
    print("wait")
    time.sleep(10)
    print("end of wait")

@time_decorator
def func_for (lst:list) -> list:
    
    for num in range(len(lst)):
        lst[num] **= 2
    return lst

@time_decorator
def func_comprehension(lst:list) -> list:
    lst = [n**2 for n in lst]
    return lst

@time_decorator
def func_map(lst:list) -> list:
    lst = list(map(lambda x: x**2,lst))
    return lst

@time_decorator
def gen_list(n):
    lst = list()
    for num in range(1,n):
        lst.append(num)
    return lst


if __name__ == "__main__":
    lst = gen_list(10000000)
    
    func_comprehension(lst)
    func_map(lst)
    func_for(lst)

